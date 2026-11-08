import pandas as pd

# Data dengan penulisan department yang berantakan
data = {
    'Nama': ['Fajar', 'Gita', 'Hani'],
    'Dept': ['IT ', 'HRD', 'Finance']
}

df_karyawan = pd.DataFrame(data)

print("--- Data Sebelum Cleaning Teks ---")

# Terlihat berantakan jika dicetak dalam bentuk list
print(df_karyawan['Dept'].tolist())

# 1. Menghapus spasi di awal dan akhir teks
df_karyawan['Dept'] = df_karyawan['Dept'].str.strip()

# 2. Menyeragamkan menjadi huruf kapital semua
df_karyawan['Dept'] = df_karyawan['Dept'].str.upper()

print("--- Data Setelah Cleaning Teks ---")
print(df_karyawan)