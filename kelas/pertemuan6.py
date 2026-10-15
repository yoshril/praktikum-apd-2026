# kartu = {"kartu merah", "kartu merah", "kartu ijo", "kartu biru"}
# print(kartu)

# kartu = ["kartu merah", "kartu merah", "kartu ijo", "kartu biru"]
# kartuku = set(kartu)
# print(kartuku)

# angka_ganjil = {1, 3, 5, 7, 9}

# for angka in angka_ganjil:
#     print(angka)

# kelas = {"a", "b", "c"}
# kelas.add("d")
# print(kelas)

# kelas_b1 = {"juna", "mia", "ilyas", "gabriel", "falih"}
# print(kelas_b1)
# kelas_b1.remove("falih")
# print(kelas_b1)

# kelas_b1 = {"juna", "mia", "ilyas", "gabriel", "falih"}
# print(kelas_b1)
# kelas_b1.discard("fadil")
# print(kelas_b1)

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)

# angka1 = {1, 2, 3, 4, 5}
# angka2 = {2, 4, 6, 8, 10}
# irisan = angka1.intersection(angka2)
# print(irisan)

# angka1 = {1, 2, 3, 4, 5}
# angka2 = {2, 4, 6, 8, 10}
# selisih = angka1.difference(angka2)
# print(selisih)

# angka1 = {1, 2, 3, 4, 5}
# angka2 = {2, 4, 6, 8, 10}
# angka1.update(angka2)
# # print(angka1)

# praktikum = {
#     "apd" : "belajar dictionary",
#     "orsikom" : "belajar logism"
# }

# print(praktikum)
# print(praktikum["orsikom"])

biodata = {
    "nama" : "ilyas",
    "nim" : "049",
    "pacar" : ["laptop", "anime"],
    "sosmed" : "@mhdilyaass",
    "jomblo" : True
}

# print(f"nama saya adalah {biodata['nama']}")
# print(f"pacar nomor 1 adalah {biodata['pacar'][0]}")
# print(biodata.get("nama"))
# print(biodata.get("alamat", "tidak ditemukan"))
# for i in biodata:
#     print(i)

# for i in biodata.keys():
#     print(i)

# for i in biodata.values():
#     print(i)

# for i, j in biodata.items():
#     print(f"{i} : {j}")
#     print(i, j)

# biodata["matkul"] = "kalkulus"
# print(biodata)

# biodata.update({"warna" : "hitam"})
# print(biodata)

# print(biodata)

# list_game = dict(genshin="odette", ml="saber", hayday="ayam")
# print(list_game)

# game = {
#     "pou" : "chill",
#     "genshin impact" : "action",
#     "valorant" : "fps",
#     "minecraft" : "sandbox",
#     "mobile legend" : "moba"
# }

# game_copy = game.copy()
# game_copy["mobile legend"] = "tawuran"

# print(game)
# print(game_copy)

# print("panjang dari dictionary game adalah: ", len(game))
# game.clear()
# print(game)
# cache = game.pop("valorant")
# print(game)
# print(game.get("valorant"))
# print(cache)
# del game["valorant"]
# print(game)
# game.update({"minecraft" : "gore"})
# print(game)
# game["valorant"] = "horror"
# print(game)
# tambah = game.setdefault("resident evil", "horror")
# print(game)

# key = "A", "B", "C"
# value = "anak infor"

# akt26 = dict.fromkeys(key, value)
# print(akt26)

# menu = {
#     "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
#     "nasi" : ["nasi goreng", "nasi uduk"],
#     "mie" : ["mie goreng rendang", "mie goreng aceh"],
#     "kuah" : ["soto", "rawon", "sop iga"]
# }

# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
#     for kategori in j:
#         print(kategori)
#     print("")