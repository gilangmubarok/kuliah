import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data umur pengunjung mall
data_pengunjung = {
    "Umur": [18, 22, 25, 22, 24, 19, 21, 23,
             22, 65, 20, 22, 19, 24, 70, 21]
}

# Membuat DataFrame
df_mall = pd.DataFrame(data_pengunjung)

# ==========================================
# 1. ANALISIS TEKS
# ==========================================

print("Statistik Deskriptif Data Pengunjung:")
print(df_mall.describe())


# ==========================================
# 2. VISUALISASI HISTOGRAM
# ==========================================

plt.hist(
    df_mall["Umur"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribusi Umur Pengunjung")
plt.xlabel("Umur")
plt.ylabel("Jumlah Pengunjung")
plt.show()


# ==========================================
# 3. VISUALISASI BOXPLOT
# ==========================================

sns.boxplot(
    x=df_mall["Umur"]
)

plt.title("Boxplot Umur Pengunjung")
plt.xlabel("Umur")
plt.show()