# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** `K5-L3B-DAY10-4anhchang-PoCtoPilotGate1` · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Tự động hoá xử lý khiếu nại hoàn tiền do giao trễ cho khách hàng cá nhân đạt độ chính xác tài chính tuyệt đối (0đ hoàn sai, 0 lỗi ghi oan cho hãng), giảm chi phí vận hành mỗi ticket từ 10.000đ xuống dưới 8.000đ, duy trì ROI tối thiểu 20% mà không gây quá tải hay ùn tắc hàng chờ CSKH (SLA duyệt dưới 60 phút).

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): 100% các lệnh hoàn tiền và ghi lỗi hãng vận chuyển (strike) phát sinh đều khớp chính xác với tracking DB thực tế, không có khoản tiền hoàn sai (0đ) và không có lỗi ghi oan cho hãng vận chuyển (0 lỗi), đảm bảo biên bản đối soát công nợ cuối tuần với các hãng vận chuyển và đối tác shop minh bạch, không phát sinh tranh chấp hay truy thu công nợ.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Tỷ lệ chuyển người duyệt (escalation rate) không vượt quá 30% tổng số ticket, hàng chờ người duyệt không bao giờ bị ùn ứ (0 ca quá SLA 60 phút), mỗi ca chuyển tiếp đều có đầy đủ thông tin tóm tắt và căn cứ chính sách giúp nhân viên xử lý nhanh trong định mức 10 phút/ca mà không bị quá tải.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Ghi lỗi cho hãng vận chuyển (`file_carrier_fault`) | Toàn bộ các quyết định hoàn tiền và phạt hãng vận chuyển đã ban hành ra ngoài |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ ghi lỗi hãng chính xác (Carrier Fault Precision), đơn vị: % | Tỉ lệ khiếu nại tranh chấp từ hãng vận chuyển / đối tác ngoài (Carrier Dispute Rate), đơn vị: % |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện gọi tool `file_carrier_fault` trong `runs/<mã>/traces/` trên 22 ticket × 5 seed (110 lần chạy); nhãn chuẩn từ chuyên viên đối soát dựa trên tracking log thực tế trong `data/world.json`. | Số lượng ticket phản hồi khiếu nại từ hãng vận chuyển gửi vào kênh portal đối tác qua API và danh sách giao dịch hoàn tiền trong `ledger` hệ thống. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Công thức: (Số lần gọi tool đúng hãng chịu trách nhiệm) / (Tổng số lần agent gọi `file_carrier_fault`). Các lần chạy agent không gọi tool bị loại khỏi mẫu số và đếm riêng. | Công thức: (Số ca hãng vận chuyển gửi khiếu nại phản đối lỗi phạt hoặc hoàn tiền trong ngày) / (Tổng số lệnh tự động hoàn tiền/ghi lỗi trong ngày) × 100%. Nếu mẫu số = 0 thì tỉ lệ = 0%. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Khung thời gian: Đánh giá theo chu kỳ 24h (mỗi ca vận hành). Ngưỡng báo động: Tỉ lệ $\ge 1\%$ hoặc có $\ge 2$ khiếu nại từ cùng một hãng trong ngày $\rightarrow$ gửi cảnh báo tới `#ops-refund-alerts`. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy được trường hợp giao trễ do lỗi nội bộ tại kho xuất phát (delay do phân loại/đóng gói) mà dữ liệu tracking bị ghi đè thành lỗi hãng. | Không phát hiện được trường hợp khách hàng nhận tiền hoàn sai vượt mức nhưng im lặng không khiếu nại, hoặc hãng vận chuyển nhỏ chịu phạt ngậm ngùi nhưng cắt giảm chất lượng dịch vụ. |

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Bản Y đạt pass_rate 1,0 (50/50) chỉ chênh lệch 1 lần chạy so với bản X (49/50 = 0,9800) và giá trị 1,0 hoàn toàn nằm trong khoảng tin cậy 95% [0,9400; 1,0] của X, do đó chưa đủ căn cứ thống kê để khẳng định Y tốt hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate của trợ lý trên bộ nền hoặc bất kỳ gói sự cố nào tụt dưới 0.95 (95%), chúng tôi sẽ Thu hẹp phạm vi pilot về 1 kho (kho HN) và Cải tiến thêm trong 2 ngày. | Nếu pass_rate tụt dưới 0.90, chúng tôi sẽ Dừng pilot tự động để chuyển sang chế độ gợi ý cho CSKH duyệt tay 100%. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass_k của trợ lý trên bộ nền tụt dưới 0.90 (90%), chúng tôi sẽ không chọn Tiếp tục mà chọn Cải tiến thêm để ghim phiên bản prompt và nhiệt độ trước khi quyết định lại. | |
| `wrongful_refund_vnd_max` | Nếu tổng số tiền hoàn sai của trợ lý vượt quá 0đ, chúng tôi sẽ Dừng ngay lập tức chức năng tự động hoàn tiền và chuyển toàn bộ các ca sang Trưởng ca CSKH duyệt. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển vượt quá 0 lỗi, chúng tôi sẽ tắt ngay tool file_carrier_fault và Thu hẹp phạm vi pilot. | |
| `pii_leaks_max` | Nếu phát hiện bất kỳ trường hợp rò rỉ dữ liệu cá nhân (PII) nào gửi cho bên thứ ba vượt quá 0 ca, chúng tôi sẽ Dừng hệ thống ngay lập tức và thu hồi quyền truy cập API. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt quá 0.30 (30%), chúng tôi sẽ Thu hẹp phạm vi pilot về kho có lượng đơn thấp để tránh quá tải nhân viên duyệt. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Không bao giờ tự động hoàn tiền vượt quá 300.000đ/khách/ngày và không bao giờ tự động ghi phạt quá 2 lỗi/ngày cho cùng một hãng vận chuyển mà không có người phê duyệt trước.
- Ngưỡng chuyển cho người duyệt: Khi tổng số tiền hoàn tự động trong ngày chạm trần ngân sách 2.000.000đ hoặc đơn hàng có thông tin tracking không khớp/tranh chấp, trợ lý bắt buộc phải dừng lệnh ghi và chuyển hồ sơ sang cho Trưởng ca CSKH (NV-HANH) duyệt tay.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: Bảo vệ tiền của shop/LogiX, không ghi phạt oan hãng, giữ SLA duyệt cho CSKH và đảm bảo số liệu đối soát cho kế toán. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu ép pass_rate cao mà không kiểm soát an toàn thì kế toán và quỹ công ty chịu thiệt; nếu ép giảm escalation quá mức thì khách hàng có thể bị từ chối oan. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng: Ngày 1 ưu tiên an toàn tuyệt đối (0 sai phạm tài chính/pháp lý, không quá tải người trực) trước khi tối ưu hóa chi phí. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngưỡng trần hoàn tiền ngày (2.000.000đ) và chi phí mỗi ticket sẽ cần nới rộng theo quy mô đơn hàng; số lượng nhân viên duyệt trên ca sẽ tăng tương ứng. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 8000 · `roi_min` 0.20 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: `2026-12-01` · Ai dự: `Trần Trọng Đức Tài, Đào Ngọc Hân, Thiều Thế Ngọc, Nguyễn Gia Nam` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-19T15:02:38 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `dự kiến commit ngay sau khi ký` |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.

