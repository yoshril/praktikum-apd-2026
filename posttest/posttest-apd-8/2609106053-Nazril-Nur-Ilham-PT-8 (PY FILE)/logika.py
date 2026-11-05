from data import konsol, pelanggan, penyewaan, admin_username, admin_password

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
    if nama.lower() == admin_username or any(p["nama"].lower() == nama.lower() for p in pelanggan.values()):
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
    if any(k["unit"].upper() == unit for k in konsol.values()):
        raise ValueError("Kode unit sudah dipakai konsol lain!")
    return validasi_harga(harga_teks)

def validasi_hari(teks):
    if not teks.isdecimal() or int(teks) < 1 or int(teks) > 30:
        raise ValueError("Lama sewa harus berupa angka 1 sampai 30!")
    return int(teks)

def cek_tanpa_sewa_aktif(kolom, kode):
    if any(s[kolom] == kode and s["status"] == "Berlangsung" for s in penyewaan.values()):
        raise ValueError("Data masih memiliki penyewaan yang berlangsung!")

def daftar_tersedia():
    hasil = {id_k: k for id_k, k in konsol.items() if k["status"] == "Tersedia"}
    if not hasil:
        raise ValueError("Data tidak ditemukan atau kosong!")
    return hasil

def daftar_sewa(id_pelanggan, hanya_aktif):
    hasil = {id_s: s for id_s, s in penyewaan.items() if id_pelanggan in ("", s["id_pelanggan"]) and (s["status"] == "Berlangsung" or not hanya_aktif)}
    if not hasil:
        raise ValueError("Data tidak ditemukan atau kosong!")
    return hasil

def jumlah_total(daftar, indeks):
    if indeks == len(daftar):
        return 0
    return daftar[indeks] + jumlah_total(daftar, indeks + 1)