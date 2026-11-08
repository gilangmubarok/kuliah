
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Membuat data mentah harian
# Tanggal masih berupa Teks/String
data = {
    'Tanggal': ['2026-10-01', '2026-10-02', '2026-10-03',
                '2026-10-04', '2026-10-05'],
    'Pengunjung': [150, 165, 140, 200, 250]
}

df = pd.DataFrame(data)

print("Tipe data awal:\n", df.dtypes)

# 2. Mengubah teks menjadi format baku Datetime Pandas
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

# 3. Menjadikan kolom Tanggal sebagai Index
df.set_index('Tanggal', inplace=True)

print("\nSetelah Tanggal menjadi Index:\n", df.head())

# 4. Memvisualisasikan dengan Line Chart dasar
plt.figure(figsize=(8, 4))
plt.plot(df.index, df['Pengunjung'], marker='o',
         color='b', linestyle='-')

plt.title("Tren Pengunjung Harian (Oktober 2026)")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Pengunjung")
plt.grid(True)
plt.show()
