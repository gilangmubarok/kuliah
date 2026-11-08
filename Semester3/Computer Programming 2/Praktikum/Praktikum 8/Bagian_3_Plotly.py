
import pandas as pd
import numpy as np
import plotly.express as px

# Membuat kembali data penjualan dari Praktik 2
np.random.seed(42)

tanggal = pd.date_range(
    start='2024-01-01',
    periods=24,
    freq='ME'
)

penjualan = (
    np.linspace(10, 50, 24)
    + (np.sin(np.linspace(0, 4 * np.pi, 24)) * 10)
    + np.random.normal(0, 2, 24)
)

df_sales = pd.DataFrame(
    {'Penjualan': penjualan},
    index=tanggal
)

# Mengubah Index menjadi kolom biasa
df_plotly = df_sales.reset_index()

df_plotly.rename(
    columns={'index': 'Bulan'},
    inplace=True
)

# Membuat grafik interaktif
fig = px.line(
    df_plotly,
    x='Bulan',
    y='Penjualan',
    title='Tren Penjualan Bulanan Interaktif (2024-2025)',
    markers=True
)

fig.show()