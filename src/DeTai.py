# ==========================================
# Sinh viên: Vũ Thành Luân - N24DCDT049
# Đề tài: DT044 - Xếp ít ca thi nhất từ bảng xung đột
# ==========================================

"""
Bước 1: Giải thích mô hình hóa đồ thị
- Đỉnh (Vertex): Mỗi môn thi được coi là một đỉnh.
- Cạnh (Edge): Sự xung đột giữa hai môn thi.
- Màu (Color): Mỗi ca thi tương ứng với một màu.
=> Bài toán xếp ít ca thi nhất trở thành bài toán tô màu đồ thị.
"""

def ca_hop_le(i, c, A, ca):
    """Kiểm tra xem môn i có thể xếp vào ca c được không."""
    for j in range(len(A)):
        if A[i][j] == 1 and ca[j] == c:
            return False
    return True

def xep_voi_k_ca(A, k):
    """Thử xếp các môn với tối đa k ca bằng thuật toán quay lui."""
    n = len(A)
    ca = [0] * n
    
    def quay_lui(i):
        if i == n:
            return True
        for c in range(1, k + 1):
            if ca_hop_le(i, c, A, ca):
                ca[i] = c
                if quay_lui(i + 1):
                    return True
                ca[i] = 0 # Backtrack
        return False

    if quay_lui(0):
        return ca.copy()
    return None

def it_ca_nhat(A):
    """Thử k từ 1 đến n, dừng tại k đầu tiên có lịch hợp lệ."""
    n = len(A)
    for k in range(1, n + 1):
        ket_qua_ca = xep_voi_k_ca(A, k)
        if ket_qua_ca is not None:
            return k, ket_qua_ca
    return n, list(range(1, n + 1))

def kiem_tra_lich(A, ca):
    """Kiểm tra mọi cặp xung đột xem có bị trùng ca không."""
    n = len(A)
    k = max(ca) if ca else 0
    for c in ca:
        if c < 1 or c > k:
            return False
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] == 1 and ca[i] == ca[j]:
                return False
    return True
