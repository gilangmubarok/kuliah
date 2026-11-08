
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# F. TUGAS MANDIRI: ANALISIS TREN SAHAM

# 1. Membuat data saham
data_saham = {
    'Date': ['15/01/2026', '16/01/2026', '17/01/2026',
             '18/01/2026', '19/01/2026', '20/01/2026',
             '21/01/2026'],
    'Harga_Tutup': [1500, 1520, 1480, 1550, 1600, 1580, 1620],
    'Volume': [1000, 1200, 900, 1500, 2000, 1800, 2200]
}

df_saham = pd.DataFrame(data_saham)

# 1. KONVERSI WAKTU (DATETIME)

# Mengubah kolom Date menjadi format Datetime
df_saham['Date'] = pd.to_datetime(
    df_saham['Date'],
    format='%d/%m/%Y'
)

# Menjadikan kolom Date sebagai Index
df_saham.set_index('Date', inplace=True)

# Menampilkan hasil konversi
print("Data Saham Setelah Konversi:")
print(df_saham)

print("\nTipe Data:")
print(df_saham.dtypes)

# 2. VISUALISASI STATIS MATPLOTLIB

plt.figure(figsize=(10, 5))

plt.plot(
    df_saham.index,
    df_saham['Harga_Tutup'],
    marker='o',
    color='b',
    linestyle='-'
)

plt.title("Pergerakan Harga Saham")
plt.xlabel("Tanggal")
plt.ylabel("Harga_Tutup")
plt.grid(True)

plt.show()

# 3. VISUALISASI INTERAKTIF PLOTLY

fig = px.line(
    df_saham.reset_index(),
    x='Date',
    y='Volume',
    title='Volume Transaksi Interaktif',
    markers=True
)

fig.show()
