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

def hitung_counter(data):
    terbesar = 0
    for kode in data:
        angka = int(kode[1:])
        if angka > terbesar:
            terbesar = angka
    return terbesar

counter_konsol = hitung_counter(konsol)
counter_pelanggan = hitung_counter(pelanggan)
counter_sewa = hitung_counter(penyewaan)

admin_username = "admin"
admin_password = "admin123"

halaman = "awal"
user_id = ""
user = {}

def buat_id_konsol():
    global counter_konsol
    counter_konsol += 1
    id_baru = f"C{counter_konsol:03d}"
    return id_baru

def buat_id_pelanggan():
    global counter_pelanggan
    counter_pelanggan += 1
    id_baru = f"P{counter_pelanggan:03d}"
    return id_baru

def buat_id_sewa():
    global counter_sewa
    counter_sewa += 1
    id_baru = f"S{counter_sewa:03d}"
    return id_baru

def daftar_tersedia():
    hasil = []
    for id_k, k in konsol.items():
        if k["status"] == "Tersedia":
            hasil.append(id_k)
    if len(hasil) == 0:
        raise ValueError("Data tidak ditemukan atau kosong!")
    return hasil

def ambil_pilihan(pesan, pilihan_valid):
    jawaban = input(pesan).strip().lower()
    if jawaban not in pilihan_valid:
        raise ValueError("Pilihan tidak valid!")
    return jawaban

def cek_login(username, password):
    if username == "" or password == "":
        raise ValueError("Username atau Password harus diisi!")
    if username == admin_username and password == admin_password:
        return "admin", "", {"nama": "Admin"}
    for id_p, p in pelanggan.items():
        if p["nama"].lower() == username.lower() and p["password"].lower() == password.lower():
            return "pelanggan", id_p, p
    raise ValueError("Username atau Password salah!")

def validasi_register(nama, pw, no_hp):
    if nama == "" or pw == "" or no_hp == "":
        raise ValueError("Semua data harus diisi!")
    if not nama.isalpha():
        raise ValueError("Nama hanya boleh huruf dan tanpa spasi!")
    nama_dipakai = False
    for p in pelanggan.values():
        if p["nama"].lower() == nama.lower():
            nama_dipakai = True
    if nama.lower() == admin_username or nama_dipakai:
        raise ValueError("Nama sudah dipakai!")
    if " " in pw:
        raise ValueError("Password tidak boleh spasi!")
    if not (no_hp.isascii() and no_hp.isdigit()) or len(no_hp) != 12:
        raise ValueError("No HP hanya boleh angka 12 digit!")

def validasi_harga(teks):
    if not teks.isdecimal() or int(teks) < 1000:
        raise ValueError("Harga harus berupa angka, minimal 1000!")
    return int(teks)

def validasi_konsol(jenis, unit, harga_teks):
    if jenis == "" or unit == "" or harga_teks == "":
        raise ValueError("Semua data harus diisi!")
    for k in konsol.values():
        if k["unit"].upper() == unit:
            raise ValueError("Kode unit sudah dipakai konsol lain!")
    return validasi_harga(harga_teks)

def validasi_hari(teks):
    if not teks.isdecimal() or int(teks) < 1 or int(teks) > 30:
        raise ValueError("Lama sewa harus berupa angka 1 sampai 30!")
    return int(teks)

def cek_tanpa_sewa_aktif(kolom, kode):
    for s in penyewaan.values():
        if s[kolom] == kode and s["status"] == "Berlangsung":
            raise ValueError("Data masih memiliki penyewaan yang berlangsung!")

def ambil_konsol_tersedia(id_konsol):
    data = konsol[id_konsol]
    if data["status"] != "Tersedia":
        raise KeyError(id_konsol)
    return data

def ambil_sewa_berlangsung(id_sewa, id_pelanggan):
    data = penyewaan[id_sewa]
    if data["status"] != "Berlangsung" or (id_pelanggan != "" and data["id_pelanggan"] != id_pelanggan):
        raise KeyError(id_sewa)
    return data

def daftar_sewa(id_pelanggan, hanya_aktif):
    hasil = []
    for id_s, s in penyewaan.items():
        if s["id_pelanggan"] == id_pelanggan and (s["status"] == "Berlangsung" or not hanya_aktif):
            hasil.append(id_s)
    if len(hasil) == 0:
        raise ValueError("Data tidak ditemukan atau kosong!")
    return hasil

def hitung_total(harga, hari):
    return harga * hari

def jumlah_total(daftar, indeks):
    if indeks == len(daftar):
        return 0
    return daftar[indeks] + jumlah_total(daftar, indeks + 1)

def bersihkan():
    os.system("cls")

def tampil_tabel_konsol(hanya_tersedia):
    print("============================================================")
    print(f"{'ID':<6}{'Jenis':<18}{'Unit':<9}{'Harga/Hari':<12}{'Status'}")
    print("------------------------------------------------------------")
    for id_k, k in konsol.items():
        if hanya_tersedia and k["status"] != "Tersedia":
            continue
        print(f"{id_k:<6}{k['jenis']:<18}{k['unit']:<9}{k['harga']:<12}{k['status']}")
    print("============================================================")

def tampil_detail_konsol(id_konsol, data):
    print("--- DETAIL KONSOL ---")
    print(f"ID Konsol   : {id_konsol}")
    print(f"Jenis       : {data['jenis']}")
    print(f"Kode Unit   : {data['unit']}")
    print(f"Harga/Hari  : Rp.{data['harga']}")
    print(f"Status      : {data['status']}")

while True:

    if halaman == "awal":
        print("============================================================")
        print("                   RENTAL PLAYSTATION")
        print("============================================================")
        print("(1) Login")
        print("(2) Register")
        print("(0) Keluar")

        try:
            pilih = ambil_pilihan("Pilih Menu: ", ("1", "2", "0"))
        except ValueError:
            bersihkan()
            print("Pilihan tidak valid!")
        else:
            if pilih == "1":
                print("--- LOGIN ---")
                username_input = input("Masukkan username: ").strip()
                password_input = input("Masukkan password: ").strip()

                try:
                    halaman_tujuan, user_id, user = cek_login(username_input, password_input)
                except ValueError as pesan:
                    bersihkan()
                    print(pesan)
                except ValueError as pesan:
                    bersihkan()
                    print(pesan)
                else:
                    bersihkan()
                    print(f"Login berhasil, Selamat datang {user['nama']}!")
                    halaman = halaman_tujuan

            elif pilih == "2":
                print("--- REGISTER ---")
                nama = input("Username (Tanpa spasi): ").strip()
                pw = input("Password (Tanpa spasi): ").strip()
                no_hp = input("Masukkan No HP (12 Digit): ").strip()

                try:
                    validasi_register(nama, pw, no_hp)
                except ValueError as pesan:
                    bersihkan()
                    print(pesan)
                else:
                    bersihkan()
                    id_baru = buat_id_pelanggan()
                    pelanggan[id_baru] = {"nama": nama, "password": pw, "no_hp": no_hp}
                    print(f"Registrasi berhasil! ID kamu: {id_baru}")
                    print(f"Silakan login dengan username '{nama}'")

            else:
                bersihkan()
                print("Anda keluar dari program...")
                break

    elif halaman == "admin":
        print("============================================================")
        print("                       MENU ADMIN")
        print("============================================================")
        print("(1) Kelola Konsol")
        print("(2) Kelola Pelanggan")
        print("(3) Kelola Penyewaan")
        print("(0) Logout")

        try:
            pilih = ambil_pilihan("Pilih menu: ", ("1", "2", "3", "0"))
        except ValueError:
            bersihkan()
            print("Pilihan tidak ada!")
        else:
            bersihkan()
            if pilih == "1":
                halaman = "admin_konsol"

            elif pilih == "2":
                halaman = "admin_pelanggan"

            elif pilih == "3":
                halaman = "admin_penyewaan"

            else:
                print("Logout berhasil")
                halaman = "awal"

    elif halaman == "admin_konsol":
        print("============================================================")
        print("                  ADMIN > KELOLA KONSOL")
        print("1. Lihat  2. Tambah  3. Ubah  4. Hapus  0. Kembali")

        try:
            pilih = ambil_pilihan("Pilih menu: ", ("1", "2", "3", "4", "0"))
        except ValueError:
            bersihkan()
            print("Pilihan tidak valid!")
        else:
            if pilih == "1":
                bersihkan()
                tampil_tabel_konsol(False)

            elif pilih == "2":
                bersihkan()
                print("--- TAMBAH UNIT ---")
                jenis = input("Jenis konsol (Contoh: PS5): ").strip()
                unit = input("Kode unit (Contoh: PS-03): ").strip().upper()
                harga = input("Harga sewa per hari: ").strip()

                try:
                    harga_valid = validasi_konsol(jenis, unit, harga)
                except ValueError as pesan:
                    bersihkan()
                    print(pesan)
                else:
                    bersihkan()
                    id_baru = buat_id_konsol()
                    konsol[id_baru] = {"jenis": jenis, "unit": unit, "harga": harga_valid, "status": "Tersedia"}
                    print(f"Konsol berhasil ditambahkan dengan ID {id_baru}")

            elif pilih == "3":
                bersihkan()
                print("--- UBAH UNIT ---")
                id_input = input("ID konsol yang diubah: ").strip().upper()

                try:
                    data = konsol[id_input]
                except KeyError:
                    bersihkan()
                    print("ID konsol tidak ditemukan!")
                else:
                    bersihkan()
                    tampil_detail_konsol(id_input, data)
                    print("1. Ubah harga")
                    print("2. Ubah status")

                    try:
                        pilih_ubah = ambil_pilihan("Pilih: ", ("1", "2"))
                    except ValueError:
                        bersihkan()
                        print("Pilihan tidak valid!")
                    else:
                        if pilih_ubah == "1":
                            print("--- UBAH HARGA ---")
                            harga_baru = input("Harga baru per hari: ").strip()

                            try:
                                data["harga"] = validasi_harga(harga_baru)
                            except ValueError as pesan:
                                bersihkan()
                                print(pesan)
                            else:
                                bersihkan()
                                print("Harga berhasil diubah")

                        else:
                            try:
                                cek_tanpa_sewa_aktif("id_konsol", id_input)
                            except ValueError:
                                bersihkan()
                                print("Status tidak bisa diubah karena konsol sedang disewa!")
                            else:
                                bersihkan()
                                print("--- UBAH STATUS ---")
                                print("1. Tersedia")
                                print("2. Tidak Tersedia")

                                try:
                                    pilih_status = ambil_pilihan("Pilih status baru: ", ("1", "2"))
                                except ValueError:
                                    bersihkan()
                                    print("Pilihan tidak valid!")
                                else:
                                    data["status"] = {"1": "Tersedia", "2": "Tidak Tersedia"}[pilih_status]
                                    bersihkan()
                                    print(f"Status diubah menjadi {data['status']}")

            elif pilih == "4":
                bersihkan()
                print("--- HAPUS KONSOL ---")
                id_input = input("ID konsol yang ingin dihapus: ").strip().upper()

                try:
                    data = konsol[id_input]
                except KeyError:
                    bersihkan()
                    print("ID konsol tidak ditemukan!")
                else:
                    try:
                        cek_tanpa_sewa_aktif("id_konsol", id_input)
                    except ValueError:
                        bersihkan()
                        print("Konsol tidak bisa dihapus karena sedang disewa!")
                    else:
                        bersihkan()
                        tampil_detail_konsol(id_input, data)

                        try:
                            yakin = ambil_pilihan(f"Yakin hapus {data['jenis']} ({data['unit']})? (y/n): ", ("y", "n"))
                        except ValueError:
                            bersihkan()
                            print("Pilihan tidak valid!")
                        else:
                            bersihkan()
                            if yakin == "y":
                                del konsol[id_input]
                                print(f"Konsol {data['jenis']} : {data['unit']} berhasil dihapus")

                            else:
                                print("Penghapusan dibatalkan")

            else:
                halaman = "admin"
                bersihkan()

    elif halaman == "admin_pelanggan":
        print("============================================================")
        print("                ADMIN > KELOLA PELANGGAN")
        print("1. Lihat  2. Hapus  0. Kembali")

        try:
            pilih = ambil_pilihan("Pilih menu: ", ("1", "2", "0"))
        except ValueError:
            bersihkan()
            print("Pilihan tidak valid!")
        else:
            if pilih == "1":
                bersihkan()
                print("============================================================")
                print(f"{'ID':<8}{'Nama':<15}{'Password':<20}{'No. Telepon':<15}")
                print("------------------------------------------------------------")
                for id_p, p in pelanggan.items():
                    print(f"{id_p:<8}{p['nama']:<15}{p['password']:<20}{p['no_hp']:<15}")
                print("============================================================")

            elif pilih == "2":
                bersihkan()
                print("--- HAPUS PELANGGAN ---")
                id_input = input("ID pelanggan yang dihapus: ").strip().upper()

                try:
                    data = pelanggan[id_input]
                except KeyError:
                    bersihkan()
                    print("ID pelanggan tidak ditemukan!")
                else:
                    try:
                        cek_tanpa_sewa_aktif("id_pelanggan", id_input)
                    except ValueError:
                        bersihkan()
                        print("Pelanggan tidak bisa dihapus, masih ada sewa yang berlangsung!")
                    else:
                        bersihkan()
                        print("--- DETAIL PELANGGAN ---")
                        print(f"ID Pelanggan : {id_input}")
                        print(f"Nama         : {data['nama']}")
                        print(f"No HP        : {data['no_hp']}")

                        try:
                            yakin = ambil_pilihan(f"Yakin hapus pelanggan {data['nama']}? (y/n): ", ("y", "n"))
                        except ValueError:
                            bersihkan()
                            print("Pilihan tidak valid!")
                        else:
                            bersihkan()
                            if yakin == "y":
                                del pelanggan[id_input]
                                print(f"Pelanggan {data['nama']} berhasil dihapus")

                            else:
                                print("Penghapusan dibatalkan")

            else:
                halaman = "admin"
                bersihkan()

    elif halaman == "admin_penyewaan":
        print("============================================================")
        print("                 ADMIN > KELOLA PENYEWAAN")
        print("1. Lihat  2. Selesaikan sewa  0. Kembali")

        try:
            pilih = ambil_pilihan("Pilih menu: ", ("1", "2", "0"))
        except ValueError:
            bersihkan()
            print("Pilihan tidak valid!")
        else:
            if pilih == "1":
                bersihkan()
                print("===========================================================================")
                print(f"{'ID Sewa':<10}{'ID Pelanggan':<15}{'ID Konsol':<12}{'Durasi':<12}{'Total':<15}{'Status':<12}")
                print("---------------------------------------------------------------------------")
                daftar_total = []
                for id_s, s in penyewaan.items():
                    daftar_total.append(s["total"])
                    print(f"{id_s:<10}{s['id_pelanggan']:<15}{s['id_konsol']:<12}{s['durasi']:<12}{s['total']:<15}{s['status']:<12}")
                print("---------------------------------------------------------------------------")
                print(f"Total nilai seluruh penyewaan : Rp.{jumlah_total(daftar_total, 0)}")
                print("===========================================================================")

            elif pilih == "2":
                bersihkan()
                print("--- SELESAIKAN SEWA ---")
                id_input = input("ID sewa yang diselesaikan: ").strip().upper()

                try:
                    data = ambil_sewa_berlangsung(id_input, "")
                except KeyError:
                    bersihkan()
                    print("ID sewa tidak ditemukan atau sudah selesai!")
                else:
                    bersihkan()
                    data["status"] = "Selesai"
                    k = konsol[data["id_konsol"]]
                    k["status"] = "Tersedia"
                    nama_konsol = f"{data['id_konsol']} | {k['jenis']} : {k['unit']}"
                    print(f"Penyewaan selesai, konsol {nama_konsol} kembali tersedia")

            else:
                halaman = "admin"
                bersihkan()

    elif halaman == "pelanggan":
        print("============================================================")
        print(f"                MENU PELANGGAN - {user['nama']}")
        print("============================================================")
        print("1. Lihat konsol tersedia")
        print("2. Sewa konsol")
        print("3. Kembalikan konsol")
        print("4. Riwayat sewa saya")
        print("0. Logout")

        try:
            pilih = ambil_pilihan("Pilih menu: ", ("1", "2", "3", "4", "0"))
        except ValueError:
            bersihkan()
            print("Pilihan tidak valid!")
        else:
            if pilih == "1":
                bersihkan()
                try:
                    daftar_tersedia()
                except ValueError:
                    print("Tidak ada konsol yang tersedia saat ini")
                else:
                    tampil_tabel_konsol(True)

            elif pilih == "2":
                bersihkan()
                try:
                    daftar_tersedia()
                except ValueError:
                    print("Maaf, tidak ada konsol yang tersedia saat ini")
                else:
                    tampil_tabel_konsol(True)
                    id_input = input("ID konsol yang ingin disewa: ").strip().upper()

                    try:
                        data = ambil_konsol_tersedia(id_input)
                    except KeyError:
                        bersihkan()
                        print("ID konsol tidak ditemukan atau sedang tidak tersedia!")
                    else:
                        hari_input = input("Lama sewa (1-30 hari): ").strip()

                        try:
                            hari = validasi_hari(hari_input)
                        except ValueError as pesan:
                            bersihkan()
                            print(pesan)
                        else:
                            total = hitung_total(data["harga"], hari)
                            print(f"{data['jenis']} ({data['unit']}) selama {hari} hari = Rp{total}")

                            try:
                                yakin = ambil_pilihan("Konfirmasi sewa? (y/n): ", ("y", "n"))
                            except ValueError:
                                bersihkan()
                                print("Pilihan tidak valid!")
                            else:
                                bersihkan()
                                if yakin == "y":
                                    id_sewa = buat_id_sewa()
                                    penyewaan[id_sewa] = {
                                        "id_pelanggan": user_id,
                                        "id_konsol": id_input,
                                        "durasi": f"{hari} Hari",
                                        "total": total,
                                        "status": "Berlangsung"
                                    }
                                    data["status"] = "Tidak Tersedia"
                                    print(f"Penyewaan berhasil! ID sewa kamu: {id_sewa}")

                                else:
                                    print("Penyewaan dibatalkan")

            elif pilih == "3":
                bersihkan()
                try:
                    aktif = daftar_sewa(user_id, True)
                except ValueError:
                    print("Kamu tidak punya sewa yang sedang berlangsung")
                else:
                    print("=================================================================")
                    print(f"{'ID Sewa':<12}{'ID Konsol':<12}{'Durasi':<12}{'Total':<15}{'Status':<14}")
                    print("-----------------------------------------------------------------")
                    for id_s in aktif:
                        s = penyewaan[id_s]
                        print(f"{id_s:<12}{s['id_konsol']:<12}{s['durasi']:<12}{s['total']:<15}{s['status']:<14}")
                    print("=================================================================")
                    id_input = input("ID sewa yang ingin dikembalikan: ").strip().upper()

                    try:
                        data = ambil_sewa_berlangsung(id_input, user_id)
                    except KeyError:
                        bersihkan()
                        print("ID sewa tidak ditemukan!")
                    else:
                        bersihkan()
                        data["status"] = "Selesai"
                        k = konsol[data["id_konsol"]]
                        k["status"] = "Tersedia"
                        nama_konsol = f"{data['id_konsol']} | {k['jenis']} : {k['unit']}"
                        print(f"Konsol {nama_konsol} berhasil dikembalikan, Terima kasih!")

            elif pilih == "4":
                bersihkan()
                try:
                    riwayat = daftar_sewa(user_id, False)
                except ValueError:
                    print("Kamu belum pernah menyewa konsol")
                else:
                    print("=================================================================")
                    print(f"{'ID Sewa':<12}{'ID Konsol':<12}{'Durasi':<12}{'Total':<15}{'Status':<14}")
                    print("-----------------------------------------------------------------")
                    for id_s in riwayat:
                        s = penyewaan[id_s]
                        print(f"{id_s:<12}{s['id_konsol']:<12}{s['durasi']:<12}{s['total']:<15}{s['status']:<14}")
                    print("=================================================================")

            else:
                bersihkan()
                print(f"Logout berhasil. Sampai jumpa, {user['nama']}!")
                halaman = "awal"


print("Terima kasih telah menggunakan program Rental PlayStation")
