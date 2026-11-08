
# Nama  : Gilang Mubarok
# Prodi : Teknologi Informasi
# Kelas : TI 2A
# NIM   : 4112759201250014

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os

# 0. MENGAMBIL DATASET
# Blok ini hanya berjalan jika file sampel belum ada, sehingga program tetap bisa dijalankan tanpa mengunduh ulang.

if not os.path.exists("online_retail_150.csv"):

    # Membaca dataset lengkap
    df_full = pd.read_csv(
        "hf://datasets/jason1966/abhishekrp1517_online-retail-transactions-dataset/Online Retail.csv"
    )

    # Mengambil 150 baris secara acak
    df_sample = df_full.sample(n=150, random_state=42)

    # Menyimpan dataset untuk UTS
    df_sample.to_csv("online_retail_150.csv", index=False)

    print("Dataset sampel berhasil dibuat.")


# 1. MEMBACA DAN MEMAHAMI DATA
# Membaca dataset sampel yang sudah dibuat
df = pd.read_csv("online_retail_150.csv")

# 1a. Menampilkan 5 baris pertama
print("=== 1a. LIMA BARIS PERTAMA ===")
print(df.head())

# Menampilkan jumlah baris dan kolom
print("\nJumlah baris :", df.shape[0])
print("Jumlah kolom :", df.shape[1])

# Menampilkan tipe data setiap kolom
print("\nTipe data setiap kolom:")
print(df.dtypes)

# 1b. Mengidentifikasi missing values
print("\n=== 1b. MISSING VALUES ===")
print(df.isnull().sum())

# Mengidentifikasi data duplikat
print("\nJumlah data duplikat:", df.duplicated().sum())


# 2. PREPROCESSING DATA 
# Membuat salinan agar data asli tetap tersedia
df_clean = df.copy()

# 2a. Menangani missing values
df_clean["Description"] = (
    df_clean["Description"].fillna("UNKNOWN")
)

# CustomerID merupakan identitas pelanggan.
# Nilai -1 digunakan sebagai penanda ID yang tidak diketahui.
df_clean["CustomerID"] = (
    pd.to_numeric(df_clean["CustomerID"], errors="coerce")
    .fillna(-1)
    .astype("int64")
)

print("\n=== 2a. MISSING VALUES SETELAH PREPROCESSING ===")
print(df_clean.isnull().sum())

# 2b. Membersihkan teks Description
# Menghapus spasi di awal dan akhir, lalu mengubah ke huruf kapital
df_clean["Description"] = (
    df_clean["Description"].str.strip().str.upper()
)

print("\n=== 2b. DESCRIPTION SETELAH DIBERSIHKAN ===")
print(df_clean["Description"].head())

# 2c. Menyimpan data bersih tanpa index
df_clean.to_csv("retail_bersih.csv", index=False)

print("\nFile retail_bersih.csv berhasil disimpan.")


# MEMBUAT DATABASE SQLITE
conn = sqlite3.connect("retail.db")

df_clean.to_sql(
    "retail",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database retail.db berhasil dibuat.")


# 3. VISUALISASI DAN EXPLORATORY DATA ANALYSIS
df_sales = df_clean[
    (df_clean["Quantity"] > 0) &
    (df_clean["UnitPrice"] > 0)
].copy()

# Menghitung total penjualan setiap transaksi
df_sales["TotalSales"] = (
    df_sales["Quantity"] * df_sales["UnitPrice"]
)

print("\n=== DATA UNTUK ANALISIS PENJUALAN ===")
print("Jumlah transaksi awal :", len(df_clean))
print("Jumlah transaksi yang dianalisis :", len(df_sales))


# 3a. BAR CHART 5 PRODUK DENGAN UNIT TERJUAL TERTINGGI
top5 = (
    df_sales.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n=== 3a. TOP 5 PRODUK BERDASARKAN UNIT TERJUAL ===")
print(top5)

plt.figure(figsize=(10, 6))

top5.sort_values().plot(
    kind="barh"
)

plt.title("5 Produk dengan Unit Terjual Tertinggi")
plt.xlabel("Jumlah Unit Terjual")
plt.ylabel("Nama Produk")
plt.tight_layout()
plt.show()


# 3b. HISTOGRAM DISTRIBUSI UNITPRICE
plt.figure(figsize=(10, 6))

plt.hist(
    df_clean["UnitPrice"].dropna(),
    bins=30,
    edgecolor="black"
)

plt.title("Distribusi Harga Produk (UnitPrice)")
plt.xlabel("Harga Produk")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.show()


# 3c. TOP 5 NEGARA BERDASARKAN TOTAL PENJUALAN
top_negara = (
    df_sales.groupby("Country")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n=== 3c. TOP 5 NEGARA BERDASARKAN TOTAL PENJUALAN ===")
print(top_negara)

# Visualisasi tambahan untuk membandingkan penjualan antarnegara
plt.figure(figsize=(10, 6))

top_negara.sort_values().plot(
    kind="barh"
)

plt.title("5 Negara dengan Total Penjualan Tertinggi")
plt.xlabel("Total Penjualan")
plt.ylabel("Negara")
plt.tight_layout()
plt.show()



# 3e. BOXPLOT UNTUK MENDETEKSI OUTLIER
# Boxplot Quantity
plt.figure(figsize=(8, 5))

sns.boxplot(y=df_clean["Quantity"])

plt.title("Boxplot Quantity")
plt.ylabel("Jumlah Unit")
plt.tight_layout()
plt.show()

# Boxplot UnitPrice
plt.figure(figsize=(8, 5))

sns.boxplot(y=df_clean["UnitPrice"])

plt.title("Boxplot UnitPrice")
plt.ylabel("Harga Produk")
plt.tight_layout()
plt.show()


# ANALISIS OUTLIER DENGAN METODE IQR
print("\n=== HASIL ANALISIS OUTLIER DENGAN IQR ===")

for kolom in ["Quantity", "UnitPrice"]:

    data = df_clean[kolom].dropna()

    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)

    iqr = q3 - q1

    batas_bawah = q1 - (1.5 * iqr)
    batas_atas = q3 + (1.5 * iqr)

    jumlah_outlier = (
        (data < batas_bawah) |
        (data > batas_atas)
    ).sum()

    print(f"\nKolom: {kolom}")
    print(f"Q1: {q1:.2f}")
    print(f"Q3: {q3:.2f}")
    print(f"IQR: {iqr:.2f}")
    print(
        f"Batas bawah: {batas_bawah:.2f}"
    )
    print(
        f"Batas atas: {batas_atas:.2f}"
    )
    print(
        f"Jumlah outlier: {jumlah_outlier} "
        f"dari {len(data)} data"
    )
    print(f"Nilai minimum: {data.min()}")
    print(f"Nilai maksimum: {data.max()}")


# 3d. KESIMPULAN ANALISIS
produk_teratas = top5.index[0]
unit_teratas = top5.iloc[0]

negara_teratas = top_negara.index[0]
total_teratas = top_negara.iloc[0]

print("\n=== 3d. KESIMPULAN ANALISIS ===")

print(f"""
Berdasarkan hasil analisis, terdapat {len(df_clean)} baris data
yang diperiksa. Dari jumlah tersebut, sebanyak {len(df_sales)}
transaksi digunakan untuk menghitung penjualan karena jumlah
barang dan harganya lebih dari nol.

Produk yang paling banyak terjual adalah {produk_teratas},
dengan jumlah sebanyak {unit_teratas} unit.

Negara dengan total penjualan tertinggi adalah {negara_teratas},
dengan nilai penjualan sebesar {total_teratas:.2f}.

Dari grafik histogram, kita dapat melihat perbedaan harga
barang yang dijual. Grafik boxplot juga menunjukkan beberapa
data yang nilainya jauh berbeda dari data lainnya, baik pada
jumlah barang maupun harga. Hal ini bisa terjadi karena ada
pembelian dalam jumlah besar atau barang yang harganya lebih mahal.

Secara keseluruhan, hasil analisis menunjukkan bahwa produk
memiliki jumlah penjualan yang berbeda-beda dan United Kingdom
menjadi negara dengan nilai penjualan tertinggi dalam sampel ini.
Namun, karena data yang dianalisis hanya 150 baris, hasilnya
belum tentu menggambarkan seluruh transaksi Online Retail.
""")

print("\n=== PROGRAM SELESAI ===")
print("File yang dihasilkan:")
print("1. retail_bersih.csv")
print("2. retail.db")
