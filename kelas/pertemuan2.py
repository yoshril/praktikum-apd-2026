# angka = 6
# if angka < 10:
#     print("Angka kurang dari 10")

# umur = int(input("Masukkan umur: ")) # Input umur
# # Misalkan, umur = 17
# if umur >= 17:
#     print("Kamu sudah bisa membuat KTP") # Blok if dijalankan karena
# else:
#     print("Kamu belum bisa membuat KTP") # Blok else tidak dijalankan

# kendaraan = input("Masukkan jenis kendaraan anda: ")
# if kendaraan == "mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000
# # Menampilkan tarif parkir yang harus dibayar
# print("Tarif parkir yang harus dibayar:", tarif_parkir)

# nilai = int(input("Masukkan nilai anda : "))
# if nilai > 90:
#     print("A")
# elif nilai > 80:
#     print("B")
# elif nilai > 70:
#     print("C")
# else:
#     print("D")



# umur = 20
# status = "Dewasa" if umur >= 18 else "Belum Dewasa" 
# print(status)

# usia = int(input("Masukkan Usia : "))
# if usia >= 16:
#     print("Pengunjung Boleh Masuk")
# else:
#     print("Pengunjung Dilarang Masuk")

# tampilkan = "Pengunjung Boleh Masuk" if usia >= 16 else "Pengunjung Tidak Boleh Masuk"
# print(tampilkan)

total_pembelian = int(input("Masukkan Total Pembelian : Rp."))
if total_pembelian > 200000:
    harga_akhir = total_pembelian * 0.70
elif total_pembelian > 100000:
    harga_akhir = total_pembelian * 0.90
else:
    harga_akhir = total_pembelian

print("Harga Akhir : " + str(harga_akhir))