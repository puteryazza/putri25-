# nama : p telasih putri
# kelas : xi tlk 2
# nomer absen : 25
# soal : Sebagai seorang manajer proyek, Anda perlu menentukan apakah suatu proyek akan diluncurkan atau ditunda berdasarkan status persiapan.

status_persiapan = input("masukkan status persiapan proyek (siap/tunda): ")
if status_persiapan.lower() == "siap":
    print("proyek diluncurkan. ") 
elif status_persiapan.lower() == "tunda":
    print("proyek ditunda.")
else:
    print("status persiapan tidak valid. harap masukkan 'siap' atau 'tunda' .")
    