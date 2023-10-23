# nama : p telasih putri
# kelas : xi tlk 2
# nomer absen : 25
# soal : Pekerjaan: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).

total_belanjaan = float(input("masukkan total belanjaan: "))
status_anggota = input("masukkan status anggota(biasa atau premium): ")

diskon = 0

if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15
    else:
        diskon = 0.10
elif status_anggota == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07

total_setelah_diskon = total_belanjaan - (total_belanjaan * diskon)

print("total belanja setelah diskon: Rp", total_setelah_diskon)
