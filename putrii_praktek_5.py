# nama : p telasih putri
# kelas : xi tlk 2
# nomer absen : 25
# soal : Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.

nilai_tugas = float(input("memasukkan nilai tugas (0-100): "))
nilai_ujian = float(input("memasukkan nilai ujian (0-100): "))

if nilai_tugas > 70 and nilai_ujian > 60:
    status = "lulus"
else:
    status = "gagal"

print(f"status kelulusan: {status}")            