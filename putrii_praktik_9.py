# nama : p telasih putri
# kelas : xi tlk 2
# nomer absen : 25
# soal : Sebagai seorang pustakawan, Anda perlu menentukan jenis pinjaman buku berdasarkan durasi peminjaman.

durasi_peminjaman = int(input("masukkan durasi peminjaman buku dalam hari: "))

if durasi_peminjaman <= 7:
    jenis_peminjaman = "peminjaman pendek"
elif 7 < durasi_peminjaman <= 30:
    jenis_peminjaman = "peminjaman menengah"
else:
    jenis_peminjaman = "peminjaman panjang"

print(f"jenis peinjaman: {jenis_peminjaman}")
