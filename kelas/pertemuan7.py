# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas

# #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang())

# hasil = luas_persegi_panjang()
# print("Luas persegi panjang:", hasil)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# #Kita panggil fungsinya lalu argumen kita adalah angka 7
# sisi = int(input("Masukkan sisi persegi: "))
# hasil = luas_persegi(sisi)
# print("Luas persegi: ", luas_persegi(7))
# print("Luas persegi: ", hasil)

# #Tanpa parameter
# def pengumuman():
#     print("Hari ini Pengujian Proyek Akhir")
# #Pemanggilan Prosedur
# for i in range(3):
#     pengumuman()

# def pengumuman(nama):
#     print(f"Selamat datang, {nama}!")

# nama = input("Masukkan nama: ")
# pengumuman(nama)

# def faktorial(n):
#     #Base Case: Kondisi fungsi berhenti
#     if n == 0 or n == 1:
#         return 1
#     #Rekursive Case: Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# #Memanggil fungsi
# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4! {hasil_faktorial}")

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as e:
    print(e)
else:
    print(usn)