from src.DeTai import it_ca_nhat, kiem_tra_lich, ca_hop_le

def in_ket_qua(ten_test, A):
    print(f"\n--- {ten_test} ---")
    print(f"Ma trận xung đột A = {A}")
    try:
        so_ca, ca = it_ca_nhat(A)
        print(f"Số ca nhỏ nhất: {so_ca}")
        print(f"Mảng ca thi: {ca}")
        hop_le = kiem_tra_lich(A, ca)
        print(f"Kiểm tra lịch hợp lệ: {'ĐÚNG' if hop_le else 'SAI'}")
    except Exception as e:
        print(f"Lỗi khi chạy: {e}")

def main():
    print("MÔ PHỎNG XẾP LỊCH THI BẰNG TÔ MÀU ĐỒ THỊ")
    print("Sinh viên: Vũ Thành Luân - N24DCDT049\n")

    # [CÁC CA ĐÃ CÓ (7 ca đầu)]
    A_vd1 = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    in_ket_qua("A01: Ví dụ 1 (Đề bài): 4 môn tạo thành chu trình C4", A_vd1)

    A_vd2 = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    in_ket_qua("A02: Ví dụ 2 (Đề bài): 3 môn đôi một xung đột (K3)", A_vd2)

    A_test1 = [[0]]
    in_ket_qua("A03: Test 1: Một môn duy nhất", A_test1)

    A_test2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    in_ket_qua("A04: Test 2: Bốn môn không xung đột", A_test2)

    A_test3 = [[0, 1], [1, 0]]
    in_ket_qua("A05: Test 3: Hai môn xung đột nhau", A_test3)

    A_test4 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    in_ket_qua("A06: Test 4: Đường 3 môn (1-2-3)", A_test4)

    A_test5 = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
    in_ket_qua("A07: Test 5: Bốn môn đôi một xung đột (K4)", A_test5)

    # ==========================================
    # [BỔ SUNG 5 CA KIỂM TRA MỚI (A08 -> A12)]
    # ==========================================
    
    # A08: Kiểm tra biên - Đồ thị rỗng (Không có môn thi nào)
    A_test_rong = []
    in_ket_qua("A08: Biên - Đồ thị rỗng (0 môn thi)", A_test_rong)

    # A09: Kiểm tra biên - Đồ thị hình sao (Đỉnh trung tâm xung đột với n-1 đỉnh còn lại)
    # Ví dụ: Môn 0 xung đột với 1, 2, 3, 4. Các môn 1, 2, 3, 4 không xung đột với nhau.
    A_test_sao = [
        [0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]
    in_ket_qua("A09: Biên - Đồ thị hình sao 5 đỉnh", A_test_sao)

    # A10: Kiểm tra đồ thị phân đôi (Bipartite Graph) - 6 đỉnh
    # Có thể tô bằng 2 màu (2 ca thi). 
    A_test_bipartite = [
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0]
    ]
    in_ket_qua("A10: Đồ thị phân đôi K(3,3)", A_test_bipartite)
    
    # A11: Kiểm tra ngoại lệ hàm con - Đầu vào hàm kiem_tra_lich có mảng ca chứa giá trị 0
    # Expected: Hàm kiem_tra_lich trả về False
    print("\n--- A11: Kiểm tra ngoại lệ hàm con ---")
    A_loi = [[0, 1], [1, 0]]
    ca_loi = [0, 1]  # Môn đầu tiên chưa được gán ca thi (giá trị 0)
    ket_qua_loi = kiem_tra_lich(A_loi, ca_loi)
    print(f"Gọi kiem_tra_lich với mảng ca có chứa số 0 {ca_loi}. Hợp lệ: {ket_qua_loi}")

    # A12: Kiểm tra ngoại lệ hàm con - Đầu vào hàm ca_hop_le với ca thi đã bị trùng
    print("\n--- A12: Kiểm tra hàm con ca_hop_le ---")
    # Môn 1 đã xếp vào ca 1. Ta thử xếp môn 0 (xung đột môn 1) vào ca 1
    ket_qua_hop_le = ca_hop_le(i=0, c=1, A=[[0, 1], [1, 0]], ca=[0, 1])
    print(f"Thử xếp môn 0 vào ca 1 khi môn 1 (đã ở ca 1) xung đột với nó. Hợp lệ: {ket_qua_hop_le}")


    print("\n--- TÙY CHỌN NHẬP TỪ BÀN PHÍM ---")
    nhap = input("Bạn có muốn tự nhập ma trận không? (y/n): ")
    if nhap.lower() == 'y':
        try:
            n = int(input("Nhập số lượng môn thi (n <= 7): "))
            A_custom = [[0]*n for _ in range(n)]
            print("Nhập 1 nếu môn i và j xung đột, ngược lại nhập 0.")
            for i in range(n):
                for j in range(i + 1, n):
                    val = int(input(f"Môn {i} và môn {j} có xung đột không? (1/0): "))
                    A_custom[i][j] = val
                    A_custom[j][i] = val
            in_ket_qua("Kết quả ma trận tự nhập", A_custom)
        except ValueError:
            print("Lỗi nhập liệu! Vui lòng nhập số nguyên.")

if __name__ == "__main__":
    main()
