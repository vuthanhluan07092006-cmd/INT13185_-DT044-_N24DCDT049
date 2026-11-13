import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.DeTai import it_ca_nhat, kiem_tra_lich, ca_hop_le

class TestXepLichThi(unittest.TestCase):
    # --- CÁC CA ĐÃ CÓ ---
    def test_ca_hop_le_hop_le_va_khong(self):
        A = [[0, 1], [1, 0]]
        self.assertFalse(ca_hop_le(1, 1, A, [1, 0]))
        self.assertTrue(ca_hop_le(1, 2, A, [1, 0]))

    def test_it_ca_nhat_vi_du_1(self):
        A = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
        so_ca, ca = it_ca_nhat(A)
        self.assertEqual(so_ca, 2)
        self.assertTrue(kiem_tra_lich(A, ca))

    def test_it_ca_nhat_vi_du_2(self):
        A = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        so_ca, ca = it_ca_nhat(A)
        self.assertEqual(so_ca, 3)
        self.assertTrue(kiem_tra_lich(A, ca))

    def test_mot_mon(self):
        A = [[0]]
        so_ca, ca = it_ca_nhat(A)
        self.assertEqual(so_ca, 1)
        self.assertEqual(ca, [1])

    # --- 5 CA KIỂM TRA MỚI (A08 -> A12) ---
    def test_bien_do_thi_rong(self):
        # Đồ thị không có đỉnh nào
        A = []
        so_ca, ca = it_ca_nhat(A)
        self.assertEqual(so_ca, 0)
        self.assertEqual(ca, [])

    def test_bien_do_thi_hinh_sao(self):
        # Đỉnh 0 xung đột với 1, 2, 3, 4. Các đỉnh còn lại không xung đột.
        A = [
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]
        ]
        so_ca, ca = it_ca_nhat(A)
        self.assertEqual(so_ca, 2) # Chỉ cần 2 ca: Đỉnh 0 thi ca 1, còn lại thi ca 2
        self.assertTrue(kiem_tra_lich(A, ca))

    def test_do_thi_phan_doi(self):
        # K(3,3): 2 tập đỉnh (0,1,2) và (3,4,5).
        A = [
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0]
        ]
        so_ca, ca = it_ca_nhat(A)
        self.assertEqual(so_ca, 2) 
        self.assertTrue(kiem_tra_lich(A, ca))

    def test_kiem_tra_lich_loi_chua_gan_ca(self):
        # Môn 0 được gán ca 0 (không hợp lệ)
        A = [[0, 1], [1, 0]]
        ca = [0, 1] 
        self.assertFalse(kiem_tra_lich(A, ca))

    def test_kiem_tra_lich_loi_xung_dot(self):
        # Môn 0 và 1 xung đột nhưng cùng xếp vào ca 1
        A = [[0, 1], [1, 0]]
        ca = [1, 1] 
        self.assertFalse(kiem_tra_lich(A, ca))

if __name__ == '__main__':
    unittest.main()
