import os

konsol = [
    ["C001", "PS5", "PS5-01", 150000, "Tersedia"],
    ["C002", "PS5", "PS5-02", 150000, "Tidak Tersedia"],
    ["C003", "PS4", "PS4-01", 80000, "Tidak Tersedia"],
    ["C004", "PS4", "PS4-02", 80000, "Tersedia"],
    ["C005", "PS3", "PS3-01", 40000, "Tidak Tersedia"],
    ["C006", "PS3", "PS3-02", 40000, "Tidak Tersedia"],
    ["C007", "Nintendo Switch", "NS-01", 100000, "Tersedia"],
    ["C008", "Nintendo Switch", "NS-02", 100000, "Tersedia"],
    ["C009", "Xbox", "X-01", 100000, "Tidak Tersedia"],
    ["C010", "Xbox", "X-02", 100000, "Tersedia"]
]

pelanggan = [
    ["P001", "Nazril", "rilease", "082254457382"],
    ["P002", "Fadil", "anak", "081376529601"],
    ["P003", "Ilham", "ilham123", "081256238729"],
    ["P004", "Klein", "lotm", "082249381742"],
    ["P005", "Rex", "pluto", "082144209194"],
    ["P006", "Zenn", "upr123", "082245538389"]
]

penyewaan = [
    ["S001", "P002", "C002", "1 Hari", 150000, "Berlangsung"],
    ["S002", "P001", "C003", "3 Hari", 240000, "Berlangsung"],
    ["S003", "P003", "C005", "1 Hari", 40000, "Berlangsung"],
    ["S004", "P004", "C006", "2 Hari", 80000, "Selesai"],
    ["S005", "P005", "C009", "1 Hari", 100000, "Selesai"]
]

counter_konsol = 0
for k in konsol:
    if int(k[0][1:]) > counter_konsol:
        counter_konsol = int(k[0][1:])

counter_pelanggan = 0
for p in pelanggan:
    if int(p[0][1:]) > counter_pelanggan:
        counter_pelanggan = int(p[0][1:])

counter_sewa = 0
for s in penyewaan:
    if int(s[0][1:]) > counter_sewa:
        counter_sewa = int(s[0][1:])     

admin_username = "admin"
admin_password = "admin123"

halaman = "awal"

while True:

    if halaman == "awal":
        print("============================================================")
        print("                   RENTAL PLAYSTATION")
        print("============================================================")
        print("(1) Login")
        print("(2) Register")
        print("(0) Keluar")
        pilih = input("Pilih Menu: ").strip()

        if pilih == "1":
            print("--- LOGIN ---")
            username_input = input("Masukkan username: ").strip()
            password_input = input("Masukkan password: ").strip()

            if username_input == admin_username and password_input == admin_password:
                os.system("cls")
                print("Anda berhasil login sebagai Admin!")
                halaman = "admin"

            elif username_input == "" or password_input == "":
                os.system("cls")
                print("Username atau Password harus diisi!")

            else:
                akun_ditemukan = False
                for p in pelanggan:
                    if p[1].lower() == username_input.lower() and p[2].lower() == password_input.lower():
                        akun_ditemukan = True
                        user = p

                if akun_ditemukan:
                    os.system("cls")
                    print(f"Login berhasil, Selamat datang {user[1]}!")
                    halaman = "pelanggan"

                else:
                    os.system("cls")
                    print("Username atau Password salah!")
                    

        elif pilih == "2":
            print("--- REGISTER ---")
            nama = input("Username (Tanpa spasi): ").strip()
            pw = input("Password (Tanpa spasi): ").strip()
            no_hp = input("Masukkan No HP (12 Digit): ").strip()

            nama_dipakai = False
            for p in pelanggan:
                if p[1].lower() == nama.lower():
                    nama_dipakai = True

            if nama == "" or pw == "" or no_hp == "":
                os.system("cls")
                print("Semua data harus diisi!")

            elif not nama.isalpha():
                os.system("cls")
                print("Nama hanya boleh huruf dan tanpa spasi!")

            elif nama.lower() == admin_username or nama_dipakai:
                os.system("cls")
                print("Nama sudah dipakai!")

            elif " " in pw:
                os.system("cls")
                print("Password tidak boleh spasi!")

            elif not (no_hp.isascii() and no_hp.isdigit()) or len(no_hp) != 12:
                os.system("cls")
                print("No HP hanya boleh angka 12 digit!")

            else:
                os.system("cls")
                counter_pelanggan += 1
                id_baru = f"P{counter_pelanggan:03d}"
                pelanggan.append([id_baru, nama, pw, no_hp])
                print(f"Registrasi berhasil! ID kamu: {id_baru}")
                print(f"Silakan login dengan username '{nama}'")

        elif pilih == "0":
            os.system("cls")
            print("Anda keluar dari program...")
            break

        else:
            os.system("cls")
            print("Pilihan tidak valid!")

    elif halaman == "admin":
        print("============================================================")
        print("                       MENU ADMIN")
        print("============================================================")
        print("(1) Kelola Konsol")
        print("(2) Kelola Pelanggan")
        print("(3) Kelola Penyewaan")
        print("(0) Logout")
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            os.system("cls")
            halaman = "admin_konsol"
            
        elif pilih == "2":
            os.system("cls")
            halaman = "admin_pelanggan"

        elif pilih == "3":
            os.system("cls")
            halaman = "admin_penyewaan"

        elif pilih == "0":
            os.system("cls")
            print("Logout berhasil")
            halaman = "awal"

        else:
            os.system("cls")
            print("Pilihan tidak ada!")

    elif halaman == "admin_konsol":
        print("============================================================")
        print("                  ADMIN > KELOLA KONSOL")
        print("1. Lihat  2. Tambah  3. Ubah  4. Hapus  0. Kembali")
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            os.system("cls")
            print("============================================================")
            print(f"{'ID':<6}{'Jenis':<18}{'Unit':<9}{'Harga/Hari':<12}{'Status'}")
            print("------------------------------------------------------------")

            if len(konsol) == 0:
                print("Belum ada data konsol")

            for k in konsol:
                print(f"{k[0]:<6}{k[1]:<18}{k[2]:<9}{k[3]:<12}{k[4]}")

            print("============================================================")

        elif pilih == "2":
            os.system("cls")
            print("--- TAMBAH UNIT ---")
            jenis = input("Jenis konsol (Contoh: PS5): ").strip()
            unit = input("Kode unit (Contoh: PS-03): ").strip().upper()
            harga = input("Harga sewa per hari: ").strip()

            unit_dipakai = False
            for k in konsol:
                if k[2].upper() == unit:
                    unit_dipakai = True

            if jenis == "" or unit == "" or harga == "":
                os.system("cls")
                print("Semua data harus diisi!")

            elif unit_dipakai:
                os.system("cls")                
                print("Kode unit sudah dipakai konsol lain!")

            elif not harga.isdecimal() or int(harga) < 1000:
                os.system("cls")                
                print("Harga harus berupa angka, minimal 1000!")

            else:
                os.system("cls")
                counter_konsol += 1
                id_baru = f"C{counter_konsol:03d}"
                konsol.append([id_baru, jenis, unit, int(harga), "Tersedia"])
                print(f"Konsol berhasil ditambahkan dengan ID {id_baru}")

        elif pilih == "3":
            os.system("cls")
            print("--- UBAH UNIT ---")
            id_input = input("ID konsol yang diubah: ").strip().upper()

            data = None
            for k in konsol:
                if k[0] == id_input:
                    data = k

            if data is None:
                os.system("cls")
                print("ID konsol tidak ditemukan!")

            else:
                os.system("cls")
                print("--- DETAIL KONSOL ---")
                print(f"ID Konsol   : {data[0]}")
                print(f"Jenis       : {data[1]}")
                print(f"Kode Unit   : {data[2]}")
                print(f"Harga/Hari  : Rp.{data[3]}")
                print(f"Status      : {data[4]}")

                sedang_disewa = False
                for s in penyewaan:
                    if s[2] == data[0] and s[5] == "Berlangsung":
                        sedang_disewa = True

                print("1. Ubah harga")
                print("2. Ubah status")
                pilih_ubah = input("Pilih: ").strip()

                if pilih_ubah == "1":
                    print("--- UBAH HARGA ---")
                    harga_baru = input("Harga baru per hari: ").strip()

                    if not harga_baru.isdecimal() or int(harga_baru) < 1000:
                        os.system("cls")
                        print("Harga harus berupa angka, minimal 1000!")

                    else:
                        data[3] = int(harga_baru)
                        os.system("cls")
                        print("Harga berhasil diubah")

                elif pilih_ubah == "2":
                    if sedang_disewa:
                        os.system("cls")
                        print("Status tidak bisa diubah karena konsol sedang disewa!")

                    else:
                        os.system("cls")
                        print("--- UBAH STATUS ---")
                        print("1. Tersedia")
                        print("2. Tidak Tersedia")
                        pilih_status = input("Pilih status baru: ").strip()

                        if pilih_status == "1":
                            data[4] = "Tersedia"
                            os.system("cls")
                            print("Status diubah menjadi Tersedia")

                        elif pilih_status == "2":
                            data[4] = "Tidak Tersedia"
                            os.system("cls")
                            print("Status diubah menjadi Tidak Tersedia")

                        else:
                            os.system("cls")
                            print("Pilihan tidak valid!")

                else:
                    os.system("cls")
                    print("Pilihan tidak valid!")

        elif pilih == "4":
            os.system("cls")
            print("--- HAPUS KONSOL ---")
            id_input = input("ID konsol yang ingin dihapus: ").strip().upper()

            data = None
            for k in konsol:
                if k[0] == id_input:
                    data = k

            if data is None:
                os.system("cls")
                print("ID konsol tidak ditemukan!")

            else:
                sedang_disewa = False
                for s in penyewaan:
                    if s[2] == data[0] and s[5] == "Berlangsung":
                        sedang_disewa = True

                if sedang_disewa:
                    os.system("cls")
                    print("Konsol tidak bisa dihapus karena sedang disewa!")

                else:
                    os.system("cls")
                    print("--- DETAIL KONSOL ---")
                    print(f"ID Konsol   : {data[0]}")
                    print(f"Jenis       : {data[1]}")
                    print(f"Kode Unit   : {data[2]}")
                    print(f"Harga/Hari  : Rp.{data[3]}")
                    print(f"Status      : {data[4]}")                    
                    yakin = input(f"Yakin hapus {data[1]} ({data[2]})? (y/n): ").strip().lower()

                    if yakin == "y":
                        konsol.remove(data)
                        os.system("cls")
                        print(f"Konsol {data[1]} : {data[2]} berhasil dihapus")

                    elif yakin == "n":
                        os.system("cls")
                        print("Penghapusan dibatalkan")

                    else:
                        os.system("cls")
                        print("Pilihan tidak valid!")

        elif pilih == "0":
            halaman = "admin"
            os.system("cls")

        else:
            os.system("cls")
            print("Pilihan tidak valid!")

    elif halaman == "admin_pelanggan":
            print("============================================================")
            print("                ADMIN > KELOLA PELANGGAN")
            print("1. Lihat  2. Hapus  0. Kembali")
            pilih = input("Pilih menu: ").strip()
    
            if pilih == "1":
                os.system("cls")
                print("============================================================")
                print(f"{'ID':<8}{'Nama':<15}{'Password':<20}{'No. Telepon':<15}")
                print("------------------------------------------------------------")

                if len(pelanggan) == 0:
                    print("Belum ada data pelanggan.")

                for p in pelanggan:
                    print(f"{p[0]:<8}{p[1]:<15}{p[2]:<20}{p[3]:<15}")

                print("============================================================")
    
            elif pilih == "2":
                os.system("cls")
                print("--- HAPUS PELANGGAN ---")
                id_input = input("ID pelanggan yang dihapus: ").strip().upper()
    
                data = None
                for p in pelanggan:
                    if p[0] == id_input:
                        data = p
    
                if data is None:
                    os.system("cls")
                    print("ID pelanggan tidak ditemukan!")

                else:
                    punya_sewa = False
                    for s in penyewaan:
                        if s[1] == data[0] and s[5] == "Berlangsung":
                            punya_sewa = True
    
                    if punya_sewa:
                        os.system("cls")
                        print("Pelanggan tidak bisa dihapus, masih ada sewa yang berlangsung!")

                    else:
                        os.system("cls")
                        print("--- DETAIL PELANGGAN ---")
                        print(f"ID Pelanggan : {data[0]}")
                        print(f"Nama         : {data[1]}")
                        print(f"No HP        : {data[3]}")                        
                        yakin = input(f"Yakin hapus pelanggan {data[1]}? (y/n): ").strip().lower()

                        if yakin == "y":
                            pelanggan.remove(data)
                            os.system("cls")
                            print(f"Pelanggan {data[1]} berhasil dihapus")

                        elif yakin == "n":
                            os.system("cls")
                            print("Penghapusan dibatalkan")

                        else:
                            os.system("cls")
                            print("Pilihan tidak valid!")
    
            elif pilih == "0":
                halaman = "admin"
                os.system("cls")

            else:
                os.system("cls")
                print("Pilihan tidak valid!")

    elif halaman == "admin_penyewaan":
            print("============================================================")
            print("                 ADMIN > KELOLA PENYEWAAN")
            print("1. Lihat  2. Selesaikan sewa  0. Kembali")
            pilih = input("Pilih menu: ").strip()
    
            if pilih == "1":
                os.system("cls")
                print("===========================================================================")
                print(f"{'ID Sewa':<10}{'ID Pelanggan':<15}{'ID Konsol':<12}{'Durasi':<12}{'Total':<15}{'Status':<12}")
                print("---------------------------------------------------------------------------")

                if len(penyewaan) == 0:
                    print("Belum ada data penyewaan")

                for s in penyewaan:
                    print(f"{s[0]:<10}{s[1]:<15}{s[2]:<12}{s[3]:<12}{s[4]:<15}{s[5]:<12}")

                print("===========================================================================")
    
            elif pilih == "2":
                os.system("cls")
                print("--- SELESAIKAN SEWA ---")
                id_input = input("ID sewa yang diselesaikan: ").strip().upper()
    
                data = None
                for s in penyewaan:
                    if s[0] == id_input and s[5] == "Berlangsung":
                        data = s
    
                if data is None:
                    os.system("cls")
                    print("ID sewa tidak ditemukan atau sudah selesai!")

                else:
                    os.system("cls")
                    data[5] = "Selesai"
                    for k in konsol:
                        if k[0] == data[2]:
                            k[4] = "Tersedia"
                            nama_konsol = f"{k[0]} | {k[1]} : {k[2]}"
                    print(f"Penyewaan selesai, konsol {nama_konsol} kembali tersedia")
    
            elif pilih == "0":
                halaman = "admin"
                os.system("cls")

            else:
                os.system("cls")
                print("Pilihan tidak valid!")

    elif halaman == "pelanggan":
            print("============================================================")
            print(f"                MENU PELANGGAN - {user[1]}")
            print("============================================================")
            print("1. Lihat konsol tersedia")
            print("2. Sewa konsol")
            print("3. Kembalikan konsol")
            print("4. Riwayat sewa saya")
            print("0. Logout")
            pilih = input("Pilih menu: ").strip()
    
            if pilih == "1":
                os.system("cls")
                print("============================================================")
                print(f"{'ID':<6}{'Jenis':<18}{'Unit':<9}{'Harga/Hari':<12}{'Status'}")
                print("------------------------------------------------------------")

                ada = False
                for k in konsol:
                    if k[4] == "Tersedia":
                        ada = True
                        print(f"{k[0]:<6}{k[1]:<18}{k[2]:<9}{k[3]:<12}{k[4]}")

                if not ada:
                    print("Tidak ada konsol yang tersedia saat ini")

                print("============================================================")
    
            elif pilih == "2":
                os.system("cls")
                print("============================================================")
                print(f"{'ID':<6}{'Jenis':<18}{'Unit':<9}{'Harga/Hari':<12}{'Status'}")
                print("------------------------------------------------------------")

                ada = False
                for k in konsol:
                    if k[4] == "Tersedia":
                        ada = True
                        print(f"{k[0]:<6}{k[1]:<18}{k[2]:<9}{k[3]:<12}{k[4]}")

                print("============================================================")
    
                if not ada:
                    print("Maaf, tidak ada konsol yang tersedia saat ini")

                else:
                    id_input = input("ID konsol yang ingin disewa: ").strip().upper()
    
                    data = None
                    for k in konsol:
                        if k[0] == id_input and k[4] == "Tersedia":
                            data = k
    
                    if data is None:
                        os.system("cls")
                        print("ID konsol tidak ditemukan atau sedang tidak tersedia!")

                    else:
                        hari = input("Lama sewa (1-30 hari): ").strip()
                        if not hari.isdecimal() or int(hari) < 1 or int(hari) > 30:
                            print("Lama sewa harus berupa angka 1 sampai 30!")

                        else:
                            hari = int(hari)
                            total = data[3] * hari
                            print(f"{data[1]} ({data[2]}) selama {hari} hari = Rp{total}")
                            yakin = input("Konfirmasi sewa? (y/n): ").strip().lower()
    
                            if yakin == "y":
                                os.system("cls")
                                counter_sewa += 1
                                id_sewa = f"S{counter_sewa:03d}" 
                                penyewaan.append([id_sewa, user[0], data[0], f"{hari} Hari", total, "Berlangsung"])
                                data[4] = "Tidak Tersedia"
                                print(f"Penyewaan berhasil! ID sewa kamu: {id_sewa}")

                            elif yakin == "n":
                                os.system("cls")
                                print("Penyewaan dibatalkan")

                            else:
                                os.system("cls")
                                print("Pilihan tidak valid!")
    
            elif pilih == "3":
                os.system("cls")
                print("=================================================================")
                print(f"{'ID Sewa':<12}{'ID Konsol':<12}{'Durasi':<12}{'Total':<15}{'Status':<14}")
                print("-----------------------------------------------------------------")

                ada = False
                for s in penyewaan:
                    if s[1] == user[0] and s[5] == "Berlangsung":
                        ada = True
                        print(f"{s[0]:<12}{s[2]:<12}{s[3]:<12}{s[4]:<15}{s[5]:<14}")

                print("=================================================================")
    
                if not ada:
                    os.system("cls")
                    print("Kamu tidak punya sewa yang sedang berlangsung")

                else:
                    id_input = input("ID sewa yang ingin dikembalikan: ").strip().upper()
    
                    data = None
                    for s in penyewaan:
                        if s[0] == id_input and s[1] == user[0] and s[5] == "Berlangsung":
                            data = s
    
                    if data is None:
                        os.system("cls")
                        print("ID sewa tidak ditemukan!")

                    else:
                        os.system("cls")
                        data[5] = "Selesai"
                        for k in konsol:
                            if k[0] == data[2]:
                                k[4] = "Tersedia"
                                nama_konsol = f"{k[0]} | {k[1]} : {k[2]}"
                        print(f"Konsol {nama_konsol} berhasil dikembalikan, Terima kasih!")
    
            elif pilih == "4":
                os.system("cls")
                print("=================================================================")
                print(f"{'ID Sewa':<12}{'ID Konsol':<12}{'Durasi':<12}{'Total':<15}{'Status':<14}")
                print("-----------------------------------------------------------------")

                ada = False
                for s in penyewaan:
                    if s[1] == user[0]:
                        ada = True
                        print(f"{s[0]:<12}{s[2]:<12}{s[3]:<12}{s[4]:<15}{s[5]:<14}")

                if not ada:
                    print("Kamu belum pernah menyewa konsol")

                print("=================================================================")
    
            elif pilih == "0":
                os.system("cls")
                print(f"Logout berhasil. Sampai jumpa, {user[1]}!")
                halaman = "awal"
                
            else:
                os.system("cls")
                print("Pilihan tidak valid!")
