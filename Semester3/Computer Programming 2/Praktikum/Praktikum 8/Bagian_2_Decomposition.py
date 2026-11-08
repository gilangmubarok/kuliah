
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

# 1. Membuat 24 bulan data dummy (2 tahun)
np.random.seed(42)

tanggal = pd.date_range(
    start='2024-01-01',
    periods=24,
    freq='ME'
)

# Pola: Tren naik + Musiman + Acak
penjualan = (
    np.linspace(10, 50, 24)
    + (np.sin(np.linspace(0, 4 * np.pi, 24)) * 10)
    + np.random.normal(0, 2, 24)
)

df_sales = pd.DataFrame(
    {'Penjualan': penjualan},
    index=tanggal
)

# 2. Melakukan Dekomposisi
hasil_dekomposisi = seasonal_decompose(
    df_sales['Penjualan'],
    model='additive',
    period=12
)

# 3. Menampilkan grafik hasil pecahan
fig = hasil_dekomposisi.plot()
fig.set_size_inches(10, 8)

plt.show()
