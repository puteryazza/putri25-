# nama : p telasih putri
# kelas : xi tlk 2
# nomer absen : 25
# soal : Sebagai seorang pengembang perangkat lunak, Anda perlu membuat program sederhana yang menghitung bonus tahunan karyawan berdasarkan performa mereka.

nilai_perfom = int(input("masukkan nilai perfom karyawan (1-5): "))
gaji_tahunan = float(input("masukkan gaji tahunan karyawan: "))
bonus = (0.2 * gaji_tahunan) if nilai_perfom == 5 else (0.1 * gaji_tahunan) if nilai_perfom == 4 else (0.05 * gaji_tahunan) if nilai_perfom == 3 else (0.02 * gaji_tahunan) if nilai_perfom == 2 else 0
print(f"bonus tahunan karyawan: ${bonus:.2f}")
