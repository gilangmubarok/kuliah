import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DATASET RUMAH

data_rumah = {
    'Lokasi': ['Pusat', 'Pinggiran', 'Pusat', 'Pusat',
               'Pinggiran', 'Pusat', 'Pinggiran', 'Pinggiran'],

    'Tipe': ['Minimalis', 'Mewah', 'Mewah', 'Minimalis',
             'Minimalis', 'Mewah', 'Mewah', 'Minimalis'],

    'Luas_Tanah': [120, 300, 250, 100, 90, 400, 280, 85],

    'Harga_Milyar': [1.5, 3.2, 4.0, 1.2, 0.8, 10.5, 2.9, 0.7]
}

df_rumah = pd.DataFrame(data_rumah)

print("=== DATA RUMAH ===")
print(df_rumah)


# TUGAS 1: GROUPBY


total_aset = df_rumah.groupby('Lokasi')['Harga_Milyar'].sum()

print("\n=== TOTAL NILAI ASET PER LOKASI ===")
print(total_aset)



# TUGAS 1: PIVOT TABLE


pivot_rumah = pd.pivot_table(
    df_rumah,
    values='Harga_Milyar',
    index='Lokasi',
    columns='Tipe',
    aggfunc='mean'
)

print("\n=== PIVOT TABLE ===")
print(pivot_rumah)



# TUGAS 2: SCATTER PLOT

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df_rumah,
    x='Luas_Tanah',
    y='Harga_Milyar',
    hue='Tipe',
    s=100
)

plt.title('Hubungan Luas Tanah dengan Harga Rumah')
plt.xlabel('Luas Tanah (m²)')
plt.ylabel('Harga (Miliar Rupiah)')
plt.grid(True)

plt.show()