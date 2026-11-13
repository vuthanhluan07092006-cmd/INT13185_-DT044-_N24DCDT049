DT044 — Xếp ít ca thi nhất từ bảng xung đột

Bản cài đặt hoàn chỉnh bằng ngôn ngữ Python. Thuật toán lõi sử dụng phương pháp quay lui (Backtracking) để giải quyết bài toán tô màu đồ thị (Graph Coloring).

Thông tin và căn cứ

Họ tên, MSSV, lớp: Vũ Thành Luân, N24DCDT049 (Giảng viên: Hồ Nhựt Minh).

Mã và tên đề tài đúng trong danh sách: DT044 - Xếp ít ca thi nhất từ bảng xung đột.

Giáo trình: Giao-trinh-Cau-truc-du-lieu-va-Giai-thuat-INT1306.pdf.

Chương, mục, bài tập, trang in và trang PDF đúng đề: Chương 3, Bài tập chương 3, câu 29: Bài toán xếp lịch thi; trang in 86; trang PDF 98.

URL GitHub thật: https://github.com/vuthanhluan07092006-cmd/INT13185_-DT044-_N24DCDT049.git; SHA chạy C ghi trong báo cáo và TXT nộp rời.

Permalink tệp thuật toán tại C: ghi trong báo cáo/TXT; phiên bản ngôn ngữ: Python 3.x (Dự án đã được chuyển đổi từ Julia sang Python).

Việc đã hoàn thành so với yêu cầu

Đã phân tích phiếu đề tài cá nhân và phần giáo trình liên quan.

Hợp đồng input/output đã thiết lập: Input là ma trận biểu diễn xung đột, xuất ra số ca thi nhỏ nhất và danh sách ca thi (Mỗi môn một ca trong miền 1..k; môn xung đột phải khác ca).

Đã cài đặt src/DeTai.py bằng thuật toán Quay lui. Các hàm đã có docstring giải thích chi tiết lý thuyết.

Triển khai code tại demo.py. Khai báo trực tiếp 7 ca mẫu và có chức năng nhập tùy chọn từ bàn phím.

Thiết lập test/runtests.py qua thư viện unittest. Chứa tổng cộng 12 ca kiểm thử độc lập (bao gồm các ca kỳ vọng, ca biên, rỗng, sao và các lỗi input hàm con).

Cấu trúc để xuất ảnh minh chứng lưu tại docs/anh_ket_qua/.

Hoàn thiện các cơ sở lý thuyết, độ phức tạp cho báo cáo.

Chạy sau khi đã cài đặt

Mở terminal tại thư mục repo:

python --version
python demo.py
python -m unittest test/runtests.py


Lệnh thực tế, cấu trúc input và output của bài cá nhân: Lệnh chạy: python demo.py. Input: Ma trận kề nhập thủ công (1 = có xung đột, 0 = không). Output: Mảng ánh xạ ca thi hợp lệ và Giá trị ca thi nhỏ nhất (k) đạt được.
Kết quả kiểm thử: 12 ca, 12 phép kiểm tra độc lập, ĐẠT 100% thực tế.

Công bố mã và kiểm tra bản clone

Các lệnh đã dùng để đưa phiên bản C (Commit C) lên GitHub:

git init
git add README.md .gitignore src demo.py test docs
git commit -m "Commit C: Hoan thanh ma nguon va test DT044"
git branch -M main
git remote add origin https://github.com/vuthanhluan07092006-cmd/INT13185_-DT044-_N24DCDT049.git
git push -u origin main
git rev-parse HEAD


Clone vào thư mục mới chưa tồn tại rồi chạy lại (Minh chứng A10):

git clone https://github.com/vuthanhluan07092006-cmd/INT13185_-DT044-_N24DCDT049.git kiem_tra_ban_nop_N24DCDT049
cd kiem_tra_ban_nop_N24DCDT049
git rev-parse HEAD
python --version
python demo.py
python -m unittest test/runtests.py


Báo cáo ghi URL repo và commit. Trên GitHub mở tệp thuật toán, nhấn y, sao chép permalink theo commit (dùng để lưu vào TXT).

Quy ước nộp Classroom

Báo cáo ghi SHA C của mã/test/input dùng tạo kết quả và permalink tại C. Sau khi thêm ảnh/báo cáo, chốt SHA S rồi ghi S trong ThongTinNop.txt nộp rời trên Classroom. Không đưa hash của chính commit vào tệp thuộc commit đó. Nộp đủ Word, PDF, ZIP mã và TXT đúng tên theo 00_HUONG_DAN_SINH_VIEN.html trong gói phát cho lớp.