import os
import inquirer
from prettytable import PrettyTable

def ambil_pilihan(pesan, pilihan_valid):
    jawaban = inquirer.prompt([inquirer.List("hasil", message=pesan, choices=pilihan_valid)])
    if jawaban is None:
        raise SystemExit("Program dihentikan.")
    return jawaban["hasil"]

def ambil_teks(pesan, rahasia=False):
    jenis = inquirer.Password if rahasia else inquirer.Text
    jawaban = inquirer.prompt([jenis("hasil", message=pesan)])
    return "" if jawaban is None else jawaban["hasil"].strip()

def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")

def kembali_ke_menu():
    ambil_pilihan("Selesai melihat data", [("Kembali ke menu", "0")])
    bersihkan()

def tampil_tabel(kolom, data):
    tabel = PrettyTable(kolom)
    tabel.align = "l"
    for id_data, isi in data.items():
        tabel.add_row([id_data, *isi.values()])
    print(tabel)