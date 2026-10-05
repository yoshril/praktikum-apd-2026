username = "nazril"
password = "053"


while True:
    username_input = input("Masukkan username anda: ").lower()
    password_input = input("Masukkan password anda: ").lower()

    if username_input == "" or password_input == "":
        print("Username/Password tidak boleh kosong, coba lagi!\n")
    elif username_input == username and password_input == password:
        print("Login berhasil!\n")
        break
    elif username_input != username and password_input != password:
        print("Username dan Password salah, coba lagi!\n")
    elif username_input != username:
        print("Username salah, coba lagi!\n")
    else:
        print("Password salah, coba lagi!\n")

total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0

while True:

    while True:
        print("=========================")
        print("(1) Kalimantan")
        print("(2) Sumatera")
        print("=========================")
        pulau = input("Masukkan pulau: ")
        print("\n")

        if pulau == "":
            print("Input tidak boleh kosong!\n")
        elif pulau == "1" or pulau == "2":
            break
        else:
            print("Pilihan tidak tersedia!\n")

    
    if pulau == "1":
        while True:
            print("=========================")
            print("(1) Kalimantan-Gambut")
            print("(2) Kalimantan-Mineral")
            print("=========================")
            jenis = input("Masukkan jenis lahan: ")

            if jenis == "":
                print("Input tidak boleh kosong!\n")
            elif jenis == "1":
                pulau_kategori = "Kalimantan-Gambut"
                break
            elif jenis == "2":
                pulau_kategori = "Kalimantan-Mineral"
                break
            else:
                print("Pilihan tidak tersedia!\n")
        
    else:
        while True:
            print("=========================")
            print("(1) Sumatera-Gambut")
            print("(2) Sumatera-Mineral")
            print("=========================")
            jenis = input("Masukkan jenis: ")

            if jenis == "":
                print("Input tidak boleh kosong!\n")
            elif jenis == "1":
                pulau_kategori = "Sumatera-Gambut"
                break
            elif jenis == "2":
                pulau_kategori = "Sumatera-Mineral"
                break
            else:
                print("Pilihan tidak tersedia!\n")

    while True:
        hotspot_input = input("Masukkan jumlah titik api: ")

        if hotspot_input == "":
            print("Input tidak boleh kosong!\n")
        elif not hotspot_input.isdigit():
            print("Masukkan angka bulat yang valid!\n")
        else:
            hotspot = int(hotspot_input)
            break

    luas = hotspot * 5
    print(f"\n>> {pulau_kategori}: {hotspot} titik api = {luas} Hektare terbakar\n")

    if pulau_kategori == "Kalimantan-Gambut":
        total_kalimantan_gambut += luas
    elif pulau_kategori == "Kalimantan-Mineral":
        total_kalimantan_mineral += luas
    elif pulau_kategori == "Sumatera-Gambut":
        total_sumatera_gambut += luas
    else:
        total_sumatera_mineral += luas

    while True:
        lagi = input("Apakah anda masih mau input data titik api lagi? (Y/T): ").lower()
        if lagi == "y" or lagi == "t":
            break
        elif lagi == "":
            print("Input tidak boleh kosong!\n")
        else:
            print("Jawab dengan Y atau T saja!\n")

    if lagi == "t":
        break

total_semua = total_kalimantan_gambut + total_kalimantan_mineral + total_sumatera_gambut + total_sumatera_mineral

print("========================")
print("  Data Kebakaran Lahan  ")
print("========================")
print(f"Kalimantan-Gambut  : {total_kalimantan_gambut} Hektare")
print(f"Kalimantan-Mineral : {total_kalimantan_mineral} Hektare")
print(f"Sumatera-Gambut    : {total_sumatera_gambut} Hektare")
print(f"Sumatera-Mineral   : {total_sumatera_mineral} Hektare")
print(f"TOTAL KESELURUHAN  : {total_semua} Hektare")

    




        


