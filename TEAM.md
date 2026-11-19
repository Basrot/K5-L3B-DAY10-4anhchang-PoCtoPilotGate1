# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `4anhchang`
- Lớp: `L3A` / `L3B`: `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`:
  `K5-L3B-DAY10-4anhchang-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S7`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Thiều Thế Ngọc | 2A202603788 | Kỹ sư cổng |             |
|   2 | Nguyễn Gia Nam | 2A202603761 | Kỹ sư cổng |      x      |
|   3 | Đào Ngọc Hân | 2A202603779 | Sản phẩm và kinh doanh |             |
|   4 | Trần Trọng Đức Tài | 2A202603732 | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## ThieuTheNgoc-2A202603788

### Phần việc phụ trách

Kỹ sư cổng: viết cổng trong `lab10/guards.py`; chủ trì các cổng vòng 1, trace, behavioral test và Phiếu B mục B7.1–B7.3.

### Đóng góp cụ thể

Đã chủ trì thiết kế và chốt cổng vòng 1 trong `lab10/guards.py`, bao gồm ghim chính sách theo `as_of`, kiểm tra hoàn trùng và hạn mức/tài liệu tracking, chuẩn hóa lỗi hãng và allowlist dữ liệu gửi carrier; hoàn thiện runbook phần cổng phòng ngừa, công tắc dừng khẩn cấp và Quyết định Gate 1 vòng 1; chạy/đối chiếu báo cáo base, after và trace `T-002@55`.

### Bằng chứng

Mã commit: `9395859`, `f3ac175` · Mã lần chạy: `R-base-after-20261119-161030-b3b3af` · Dòng trong phiếu: B7.1–B7.3 · File: `lab10/guards.py`

### Exit ticket

Một điều học được: Cổng ở bên ngoài model cần đối chiếu trực tiếp nguồn sự thật (tracking, policy, ledger) thay vì tin dữ liệu do agent hoặc khách tự khai. · Một điều còn chưa chắc: Ngưỡng cho công tắc dừng khẩn cấp và dung sai tự động hóa khi pilot mở rộng nhiều kho/luồng ngoài dữ liệu giả.

## NguyenGiaNam-2A202603761

### Phần việc phụ trách

Kỹ sư cổng phụ trách đo lường và phân tích trace: chạy các mốc, đọc `T-002@55`, B0–B2, trace thẻ, thêm chỉ số trong `lab10/monitors.py` và Phiếu C mục C1–C2, C8.

### Đóng góp cụ thể

Đã chạy bài kiểm tra công khai, mốc base, gate đối chiếu tiêu chí và trace `T-002@55`; điền Phiếu B mục B0–B2; hoàn thành offline metric cho bước chọn độ trễ.

### Bằng chứng

Mã commit: `7b22e51` · Mã lần chạy: `R-base-before-20261119-153147-bde05c` · Dòng trong phiếu: A2, B0–B2, C1–C2, C8

### Exit ticket

Một điều học được: Mốc báo cáo và trace giúp tìm ra bước sai cụ thể thay vì chỉ nhìn tổng pass_rate; chỉ số theo dõi phải tính từ dữ liệu production không nhãn, chứ không dùng nhãn đúng/sai. · Một điều còn chưa chắc: Khi chạy pilot thật, monitor PII có phát hiện đúng PII ở mọi kênh outbound hay chỉ phát hiện được những trường đã được trace ghi lại.

## DaoNgocHan-2A202603779

### Phần việc phụ trách

Sản phẩm và kinh doanh: đồng chốt tiêu chí chấp nhận (Phiếu A), bản đồ dữ liệu và ví dụ drift (`B3`), Pre-mortem lăng kính kinh doanh (`B6`), cổng `business` trong `config/operating_gates.json` và `B7.4`, đồng bộ số liệu Runbook 1–3, chốt cổng vòng 1 (`lab10.checkpoint`), Quyết định Gate 1 v1 (`B8`), rà soát hoàn thiện Phiếu C (`C0`, `C2`, `C5–C9`, `C12`), Quyết định v2 + ba dòng bắt buộc (`submission/submission.json`) và đồng bộ `submission/` chuẩn LF (`check_submission --collect`).

### Đóng góp cụ thể

- Thiết lập 4 cổng kinh doanh trong `config/operating_gates.json` mục `business` dựa trên ước lượng Fermi từ `ops_facts`/`ops_limits`: `daily_refund_cap_vnd = 1.500.000đ` (75% ngân sách Finance `2.000.000đ`), `cost_budget_per_ticket_vnd = 1.100đ` (dự phòng `400đ` các bước sau để không vượt trần LLM `1.500đ`), `pilot_scope` 4 kho đơn lẻ `["HN", "HCM", "DN", "CT"]` (loại chủ động kho sỉ `HCM-B2B` ≥ 2 triệu gây lỗ), `roi_min = 0.2`; đồng bộ lại 3 dòng con số trong Runbook 1–3 cho khớp config.
- Hoàn thiện Bản đồ dữ liệu & Concept Drift `REFUND-v4` (ngày `2026-12-01`) tại `B3`, bổ sung dòng rủi ro kinh doanh `HCM-B2B`/trần LLM vào Pre-mortem `B6`.
- Chạy `lab10.checkpoint` chốt mốc `prepared` (hash `3ea4677b`), chạy đối chiếu `base · prepared` và `base · after`, điền nhật ký `B0` và viết toàn bộ Quyết định Gate 1 · v1 (`Tiếp tục`) tại `B8`.
- Kiểm tra toàn vẹn bài nộp cuối buổi trên thẻ `S7`, phát hiện và xử lý lỗi lệch hash CRLF/LF + khôi phục đầy đủ `journal.jsonl` của cả nhóm, hoàn thiện các mục còn thiếu trong Phiếu C (`C0`, `C2`, `C5–C9`, `C12`) và đồng bộ ba dòng bắt buộc với `submission/submission.json`, chạy `lab10.grade --incident S7` (`PASS-VISIBLE`) và `lab10.check_submission --collect` (`ĐỦ THÀNH PHẦN`).
- *Ghi chú sử dụng AI (`RULES.md`):* Có sử dụng trợ lý AI theo phương pháp hỏi đáp Socratic để hiểu khái niệm thống kê (khoảng tin cậy, `pass^k`, `escalation_rate`), kiểm chứng tính toán Fermi cho chi phí/ROI, rà soát độ nhất quán câu chữ giữa các phiếu và kiểm tra lỗi kỹ thuật Git/hash LF.

### Bằng chứng

Mã commit: `0d373be`, `9d203a2`, `305d6e7` (và commit hoàn thiện cuối buổi) · Mã lần chạy: `R-base-prepared-20261119-162423-64330d`, `R-base-after-20261119-162757-64330d`, `R-S7-grade-20261119-165927-37dae7`, `R-base-after-20261119-165638-f9f77e` · Dòng trong phiếu: A1–A5 (đồng ký `4e9908d`), B0, B3, B6, B7.4, B8, C0, C2, C5–C9, C12 · File: `config/operating_gates.json`, `config/round1.lock`, `submission/submission.json`.

### Exit ticket

Một điều học được: Quyết định đưa AI từ PoC sang Pilot không thể chỉ nhìn `pass_rate` mà phải đặt tiêu chí bằng ước lượng kinh tế thực tế (chi phí AI + công người duyệt + phí giữ chỗ + thiệt hại hoàn oan/PII) trước khi đo, và các cổng phòng ngừa ngoài model như allowlist (`notify_carrier`) và khoanh vùng `pilot_scope` có thể NGĂN hẳn thiệt hại ngay cả trước khi sự cố xảy ra. · Một điều còn chưa chắc: Khi triển khai thật từ `2026-12-01` với chính sách `REFUND-v4` (hạ hạn mức tự động xuống `100.000đ`), tỷ lệ đơn đẩy sang người duyệt và tải hàng chờ giờ cao điểm ngoài thực tế sẽ tăng mạnh tới mức nào và có cần điều chỉnh lại số người trực hay `pilot_scope` không.

## TranTrongDucTai-2A202603732

### Phần việc phụ trách

Vận hành và pháp lý: HAZOP, checklist 9 nhóm, cổng `operations` và `legal`, runbook, giờ cao điểm, HAZOP của thẻ, gom bài nộp và `submission/submission.json`.

### Đóng góp cụ thể

Hoàn thành phân tích HAZOP vòng 1 cho tool `issue_refund` (Phiếu B mục B4); rà soát Checklist 9 nhóm việc có PIC đích danh (mục B5); cấu hình mục `operations` và `legal` trong `config/operating_gates.json`; hoàn thiện Runbook phần 1–3 (mục B7.5) và quy trình xử lý Giờ cao điểm (mục B7.6). Phối hợp giải quyết sự cố S7 (rò rỉ dữ liệu cá nhân PII của người nhận quà): phân tích rủi ro pháp lý theo Nghị định 13/2023/NĐ-CP, cập nhật allowlist bảo vệ PII, hoàn thiện Runbook phần 4–5 và kiểm tra gom bài nộp `submission.json` đạt ĐỦ THÀNH PHẦN.

### Bằng chứng

Mã commit: `1e29321`, `91f544d` · Mã lần chạy: `R-S7-grade-20261119-164320-b53f96` · Dòng trong phiếu: B4, B5, B7.5, B7.6, C4, C10, C11, C12 · File: `config/operating_gates.json`, `submission/submission.json`

### Exit ticket

Một điều học được: Khi xử lý sự cố lộ dữ liệu cá nhân (PII), cách tiếp cận bảo đảm bằng allowlist nghiêm ngặt tại cổng ra (write gate) hiệu quả và an toàn tuyệt đối hơn việc cố gắng dùng regex để che mờ dữ liệu. · Một điều còn chưa chắc: Việc áp dụng allowlist khắt khe có thể khiến đối tác vận chuyển thiếu thông tin liên lạc trong các trường hợp giao hàng khẩn cấp hay không.
