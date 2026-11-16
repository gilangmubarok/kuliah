# 1. Import Library
import pandas as pd
import numpy as np
import datetime as dt

# ==========================================
# BAGIAN 1: RFM ANALYSIS
# ==========================================

# 2. Membuat Data Dummy Transaksi E-Commerce
np.random.seed(42)
n_trx = 300

data = {
    'ID_Pelanggan': [
        f'CUST-{np.random.randint(1, 51):02d}'
        for _ in range(n_trx)
    ],
    'Tanggal_Trx': pd.to_datetime('2026-01-01') +
    pd.to_timedelta(np.random.randint(0, 180, n_trx), unit='D'),
    'Total_Belanja': np.random.randint(50, 1000, n_trx) * 1000
}

df = pd.DataFrame(data)

print("5 Data Transaksi Teratas:\n", df.head())


# 3. Menentukan Tanggal Acuan
tanggal_acuan = df['Tanggal_Trx'].max() + dt.timedelta(days=1)

print(
    f"\nTanggal Acuan Analisis: "
    f"{tanggal_acuan.strftime('%Y-%m-%d')}"
)


# 4. Menghitung Nilai R, F, M per Pelanggan
rfm = df.groupby('ID_Pelanggan').agg({
    'Tanggal_Trx': lambda x: (tanggal_acuan - x.max()).days,
    'ID_Pelanggan': 'count',
    'Total_Belanja': 'sum'
})


# 5. Merapikan Nama Kolom
rfm.rename(columns={
    'Tanggal_Trx': 'Recency',
    'ID_Pelanggan': 'Frequency',
    'Total_Belanja': 'Monetary'
}, inplace=True)

print("\nHasil Tabel RFM (5 Pelanggan Pertama):\n", rfm.head())


# ==========================================
# BAGIAN 2: DATA PREPROCESSING (SCALING)
# ==========================================

from sklearn.preprocessing import StandardScaler

# 1. Inisialisasi Scaler
scaler = StandardScaler()

# 2. Mengubah Skala R, F, M
rfm_scaled = scaler.fit_transform(
    rfm[['Recency', 'Frequency', 'Monetary']]
)

# 3. Mengembalikan ke Format DataFrame
df_scaled = pd.DataFrame(
    rfm_scaled,
    columns=['Recency', 'Frequency', 'Monetary'],
    index=rfm.index
)

print("\nData RFM Setelah Scaling:\n", df_scaled.head())


# ==========================================
# BAGIAN 3: K-MEANS CLUSTERING
# ==========================================

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Membuat Model K-Means dengan 3 Cluster
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

rfm['Cluster'] = kmeans.fit_predict(df_scaled)


# 2. Melihat Karakteristik Rata-rata Setiap Cluster
profil_cluster = rfm.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'Cluster': 'count'
}).rename(columns={
    'Cluster': 'Jumlah_Pelanggan'
})

print("\n--- Profil Rata-Rata Setiap Cluster ---")
print(profil_cluster.round(1))


# 3. Visualisasi Hasil Segmentasi
plt.figure(figsize=(9, 4.5))

sns.scatterplot(
    data=rfm,
    x='Recency',
    y='Monetary',
    hue='Cluster',
    palette='viridis',
    s=100
)

plt.title('Segmentasi Pelanggan Berdasarkan Recency & Monetary')
plt.xlabel('Recency (Hari Sejak Belanja Terakhir)')
plt.ylabel('Monetary (Total Belanja Rp)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()


# ==========================================
# BAGIAN 4: TUGAS MANDIRI
# EKSPERIMEN DENGAN 4 CLUSTER
# ==========================================

# Membuat Model K-Means dengan 4 Cluster
kmeans_4 = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm_4 = rfm.drop(columns=['Cluster']).copy()

rfm_4['Cluster'] = kmeans_4.fit_predict(df_scaled)


# Menghitung Profil Cluster Baru
profil_cluster_4 = rfm_4.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'Cluster': 'count'
}).rename(columns={
    'Cluster': 'Jumlah_Pelanggan'
})

print("\n--- Profil Rata-Rata Setiap Cluster (4 Cluster) ---")
print(profil_cluster_4.round(1))


# Visualisasi 4 Cluster
plt.figure(figsize=(9, 4.5))

sns.scatterplot(
    data=rfm_4,
    x='Recency',
    y='Monetary',
    hue='Cluster',
    palette='viridis',
    s=100
)

plt.title('Segmentasi Pelanggan dengan 4 Cluster')
plt.xlabel('Recency (Hari Sejak Belanja Terakhir)')
plt.ylabel('Monetary (Total Belanja Rp)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()


# ==========================================
# BAGIAN 5: MENYIMPAN HASIL ANALISIS
# ==========================================

df.to_csv('data_transaksi.csv', index=False)

rfm.to_csv('hasil_rfm_3_cluster.csv')

profil_cluster.round(1).to_csv('profil_3_cluster.csv')

rfm_4.to_csv('hasil_rfm_4_cluster.csv')

profil_cluster_4.round(1).to_csv('profil_4_cluster.csv')

print("\nSemua hasil analisis berhasil disimpan!")
