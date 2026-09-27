nama_benar = "nazril nur ilham"
nim_benar = 53
biaya_langganan = 1500000

print("=============================")
print("  SELAMAT DATANG DI ANGKASA  ")
print("=============================")
nama = input("= Masukkan  nama : ").lower()
nim = int(input("= Masukkan 2 digit NIM terakhir : "))

if nama == nama_benar and nim == nim_benar:
    print("=============================")
    print(" Pilih Paket (Gunakan Angka) ")
    print("=============================")
    print("1. Paket Orbit")
    print("2. Paket Nebula")
    print("3. Paket Galaxy")
    print("4. Paket Supernova")
    print("=============================")
    paket = int(input("Pilih paket : "))

    if paket == 1:
        biaya_administrasi = 0.01
        total_bayar = round(biaya_langganan + (biaya_langganan * biaya_administrasi))

        print("=============================")
        print("        -Paket Orbit-        ")
        print("=============================")
        print("Paket Orbit sudah aktif!")
        print(f"Total Bayar : Rp.{total_bayar}")
        print("Fitur : Akses dasar ke lagu-lagu populer")
    elif paket == 2:
        biaya_administrasi = 0.03
        total_bayar = round(biaya_langganan + (biaya_langganan * biaya_administrasi))

        print("=============================")
        print("        -Paket Nebula-       ")
        print("=============================")
        print("Paket Nebula sudah aktif!")
        print(f"Total Bayar : Rp.{total_bayar}")
        print("Fitur : Akses lagu premium dan playlist kostum")
    elif paket == 3:
        biaya_administrasi = 0.05
        total_bayar = round(biaya_langganan + (biaya_langganan * biaya_administrasi))

        print("=============================")
        print("        -Paket Galaxy-       ")
        print("=============================")
        print("Paket Galaxy sudah aktif!")
        print(f"Total Bayar : Rp.{total_bayar}")
        print("Fitur : Akses lagu premium, playlist kustom, dan mode offline")
    elif paket == 4:
        biaya_administrasi = 0.07
        total_bayar = round(biaya_langganan + (biaya_langganan * biaya_administrasi))

        print("=============================")
        print("      -Paket Supernova-      ")
        print("=============================")
        print("Paket Supernova sudah aktif!")
        print(f"Total Bayar : Rp.{total_bayar}")
        print("Fitur : Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")
    else:
        print("Paket tidak tersedia!")
        
else:
    print("Nama atau NIM salah!")
    print("Login gagal")
    