# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `4anhchang`
- Lớp: `L3A` / `L3B`: `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`:
  `K5-L3B-DAY10-4anhchang-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Thiều Thế Ngọc | 2A202603788 | Kỹ sư cổng |             |
|   2 | Nguyễn Gia Nam | 2A202603761 | Kỹ sư cổng |             |
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

Sản phẩm và kinh doanh: Phiếu A, tiêu chí đã ký, bản đồ dữ liệu, cổng `business`, quyết định v1/v2 và phần `config/acceptance_criteria.json`.

### Đóng góp cụ thể

Chưa ghi ở phiên bản này; bổ sung khi hoàn thành công việc.

### Bằng chứng

Mã commit: … · Mã lần chạy: `runs/<mã>` · Dòng trong phiếu: A1–A5, B3, B7.4, B8, C5, C12

### Exit ticket

Một điều học được: … · Một điều còn chưa chắc: …

## TranTrongDucTai-2A202603732

### Phần việc phụ trách

Vận hành và pháp lý: HAZOP, checklist 9 nhóm, cổng `operations` và `legal`, runbook, giờ cao điểm, HAZOP của thẻ, gom bài nộp và `submission/submission.json`.

### Đóng góp cụ thể

Đã hoàn thành phân tích HAZOP vòng 1 cho tool `issue_refund` (Phiếu B mục B4); rà soát và điền Checklist 9 nhóm việc có PIC đích danh (mục B5); cấu hình mục `operations` và `legal` trong `config/operating_gates.json`; hoàn thiện Runbook phần 1–3 (mục B7.5) và quy trình xử lý Giờ cao điểm (mục B7.6).

### Bằng chứng

Mã commit: (commit cập nhật Khối 2A/2B) · Dòng trong phiếu: B4, B5, B7.5, B7.6 · File: `config/operating_gates.json`

### Exit ticket

Một điều học được: Khi đưa AI vào thực tế, các rào chắn vận hành và pháp lý (SLA duyệt ca, phân công PIC, hạn mức PII, công tắc dừng khẩn cấp) mang tính sống còn để kiểm soát rủi ro không thể đảo ngược. · Một điều còn chưa chắc: Liệu trong sự cố vòng 2, lượng ticket dồn dập có làm hàng chờ CSKH bị quá tải vượt quá công suất 6 ca/giờ của ca trực hay không.
