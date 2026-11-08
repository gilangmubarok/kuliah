import pandas as pd
import numpy as np

data_toko = {
    "ID_Trx": ["T01", "T02", "T01", "T03", "T04", "T05"],
    "Produk": [" Laptop", "mouse", " Laptop", "KEYBOARD", "monitor ", "mouse"],
    "Harga": [7500000, 150000, 7500000, np.nan, 2000000, np.nan],
    "Jumlah": [1, 5, 1, 2, np.nan, 3]
}

# 1. (Skor 20) Ubah ke DataFrame, deteksi & hapus duplikat
df_toko = pd.DataFrame(data_toko)

print("--- Data Sebelum Cleaning ---")
print(df_toko)

jumlah_duplikat = df_toko.duplicated().sum()
print(f"\nDitemukan {jumlah_duplikat} baris duplikat.")

df_toko = df_toko.drop_duplicates()
print("\n--- Setelah Hapus Duplikat ---")
print(df_toko)

# 2. (Skor 30) Bersihkan kolom Produk - hapus spasi & Title Case
df_toko['Produk'] = df_toko['Produk'].str.strip().str.capitalize()

print("\n--- Setelah Cleaning Kolom Produk ---")
print(df_toko)

# 3. (Skor 30) Atasi Missing Values
# Isi kolom Jumlah yang kosong dengan angka 1
df_toko['Jumlah'] = df_toko['Jumlah'].fillna(1)

# Isi kolom Harga yang kosong dengan rata-rata (mean) Harga
rata_harga = df_toko['Harga'].mean()
df_toko['Harga'] = df_toko['Harga'].fillna(rata_harga)

print("\n--- Setelah Missing Values Diisi ---")
print(df_toko)

# 4. (Skor 20) Export ke CSV
df_toko.to_csv("transaksi_bersih.csv", index=False)
print("\nFile 'transaksi_bersih.csv' berhasil disimpan.")