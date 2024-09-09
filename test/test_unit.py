import unittest

from src.kalkulasi import hitung_gaji, tabungan




class TestGajiMingguan(unittest.TestCase):

    #jam kerja normal

    def test_normal(self):

        self.assertEqual(hitung_gaji(15000, 15000, 40, 5, 0), 675000)


    #lembur jam dan hari 

    def test_lembur(self):

        self.assertEqual(hitung_gaji(15000, 15000, 52, 6, 0), 960000)


    #izin pulang (35 jam per minggu)

    def test_izin(self):

        self.assertEqual(hitung_gaji(15000, 15000, 35, 5, 0), 600000)


    #unpaid cuti (4 hari kerja)

    def test_cuti(self):

        self.assertEqual(hitung_gaji(15000, 15000, 30, 4, 0), 510000)


    #error (0 hari kerja)

    def test_error(self):

        self.assertEqual(hitung_gaji(15000, 15000, 40, 0, 0), "Terjadi kesalahan silahkan input ulang")


class TestTabungan(unittest.TestCase):
    

    def test_bisa(self):

        self.assertEqual(tabungan(675000, 600000), f"Bisa Menabung, anda bisa menabung sebesar {675000-600000} Rupiah")


    def test_sama(self):

        self.assertEqual(tabungan(600000, 600000), "Cari Tambahan agar Bisa Menabung")


    def test_tidak(self):

        self.assertEqual(tabungan(510000, 600000), f"Tidak Bisa Menabung, anda butuh {600000-510000+1} Rupiah Lagi")


    def test_error(self):

        self.assertEqual(tabungan(510000, -600000), "Terjadi Kesalahan, Silahkan Input Ulang")


if __name__ == '__main__':

    unittest.main()