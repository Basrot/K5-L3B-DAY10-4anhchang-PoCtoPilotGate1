"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không xác định được chính sách hoàn tiền đang hiệu lực")
    return Verdict.allow(policy_id=policy["policy_id"])


def _policy_for_run(ctx):
    policy_event = next((event for event in reversed(ctx.events) if event.get("type") == "policy"), None)
    if policy_event is None:
        return None
    return next((policy for policy in ctx.tools.lookup_policies()
                 if policy["policy_id"] == policy_event.get("policy_id")), None)


def write_gate(ctx, action):
    tool = action["tool"]

    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None or order.get("customer_id") != ctx.ticket.get("customer_id"):
            return Verdict.escalate("không xác minh được chủ đơn từ nguồn dữ liệu")
        policy = _policy_for_run(ctx)
        if policy is None:
            return Verdict.escalate("không xác minh được chính sách dùng để tính tiền hoàn")
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        cause = parcel.get("delay_cause") or ("CARRIER" if delay > 0 else None)
        maximum = H.entitlement_vnd(policy, order, delay, cause)
        amount = action.get("amount_vnd")
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            return Verdict.deny("số tiền hoàn không hợp lệ")
        if amount > maximum:
            return Verdict.modify(
                "giới hạn tiền hoàn theo tracking và chính sách hiệu lực",
                amount_vnd=maximum,
            )
        return Verdict.allow()

    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None:
            return Verdict.deny("không tìm thấy đơn trong nguồn dữ liệu")
        parcel = next((p for p in order.get("parcels", [])
                       if p.get("parcel_id") == action.get("parcel_id")), None)
        policy = _policy_for_run(ctx)
        if parcel is None or policy is None:
            return Verdict.deny("không xác minh được kiện hàng hoặc chính sách hiệu lực")
        delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking không ghi nhận lỗi hãng đủ điều kiện")
        canonical = {
            "carrier_id": parcel["carrier_id"],
            "driver_id": parcel.get("driver_id"),
            "delay_days": delay,
        }
        if any(action.get(key) != value for key, value in canonical.items()):
            return Verdict.modify("chuẩn hóa thông tin lỗi hãng theo tracking", **canonical)
        return Verdict.allow()

    if tool == "notify_carrier":
        payload = action.get("payload")
        if not isinstance(payload, dict):
            return Verdict.deny("nội dung gửi hãng không hợp lệ")
        fault = next((row for row in ctx.tools.fault_rows(
            ticket_id=action.get("ticket_id"),
            order_id=action.get("order_id", payload.get("order_id")),
        ) if row.get("parcel_id") == payload.get("parcel_id")
            and row.get("carrier_id") == action.get("carrier_id")), None)
        if fault is None:
            return Verdict.deny("chỉ gửi hãng thông tin về lỗi đã được xác minh")
        verified_payload = {
            "order_id": fault["order_id"],
            "parcel_id": fault["parcel_id"],
            "delay_days": fault["delay_days"],
        }
        return Verdict.modify(
            "chỉ gửi hãng dữ liệu tối thiểu đã xác minh; loại bỏ nội dung ticket và dữ liệu cá nhân",
            payload=verified_payload,
        )

    return Verdict.allow()
