import os

konsol = {
    "C001": {"jenis": "PS5", "unit": "PS5-01", "harga": 150000, "status": "Tersedia"},
    "C002": {"jenis": "PS5", "unit": "PS5-02", "harga": 150000, "status": "Tidak Tersedia"},
    "C003": {"jenis": "PS4", "unit": "PS4-01", "harga": 80000, "status": "Tidak Tersedia"},
    "C004": {"jenis": "PS4", "unit": "PS4-02", "harga": 80000, "status": "Tersedia"},
    "C005": {"jenis": "PS3", "unit": "PS3-01", "harga": 40000, "status": "Tidak Tersedia"},
    "C006": {"jenis": "PS3", "unit": "PS3-02", "harga": 40000, "status": "Tidak Tersedia"},
    "C007": {"jenis": "Nintendo Switch", "unit": "NS-01", "harga": 100000, "status": "Tersedia"},
    "C008": {"jenis": "Nintendo Switch", "unit": "NS-02", "harga": 100000, "status": "Tersedia"},
    "C009": {"jenis": "Xbox", "unit": "X-01", "harga": 100000, "status": "Tidak Tersedia"},
    "C010": {"jenis": "Xbox", "unit": "X-02", "harga": 100000, "status": "Tersedia"}
}

pelanggan = {
    "P001": {"nama": "Nazril", "password": "rilease", "no_hp": "082254457382"},
    "P002": {"nama": "Fadil", "password": "anak", "no_hp": "081376529601"},
    "P003": {"nama": "Ilham", "password": "ilham123", "no_hp": "081256238729"},
    "P004": {"nama": "Klein", "password": "lotm", "no_hp": "082249381742"},
    "P005": {"nama": "Rex", "password": "pluto", "no_hp": "082144209194"},
    "P006": {"nama": "Zenn", "password": "upr123", "no_hp": "082245538389"}
}

penyewaan = {
    "S001": {"id_pelanggan": "P002", "id_konsol": "C002", "durasi": "1 Hari", "total": 150000, "status": "Berlangsung"},
    "S002": {"id_pelanggan": "P001", "id_konsol": "C003", "durasi": "3 Hari", "total": 240000, "status": "Berlangsung"},
    "S003": {"id_pelanggan": "P003", "id_konsol": "C005", "durasi": "1 Hari", "total": 40000, "status": "Berlangsung"},
    "S004": {"id_pelanggan": "P004", "id_konsol": "C006", "durasi": "2 Hari", "total": 80000, "status": "Selesai"},
    "S005": {"id_pelanggan": "P005", "id_konsol": "C009", "durasi": "1 Hari", "total": 100000, "status": "Selesai"}
}

counter_konsol = 0
for id_k in konsol:
    if int(id_k[1:]) > counter_konsol:
        counter_konsol = int(id_k[1:])

counter_pelanggan = 0
for id_p in pelanggan:
    if int(id_p[1:]) > counter_pelanggan:
        counter_pelanggan = int(id_p[1:])

counter_sewa = 0
for id_s in penyewaan:
    if int(id_s[1:]) > counter_sewa:
        counter_sewa = int(id_s[1:])

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
                for id_p, p in pelanggan.items():
                    if p["nama"].lower() == username_input.lower() and p["password"].lower() == password_input.lower():
                        akun_ditemukan = True
                        user_id = id_p
                        user = p

                if akun_ditemukan:
                    os.system("cls")
                    print(f"Login berhasil, Selamat datang {user['nama']}!")
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
            for p in pelanggan.values():
                if p["nama"].lower() == nama.lower():
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
                pelanggan[id_baru] = {"nama": nama, "password": pw, "no_hp": no_hp}
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

            for id_k, k in konsol.items():
                print(f"{id_k:<6}{k['jenis']:<18}{k['unit']:<9}{k['harga']:<12}{k['status']}")

            print("============================================================")

        elif pilih == "2":
            os.system("cls")
            print("--- TAMBAH UNIT ---")
            jenis = input("Jenis konsol (Contoh: PS5): ").strip()
            unit = input("Kode unit (Contoh: PS-03): ").strip().upper()
            harga = input("Harga sewa per hari: ").strip()

            unit_dipakai = False
            for k in konsol.values():
                if k["unit"].upper() == unit:
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
                konsol[id_baru] = {"jenis": jenis, "unit": unit, "harga": int(harga), "status": "Tersedia"}
                print(f"Konsol berhasil ditambahkan dengan ID {id_baru}")

        elif pilih == "3":
            os.system("cls")
            print("--- UBAH UNIT ---")
            id_input = input("ID konsol yang diubah: ").strip().upper()

            data = None
            if id_input in konsol:
                data = konsol[id_input]

            if data is None:
                os.system("cls")
                print("ID konsol tidak ditemukan!")

            else:
                os.system("cls")
                print("--- DETAIL KONSOL ---")
                print(f"ID Konsol   : {id_input}")
                print(f"Jenis       : {data['jenis']}")
                print(f"Kode Unit   : {data['unit']}")
                print(f"Harga/Hari  : Rp.{data['harga']}")
                print(f"Status      : {data['status']}")

                sedang_disewa = False
                for s in penyewaan.values():
                    if s["id_konsol"] == id_input and s["status"] == "Berlangsung":
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
                        data["harga"] = int(harga_baru)
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
                            data["status"] = "Tersedia"
                            os.system("cls")
                            print("Status diubah menjadi Tersedia")

                        elif pilih_status == "2":
                            data["status"] = "Tidak Tersedia"
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
            if id_input in konsol:
                data = konsol[id_input]

            if data is None:
                os.system("cls")
                print("ID konsol tidak ditemukan!")

            else:
                sedang_disewa = False
                for s in penyewaan.values():
                    if s["id_konsol"] == id_input and s["status"] == "Berlangsung":
                        sedang_disewa = True

                if sedang_disewa:
                    os.system("cls")
                    print("Konsol tidak bisa dihapus karena sedang disewa!")

                else:
                    os.system("cls")
                    print("--- DETAIL KONSOL ---")
                    print(f"ID Konsol   : {id_input}")
                    print(f"Jenis       : {data['jenis']}")
                    print(f"Kode Unit   : {data['unit']}")
                    print(f"Harga/Hari  : Rp.{data['harga']}")
                    print(f"Status      : {data['status']}")
                    yakin = input(f"Yakin hapus {data['jenis']} ({data['unit']})? (y/n): ").strip().lower()

                    if yakin == "y":
                        del konsol[id_input]
                        os.system("cls")
                        print(f"Konsol {data['jenis']} : {data['unit']} berhasil dihapus")

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

                for id_p, p in pelanggan.items():
                    print(f"{id_p:<8}{p['nama']:<15}{p['password']:<20}{p['no_hp']:<15}")

                print("============================================================")

            elif pilih == "2":
                os.system("cls")
                print("--- HAPUS PELANGGAN ---")
                id_input = input("ID pelanggan yang dihapus: ").strip().upper()

                data = None
                if id_input in pelanggan:
                    data = pelanggan[id_input]

                if data is None:
                    os.system("cls")
                    print("ID pelanggan tidak ditemukan!")

                else:
                    punya_sewa = False
                    for s in penyewaan.values():
                        if s["id_pelanggan"] == id_input and s["status"] == "Berlangsung":
                            punya_sewa = True

                    if punya_sewa:
                        os.system("cls")
                        print("Pelanggan tidak bisa dihapus, masih ada sewa yang berlangsung!")

                    else:
                        os.system("cls")
                        print("--- DETAIL PELANGGAN ---")
                        print(f"ID Pelanggan : {id_input}")
                        print(f"Nama         : {data['nama']}")
                        print(f"No HP        : {data['no_hp']}")
                        yakin = input(f"Yakin hapus pelanggan {data['nama']}? (y/n): ").strip().lower()

                        if yakin == "y":
                            del pelanggan[id_input]
                            os.system("cls")
                            print(f"Pelanggan {data['nama']} berhasil dihapus")

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

                for id_s, s in penyewaan.items():
                    print(f"{id_s:<10}{s['id_pelanggan']:<15}{s['id_konsol']:<12}{s['durasi']:<12}{s['total']:<15}{s['status']:<12}")

                print("===========================================================================")

            elif pilih == "2":
                os.system("cls")
                print("--- SELESAIKAN SEWA ---")
                id_input = input("ID sewa yang diselesaikan: ").strip().upper()

                data = None
                if id_input in penyewaan and penyewaan[id_input]["status"] == "Berlangsung":
                    data = penyewaan[id_input]

                if data is None:
                    os.system("cls")
                    print("ID sewa tidak ditemukan atau sudah selesai!")

                else:
                    os.system("cls")
                    data["status"] = "Selesai"
                    k = konsol[data["id_konsol"]]
                    k["status"] = "Tersedia"
                    nama_konsol = f"{data['id_konsol']} | {k['jenis']} : {k['unit']}"
                    print(f"Penyewaan selesai, konsol {nama_konsol} kembali tersedia")

            elif pilih == "0":
                halaman = "admin"
                os.system("cls")

            else:
                os.system("cls")
                print("Pilihan tidak valid!")

    elif halaman == "pelanggan":
            print("============================================================")
            print(f"                MENU PELANGGAN - {user['nama']}")
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
                for id_k, k in konsol.items():
                    if k["status"] == "Tersedia":
                        ada = True
                        print(f"{id_k:<6}{k['jenis']:<18}{k['unit']:<9}{k['harga']:<12}{k['status']}")

                if not ada:
                    print("Tidak ada konsol yang tersedia saat ini")

                print("============================================================")

            elif pilih == "2":
                os.system("cls")
                print("============================================================")
                print(f"{'ID':<6}{'Jenis':<18}{'Unit':<9}{'Harga/Hari':<12}{'Status'}")
                print("------------------------------------------------------------")

                ada = False
                for id_k, k in konsol.items():
                    if k["status"] == "Tersedia":
                        ada = True
                        print(f"{id_k:<6}{k['jenis']:<18}{k['unit']:<9}{k['harga']:<12}{k['status']}")

                print("============================================================")

                if not ada:
                    print("Maaf, tidak ada konsol yang tersedia saat ini")

                else:
                    id_input = input("ID konsol yang ingin disewa: ").strip().upper()

                    data = None
                    if id_input in konsol and konsol[id_input]["status"] == "Tersedia":
                        data = konsol[id_input]

                    if data is None:
                        os.system("cls")
                        print("ID konsol tidak ditemukan atau sedang tidak tersedia!")

                    else:
                        hari = input("Lama sewa (1-30 hari): ").strip()
                        if not hari.isdecimal() or int(hari) < 1 or int(hari) > 30:
                            print("Lama sewa harus berupa angka 1 sampai 30!")

                        else:
                            hari = int(hari)
                            total = data["harga"] * hari
                            print(f"{data['jenis']} ({data['unit']}) selama {hari} hari = Rp{total}")
                            yakin = input("Konfirmasi sewa? (y/n): ").strip().lower()

                            if yakin == "y":
                                os.system("cls")
                                counter_sewa += 1
                                id_sewa = f"S{counter_sewa:03d}"
                                penyewaan[id_sewa] = {
                                    "id_pelanggan": user_id,
                                    "id_konsol": id_input,
                                    "durasi": f"{hari} Hari",
                                    "total": total,
                                    "status": "Berlangsung"
                                }
                                data["status"] = "Tidak Tersedia"
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
                for id_s, s in penyewaan.items():
                    if s["id_pelanggan"] == user_id and s["status"] == "Berlangsung":
                        ada = True
                        print(f"{id_s:<12}{s['id_konsol']:<12}{s['durasi']:<12}{s['total']:<15}{s['status']:<14}")

                print("=================================================================")

                if not ada:
                    os.system("cls")
                    print("Kamu tidak punya sewa yang sedang berlangsung")

                else:
                    id_input = input("ID sewa yang ingin dikembalikan: ").strip().upper()

                    data = None
                    if id_input in penyewaan:
                        s = penyewaan[id_input]
                        if s["id_pelanggan"] == user_id and s["status"] == "Berlangsung":
                            data = s

                    if data is None:
                        os.system("cls")
                        print("ID sewa tidak ditemukan!")

                    else:
                        os.system("cls")
                        data["status"] = "Selesai"
                        k = konsol[data["id_konsol"]]
                        k["status"] = "Tersedia"
                        nama_konsol = f"{data['id_konsol']} | {k['jenis']} : {k['unit']}"
                        print(f"Konsol {nama_konsol} berhasil dikembalikan, Terima kasih!")

            elif pilih == "4":
                os.system("cls")
                print("=================================================================")
                print(f"{'ID Sewa':<12}{'ID Konsol':<12}{'Durasi':<12}{'Total':<15}{'Status':<14}")
                print("-----------------------------------------------------------------")

                ada = False
                for id_s, s in penyewaan.items():
                    if s["id_pelanggan"] == user_id:
                        ada = True
                        print(f"{id_s:<12}{s['id_konsol']:<12}{s['durasi']:<12}{s['total']:<15}{s['status']:<14}")

                if not ada:
                    print("Kamu belum pernah menyewa konsol")

                print("=================================================================")

            elif pilih == "0":
                os.system("cls")
                print(f"Logout berhasil. Sampai jumpa, {user['nama']}!")
                halaman = "awal"

            else:
                os.system("cls")
                print("Pilihan tidak valid!")