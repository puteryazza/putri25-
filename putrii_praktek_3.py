# nama : p telasih putri
# kelas : xi tlk 2
# nomer absen : 25
# soal : Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya 

nama_file = "data.txt"
daftar_file_di_server = ["file1.txt,","file2.txt","data.txt","file3.txt"]

if nama_file in daftar_file_di_server:
    print("file sudah ada")
else:
    print("file belum ada")