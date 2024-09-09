# Tugas Pertama - Penjaminan Mutu Perangkat Lunak

## Permasalahan
Seorang karyawan bernama john travolta bergaji mingguan. Gaji normal seminggu (untuk 40 jam), standarnya (“rate”) adalah: rp. 15.000,- /jam. Sedangakan untuk lembur (artinya kerja diatas 40 jam/minggu) dibayar satu setengah kali dari gaji normal per jam nya (“rate”).

1) Bila Mr. John travolta pada minggu ini bekerja 52 jam, berapa gaji mr. John tersebut. Buat alogaritma + program menghitung gaji dengan nilai-nilai yang lain/variatif: (“bebas”).
2) Bila pemasukan lebih besar dari pengeluaran maka, akan ditulis (di print), ”bisa menabung”. Bila pemasukan sama dengan pengeluaran maka, akan ditulis (di print), ”tidak bisa menabung”. Bila pemasukan sama kurang dari pengeluaran maka, akan ditulis (di print), ”cari tambahan”.
pengeluaran mr. john selama seminggu ini adalah rp. 600.000. Apakah Mr. john bisa menabung atau tidak ??. bila bisa, berapa besar tabungannya untuk minggu ini. Buat alogaritma + program menghitung tabungan minggu ini dengan nilai-nilai yang lain/variatif (“bebas”).

## Penyelesaian
Untuk menambah variasi perhitungan gaji, kita dapat memperkenalkan beberapa variabel tambahan seperti uang makan dan bonus. Formula perhitungan gaji karyawan menjadi:

$$
f(x, y, z) = \min(40, x) \times 15.000 + \max(0, x - 40) \times 1.5 \times 15.000 + 15.000y + z
$$

Dimana:
- \(x\) adalah total jam kerja dalam seminggu,
- \(y\) adalah jumlah hari kerja di mana uang makan diberikan,
- \(z\) adalah bonus yang didapat.

Fungsi ini menghitung gaji karyawan berdasarkan jumlah jam kerja reguler (maksimal 40 jam), jam lembur (dihitung sebagai 1,5 kali gaji normal per jam), serta tambahan uang makan dan bonus.

Setelah menghitung gaji, langkah selanjutnya adalah mengkategorikan apakah karyawan bisa menabung atau tidak, berdasarkan perbandingan antara pemasukan dan pengeluaran. Jika pemasukan melebihi pengeluaran, maka karyawan dapat menabung, jika sama dengan pengeluaran tidak bisa menabung, dan jika pemasukan kurang dari pengeluaran, karyawan perlu mencari sumber pendapatan tambahan.

## Pengujian
Pengujian dilakukan menggunakan lima skenario kondisi kerja:
- Jam kerja normal (40 jam / 5 hari),
- Jam lembur (52 jam / 6 hari),
- Jam kerja dengan izin (35 jam / 5 hari),
- Jam kerja dengan cuti tidak dibayar (30 jam / 4 hari),
- Kondisi error (nilai input tidak valid).

Jenis pengujian yang akan dilakukan adalah:
- **Unit testing**: untuk memastikan bahwa setiap bagian dari perhitungan gaji dan tabungan berfungsi dengan benar secara independen.
- **Integration testing**: untuk memastikan bahwa fungsi-fungsi yang sudah diimplementasikan bekerja dengan baik ketika diintegrasikan dalam satu alur sistem. 
