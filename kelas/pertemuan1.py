# print("ini mau saya push")

# #numerik

# angka1 = 5
# angka2 = 10
# hasil = angka1 + angka2
# print(hasil)

# #float
# a = 3.45
# b = 1.23
# hitung = a + b
# print(hitung)

# #string
# nama = "Larry"
# hobi = "ngoding"
# print(nama)
# print(hobi)

# print('''Halo saya Rendy
# Saya suka belajar coding
# Hari ini saya belajar bahasa pemrograman Python''')

# print("aku""rajin""praktikum")
# print("aku" + "rajin")

# teks = "Rahmat Flowchart"
# print(teks[3])
# print(teks[3:6])
# print(teks[7:])
# print(teks[:6])
# print(teks[1:4:2])
# print(teks[-1])

# biodata = ["Larry", 19, "2026", 82.49, True, ["APD", "26"]]
# print(biodata)

# mata_kuliah = ["APD","Logika Matematika","Kalkulus"]
# print(mata_kuliah[0])
# print(mata_kuliah[1])
# print(mata_kuliah[2])
# print(mata_kuliah[0:1])
# print(mata_kuliah[:2])
# print(mata_kuliah[1:])
# print(mata_kuliah[::2])
# print(mata_kuliah[:-1])

# buku = {
# 'judul' : 'Atomic Habits',
# 'penulis' : 'James Clear',
# 'halaman' : 320
# }
# ...
# # Mengakses Value dalam Dictionary
# print(buku['judul'])
# print(buku['penulis'])
# print(buku['halaman'])

# angka = int("42")
# print(angka)

# ubah = float("99.99")
# print(ubah)

# nama = input("Masukkan nama kamu: ")
# print (nama)

# gaji = int(input("Masukkan gaji kamu: "))
# print(gaji)

# print(2 < 4)
# print(5 > 5)
# print(2 < 4 and 5 > 10)

# zidan = {
#     'pagi' : "kalkulus",
#     'siang' : "APD",
#     'malam' : "bahasa inggris"
# }
# ...
# print(zidan['siang'])

import inquirer
from prettytable import PrettyTable
# Deklarasi struktur dictionary untuk menampung data mahasiswa
data_mahasiswa = {
    "nim": [],
    "nama": [],
    "kelas": []
}
def tambah_data():
    pertanyaan = [
    inquirer.Text("nim", message="Input NIM kamu"),
    inquirer.Text("nama", message="Input nama lengkapmu"),
    inquirer.List("kelas", message="Pilih kelas", choices=["A", "B", "C"]),
    ]
    # Hasil input disimpan ke variabel jawaban dalam bentuk dictionary:
    # {'nim': '...', 'nama': '...', 'kelas': '...'}
    jawaban = inquirer.prompt(pertanyaan)
    # Menambahkan masing-masing nilai ke dalam list pada dictionary
    data_mahasiswa
    data_mahasiswa["nim"].append(jawaban["nim"])
    data_mahasiswa["nama"].append(jawaban["nama"])
    data_mahasiswa["kelas"].append(jawaban["kelas"])
def tampil_data():
    tabel = PrettyTable()
    tabel.field_names = ["No", "NIM", "Nama", "Kelas"]
    for i in range(len(data_mahasiswa["nim"])):
        tabel.add_row([
        i + 1,
        data_mahasiswa["nim"][i],
        data_mahasiswa["nama"][i],
        data_mahasiswa["kelas"][i]
        ])
    print(tabel)
# Memanggil fungsi
tambah_data()
tampil_data()