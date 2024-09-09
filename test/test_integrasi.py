import unittest
from unittest import TestCase
from unittest import mock
from src.kalkulasi import tabungan, hitung_gaji
from src.menu import menu


class TestungMenabung(TestCase):


    def test_bisa_menabung(self):

        self.assertEqual(tabungan(hitung_gaji(15000, 15000, 40, 5, 0), 600000), f"Bisa Menabung, anda bisa menabung sebesar {675000-600000} Rupiah")


    def test_cari_tambahan(self):

        self.assertEqual(tabungan(hitung_gaji(15000, 15000, 35, 5, 0), 600000), "Cari Tambahan agar Bisa Menabung")


    def test_tidak_menabung(self):

        self.assertEqual(tabungan(hitung_gaji(15000, 15000, 30, 4, 0), 600000), f"Tidak Bisa Menabung, anda butuh {600000-510000+1} Rupiah Lagi")


    def test_tabungan_error(self):

        self.assertEqual(tabungan(hitung_gaji(15000, 15000, 0, 0, 0), 600000), "Terjadi Kesalahan, Silahkan Input Ulang")



if __name__ == '__main__':
    unittest.main()