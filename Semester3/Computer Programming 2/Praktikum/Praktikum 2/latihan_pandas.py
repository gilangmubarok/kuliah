import pandas as pd

# 1. INPUT & MENAMPILKAN DATA
df = pd.read_csv("data_mahasiswa.csv")
print("---- Menampilkan seluruh data ----")
print(df)
print("\n")

# 2. JUMLAH BARIS DAN KOLOM (.shape)
baris = df.shape[0]
kolom = df.shape[1]
print("---- Info Dimensi ----")
print(f"Data ini memiliki {baris} baris dan {kolom} kolom.\n")

# 3. TIPE DATA (.info())
print("--- Info Tipe Data ---")
df.info()
print("\n")

# 4. CEK DATA KOSONG / MISSING VALUES (.isnull().sum())
print("--- Cek Data Kosong (Null) ---")
data_kosong = df.isnull().sum()
print(data_kosong)