import pandas as pd 
import numpy as np

#1. Membuat DataFrame Kotor
data_mentah = {
    'ID': ['KO1', 'KO2', 'KO3','K01', 'KO4', 'KO5'], # K01 muncul 2X
    'Nama': ['Andi', 'Budi', 'Citra', 'Andi', 'Diana', 'Eka'], 
    'Umur': [25, np.nan, 22, 25, 28, np.nan], # Ada 2 data kosong
    'Gaji': [5000000, 65000000, 7000000, 5000000, np.nan, 4500000] # Ada 1 data kosong
}
df = pd.DataFrame(data_mentah)

print("--- Data Mentah (Kotor) ---")
print(df)

# 2. Cek dan Hapus Data Duplikat
jumlah_duplikat = df.duplicated().sum()
print(f"\nDitemukan {jumlah_duplikat} baris data duplikat.")

# Menghapus duplikat secara permanen
df.drop_duplicates(inplace=True)
print("\n--- Data Setelah Duplikat Dihapus ---")
print(df)