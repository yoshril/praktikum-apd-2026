makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000 
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000

harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]

total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6 + 5000

konversi_euro = total_bayar / 20359

rata_rata = total_bayar / len(harga_makanan)

nim = 53

bolean = nim < rata_rata

print("Makanan 1 : Rp." + str(makanan_1))
print("Makanan 2 : Rp." + str(makanan_2))
print("Makanan 3 : Rp." + str(makanan_3))
print("Makanan 4 : Rp." + str(makanan_4))
print("Makanan 5 : Rp." + str(makanan_5))
print("Makanan 6 : Rp." + str(makanan_6))
print("Total Bayar : Rp." + str(total_bayar))
print("NIM : " + str(nim))
print("Bolean : " + str(bolean))
print("Total Bayar Dalam Euro : €" + str(konversi_euro))
print("Isi Makanan 3 - 5 : " + str(harga_makanan[-4:-1]))

