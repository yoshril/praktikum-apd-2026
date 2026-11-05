from data import konsol, pelanggan, penyewaan, counter
from logika import cek_login, validasi_register, validasi_harga, validasi_konsol, validasi_hari, cek_tanpa_sewa_aktif, daftar_tersedia, daftar_sewa, jumlah_total
from tampilan import ambil_pilihan, ambil_teks, bersihkan, kembali_ke_menu, tampil_tabel

kolom_konsol = ["ID", "Jenis", "Unit", "Harga/Hari (Rp)", "Status"]
kolom_pelanggan = ["ID", "Nama", "Password", "No. Telepon"]
kolom_sewa = ["ID Sewa", "ID Pelanggan", "ID Konsol", "Durasi", "Total (Rp)", "Status"]

halaman = "awal"
user_id = ""
user = {}

while True:

    if halaman == "awal":
        print("============================================================")
        print("                   RENTAL PLAYSTATION")
        print("============================================================")

        pilih = ambil_pilihan("Pilih Menu", [("Login", "1"), ("Register", "2"), ("Keluar", "0")])
        if pilih == "1":
            print("--- LOGIN ---")
            username_input = ambil_teks("Masukkan username")
            password_input = ambil_teks("Masukkan password", True)

            try:
                halaman_tujuan, user_id, user = cek_login(username_input, password_input)
            except ValueError as pesan:
                bersihkan()
                print(pesan)
            else:
                bersihkan()
                print(f"Login berhasil, Selamat datang {user['nama']}!")
                halaman = halaman_tujuan

        elif pilih == "2":
            print("--- REGISTER ---")
            nama = ambil_teks("Username (Tanpa spasi)")
            pw = ambil_teks("Password (Tanpa spasi)", True)
            no_hp = ambil_teks("Masukkan No HP (12 Digit)")

            try:
                validasi_register(nama, pw, no_hp)
            except ValueError as pesan:
                bersihkan()
                print(pesan)
            else:
                bersihkan()
                counter["P"] += 1
                id_baru = f"P{counter['P']:03d}"
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

        pilih = ambil_pilihan("Pilih menu", [
            ("Kelola Konsol", "1"),
            ("Kelola Pelanggan", "2"),
            ("Kelola Penyewaan", "3"),
            ("Logout", "0")
        ])
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
        print("============================================================")

        pilih = ambil_pilihan("Pilih menu", [
            ("Lihat", "1"),
            ("Tambah", "2"),
            ("Ubah", "3"),
            ("Hapus", "4"),
            ("Kembali", "0")
        ])
        if pilih == "1":
            bersihkan()
            tampil_tabel(kolom_konsol, konsol)

            kembali_ke_menu()

        elif pilih == "2":
            bersihkan()
            print("--- TAMBAH UNIT ---")
            jenis = ambil_teks("Jenis konsol (Contoh: PS5)")
            unit = ambil_teks("Kode unit (Contoh: PS-03)").upper()
            harga = ambil_teks("Harga sewa per hari")

            try:
                harga_valid = validasi_konsol(jenis, unit, harga)
            except ValueError as pesan:
                bersihkan()
                print(pesan)
            else:
                bersihkan()
                counter["C"] += 1
                id_baru = f"C{counter['C']:03d}"
                konsol[id_baru] = {"jenis": jenis, "unit": unit, "harga": harga_valid, "status": "Tersedia"}
                print(f"Konsol berhasil ditambahkan dengan ID {id_baru}")

        elif pilih == "3":
            bersihkan()
            print("--- UBAH UNIT ---")
            id_input = ambil_teks("ID konsol yang diubah").upper()

            try:
                data = konsol[id_input]
            except KeyError:
                bersihkan()
                print("ID konsol tidak ditemukan!")
            else:
                bersihkan()
                print("--- DETAIL KONSOL ---")
                tampil_tabel(kolom_konsol, {id_input: data})

                pilih_ubah = ambil_pilihan("Pilih yang ingin diubah", [("Ubah harga", "1"), ("Ubah status", "2")])
                if pilih_ubah == "1":
                    print("--- UBAH HARGA ---")
                    harga_baru = ambil_teks("Harga baru per hari")

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

                        status_baru = ambil_pilihan("Pilih status baru", ["Tersedia", "Tidak Tersedia"])
                        data["status"] = status_baru
                        bersihkan()
                        print(f"Status diubah menjadi {data['status']}")

        elif pilih == "4":
            bersihkan()
            print("--- HAPUS KONSOL ---")
            id_input = ambil_teks("ID konsol yang ingin dihapus").upper()

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
                    print("--- DETAIL KONSOL ---")
                    tampil_tabel(kolom_konsol, {id_input: data})

                    yakin = ambil_pilihan(f"Yakin hapus {data['jenis']} ({data['unit']})?", [("Ya", "y"), ("Tidak", "n")])
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
        print("============================================================")

        pilih = ambil_pilihan("Pilih menu", [("Lihat", "1"), ("Hapus", "2"), ("Kembali", "0")])
        if pilih == "1":
            bersihkan()
            tampil_tabel(kolom_pelanggan, pelanggan)

            kembali_ke_menu()

        elif pilih == "2":
            bersihkan()
            print("--- HAPUS PELANGGAN ---")
            id_input = ambil_teks("ID pelanggan yang dihapus").upper()

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
                    tampil_tabel(kolom_pelanggan, {id_input: data})

                    yakin = ambil_pilihan(f"Yakin hapus pelanggan {data['nama']}?", [("Ya", "y"), ("Tidak", "n")])
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
        print("============================================================")

        pilih = ambil_pilihan("Pilih menu", [("Lihat", "1"), ("Selesaikan sewa", "2"), ("Kembali", "0")])
        if pilih == "1":
            bersihkan()
            tampil_tabel(kolom_sewa, penyewaan)
            print(f"Total nilai seluruh penyewaan : Rp.{jumlah_total([s['total'] for s in penyewaan.values()], 0)}")

            kembali_ke_menu()

        elif pilih == "2":
            bersihkan()
            print("--- SELESAIKAN SEWA ---")
            id_input = ambil_teks("ID sewa yang diselesaikan").upper()

            try:
                data = daftar_sewa("", True)[id_input]
            except (KeyError, ValueError):
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

        pilih = ambil_pilihan("Pilih menu", [
            ("Lihat konsol tersedia", "1"),
            ("Sewa konsol", "2"),
            ("Kembalikan konsol", "3"),
            ("Riwayat sewa saya", "4"),
            ("Logout", "0")
        ])
        if pilih == "1":
            bersihkan()
            try:
                tersedia = daftar_tersedia()
            except ValueError:
                print("Tidak ada konsol yang tersedia saat ini")
            else:
                tampil_tabel(kolom_konsol, tersedia)

            kembali_ke_menu()

        elif pilih == "2":
            bersihkan()
            try:
                tersedia = daftar_tersedia()
            except ValueError:
                print("Maaf, tidak ada konsol yang tersedia saat ini")
            else:
                tampil_tabel(kolom_konsol, tersedia)
                id_input = ambil_teks("ID konsol yang ingin disewa").upper()

                try:
                    data = tersedia[id_input]
                except KeyError:
                    bersihkan()
                    print("ID konsol tidak ditemukan atau sedang tidak tersedia!")
                else:
                    hari_input = ambil_teks("Lama sewa (1-30 hari)")

                    try:
                        hari = validasi_hari(hari_input)
                    except ValueError as pesan:
                        bersihkan()
                        print(pesan)
                    else:
                        total = data["harga"] * hari
                        print(f"{data['jenis']} ({data['unit']}) selama {hari} hari = Rp{total}")

                        yakin = ambil_pilihan("Konfirmasi sewa?", [("Ya", "y"), ("Tidak", "n")])
                        bersihkan()
                        if yakin == "y":
                            counter["S"] += 1
                            id_sewa = f"S{counter['S']:03d}"
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
                tampil_tabel(kolom_sewa, aktif)
                id_input = ambil_teks("ID sewa yang ingin dikembalikan").upper()

                try:
                    data = aktif[id_input]
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
                tampil_tabel(kolom_sewa, riwayat)

            kembali_ke_menu()

        else:
            bersihkan()
            print(f"Logout berhasil. Sampai jumpa, {user['nama']}!")
            halaman = "awal"


print("Terima kasih telah menggunakan program Rental PlayStation")