# nama : p telasih putri
# kelas : xi tkj 2
# Nnomer absen : 25
# soal : sebagai seorang manager proyek, anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.

estimasi_selesai = input ("masukkan estimasasi waktu selesai proyek (tahun-bulan-tanggal): ")
tanggal_target = input ("masukkan tanggal target selesai (tahun-bulan-tanggal): ")
if estimasi_selesai <= tanggal_target:
    print("tepat waktu")
else:
    print("terlambat")