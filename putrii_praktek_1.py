# nama : p telasih putri
# kelas : xi tkj 2
# absen : 25
# soal : Di toko online, hitung diskon berdasarkan total belanjaan pelanggan.

if  total_belanjaan > 500000:
    diskon = total_belanjaan * 0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan * 0.05
else:
    diskon = 0

total_pembayaran = total_belanjaan - diskon
print(f"total pembayaran setelah diskon: (total_pembayaran)")
