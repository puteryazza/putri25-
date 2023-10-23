# nama : p telasih putri
# kelas : xi tlk 2
# nomer absen : 25
# soal : Sebagai seorang analis data, Anda harus mengkategorikan produk berdasarkan penjualan bulanan.

data_penjualan = {
    "produk": 1200,
    "produk": 800,
    "produk": 450,
}

def tentukan_kategori(penjualan):
    if penjualan > 1000:
        return "produk terlaris"
    elif 500 <= penjualan <= 1000:
        return "produk populer"
    else:
        return "prduk biasa"
    
    for produk, penjualan in data_penjualan.items():
        kategori = tentukan_kategori(penjualan)
        print(f"produk{produk}adalah {kategori}.")