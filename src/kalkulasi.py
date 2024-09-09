
#fungsi menghitung gaji per minggu
def hitung_gaji(rate, uang_makan, total_jam_kerja, total_hari_kerja, bonus):
    
    #cek data abnormal
    if not isinstance(rate, int) or not isinstance(uang_makan, int) or not isinstance(total_jam_kerja, int) or not isinstance(total_hari_kerja, int) or not isinstance(bonus, int) :
        return "Terjadi Kesalahan, Silahkan Input Ulang"
        
    elif rate < 0 or uang_makan < 0 or total_jam_kerja < 0 or total_hari_kerja <= 0 or bonus < 0 :
        return "Terjadi kesalahan silahkan input ulang"
    
    #gaji lembur
    elif total_jam_kerja > 40 :
        
        #rate lembur berlaku untuk selisih dari jam kerja normal dengan jam kerja aktual
        lembur = int(1.5*rate*(total_jam_kerja-40))
        
        #gaji normal +  lembur
        gaji= (rate*40) + lembur
    
    #gaji normal
    else:
        gaji = rate * total_jam_kerja
    
    
    uang_makan *= total_hari_kerja
    
    gaji_final = gaji + uang_makan + bonus
    
    return gaji_final

#Fungsi menilai kemampuan menabung per minggu
def tabungan(gaji: int, pengeluaran: int):
    if not isinstance(gaji, int) or not isinstance(pengeluaran, int):
        return "Terjadi Kesalahan, Silahkan Input Ulang"
    elif gaji < 0 or pengeluaran < 0:
        return "Terjadi Kesalahan, Silahkan Input Ulang"
    elif gaji == pengeluaran:
        return "Cari Tambahan agar Bisa Menabung"
    elif gaji < pengeluaran:
        return f"Tidak Bisa Menabung, anda butuh {pengeluaran-gaji+1} Rupiah Lagi"
    elif gaji > pengeluaran:
        return f"Bisa Menabung, anda bisa menabung sebesar {gaji-pengeluaran} Rupiah"


