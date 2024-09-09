from src.kalkulasi import *

def menu():
    while True:
        operasi = input("Kalkulator Gaji dan Tabungan, Ketik Angka untuk Melakukan Operasi (tanpa kurung):\n"
        "(1) Hitung Gaji Mingguan\n"
        "(2) Hitung Kemampuan Menabung\n"
        "(3) Hitung Kemampuan Menabung + Hitung Gaji Mingguan\n"
        "(4) Keluar\n"
        "\n BILQIS SEPTI YADAYANI (11220910000090)\n\n")



        match operasi:
            case "1":
                try:
                    print("\nMasukan dalam Satuan Rupiah\n")
                    rate = int(input("Gaji per Jam:"))
                    uang_makan = int(input("Nilai Uang Makan yang Diberikan Perusahaan (0 jika tidak ada):"))
                    jam_kerja = int(input("Total Jam Kerja Minggu ini:"))
                    hari_kerja = int(input("Total Hari Kerja Minggu ini:"))
                    bonus = int(input("Bonus minggu ini (0 apabila tidak ada)"))
                    
                    print(f"\nGaji anda bulan ini: {hitung_gaji(rate, uang_makan, jam_kerja, hari_kerja, bonus)}\n")
                    
                except:
                    print("\nMasukan dalam bentuk angka\n")

            case "2":
                try:
                    print("\nMasukan dalam Satuan Rupiah\n")
                    gaji = int(input("Input Pemasukan Minggu ini:"))
                    pengeluaran = int(input("Input Pengeluaran Mingguan:"))

                    print(f"\n{tabungan(gaji, pengeluaran)}\n")
                except:
                    print("\nMasukan dalam bentuk angka\n")

            case "3": 
                try:
                    print("\nMasukan dalam Satuan Rupiah\n")
                    rate = int(input("Gaji per Jam:"))
                    uang_makan = int(input("Nilai Uang Makan yang Diberikan Perusahaan (0 jika tidak ada):"))
                    jam_kerja = int(input("Total Jam Kerja Minggu ini:"))
                    hari_kerja = int(input("Total Hari Kerja Minggu ini:"))
                    bonus = int(input("Bonus minggu ini (0 apabila tidak ada)"))
                    pengeluaran = int(input("Input Pengeluaran Mingguan:"))

                    income = int(hitung_gaji(rate, uang_makan, jam_kerja, hari_kerja, bonus))

                    print(f"\nGaji anda bulan ini:{income}\n")
                    print(f"\n{tabungan(income, pengeluaran)}\n")
                except:
                    print("\nMasukan dalam bentuk angka\n")

            case "4":
                print("\nTerimakasih, Sampai Bertemu Kembali\n")
                break

            case _:
                print("Input salah, Silakan ulangi\n")

