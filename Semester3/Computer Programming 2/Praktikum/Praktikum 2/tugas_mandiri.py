import json
import csv
import pandas as pd

# Instruksi 1 Buat File JSON

data_produk = [
    {"id": "P01", "nama": "Laptop", "kategori": "Elektronik", "stok": 50},
    {"id": "P02", "nama": "Meja", "kategori": "Furniture", "stok": 5},
    {"id": "P03", "nama": "Mouse", "kategori": "Elektronik", "stok": 120},
    {"id": "P04", "nama": "Kursi", "kategori": "Furniture", "stok": 2}
]

with open("inventory.json", mode="w") as file:
    json.dump(data_produk, file, indent=4)

print("File inventory.json berhasil dibuat!\n")


# Instruksi 2 Filter & Export ke CSV
with open("inventory.json", mode="r") as file:
    data_dari_json = json.load(file)

# Looping untuk filter produk dengan stok < 10
stok_menipis = []
for produk in data_dari_json:
    if produk["stok"] < 10:
        stok_menipis.append([produk["nama"], produk["kategori"], produk["stok"]])

# Simpan hasil filter ke CSV baru, lengkap header
with open("stok_kritis.csv", mode="w", newline="") as file:
    penulis = csv.writer(file)
    penulis.writerow(["Nama", "Kategori", "Stok"])
    penulis.writerows(stok_menipis)

print("File stok_kritis.csv berhasil dibuat!\n")

# Instruksi 3 Verifikasi Pandas
df = pd.read_csv("stok_kritis.csv")

print("---- Info Dimensi ----")
print(df.shape)
print("\n")

print("---- Info Tipe Data ----")
df.info()