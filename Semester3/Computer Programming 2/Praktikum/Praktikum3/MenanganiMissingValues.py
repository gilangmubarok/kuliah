import pandas as pd
import numpy as np

# Membuat DataFrame
data_mentah = {
    'ID': ['K01', 'K02', 'K03', 'K01', 'K04', 'K05'],
    'Nama': ['Andi', 'Budi', 'Citra', 'Andi', 'Diana', 'Eka'],
    'Umur': [25, np.nan, 22, 25, 28, np.nan],
    'Gaji': [5000000, 65000000, 7000000, 5000000, np.nan, 4500000]
}

df = pd.DataFrame(data_mentah)

# Cek di kolom mana saja terdapat data kosong
print("--- Pengecekan Missing Values ---")
print(df.isnull().sum())

# OPSI A: Menghapus baris yang memiliki NaN
# df_hapus = df.dropna()
# print(df_hapus)

# OPSI B: Imputasi
# 1. Mengisi umur kosong dengan nilai rata-rata
rata_umur = df['Umur'].mean()
df['Umur'] = df['Umur'].fillna(rata_umur)

# 2. Mengisi gaji kosong dengan nilai spesifik
df['Gaji'] = df['Gaji'].fillna(4500000)

print("\n--- Data Setelah Missing Values ---")
print(df)
