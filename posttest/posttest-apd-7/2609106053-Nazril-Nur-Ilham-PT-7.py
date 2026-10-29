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

admin_username = "admin"
admin_password = "admin123"

halaman = "awal"

def pembatas():
    print("=" * 60)

def pembatas2():
    print("-" * 60)

def login():
    print("-- Login --")
    

while True:

    if halaman == "awal":
        os.system("cls")
        pembatas()
        print("                   RENTAL PLAYSTATION")
        pembatas()
        print("(1) Login")
        print("(2) Register")
        print("(0) Keluar")

        try:
            pilihan = int(input("Masukkan pilihan: "))
        except ValueError:
            os.system("cls")
            print("Pilihan tidak valid!")
        else:
            if pilihan == 1:
                
            elif pilihan == 2:
                halaman = "register"
            elif pilihan == 0:
                print("Terima kasih telah menggunakan aplikasi ini.")
                break
            else:
                os.system("cls")
                print("Pilihan tidak valid!")
