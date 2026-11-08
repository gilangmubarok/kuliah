
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Data eksperimen iklan Instagram
jumlah_pembeli = np.array([450, 380])
jumlah_tayang = np.array([5000, 5000])

# 1. Probabilitas Dasar (Conversion Rate)
conversion_video = (450 / 5000) * 100
conversion_gambar = (380 / 5000) * 100

print("=== PROBABILITAS DASAR ===")
print(f"Conversion Rate Iklan Video: {conversion_video:.2f}%")
print(f"Conversion Rate Iklan Gambar: {conversion_gambar:.2f}%")

# 2. A/B Testing (Z-Test)
z_stat, p_value = proportions_ztest(
    jumlah_pembeli,
    jumlah_tayang
)

print("\n=== HASIL A/B TESTING ===")
print(f"Nilai p-value: {p_value:.5f}")

# 3. Kesimpulan Bisnis
print("\n=== KESIMPULAN BISNIS ===")

if p_value < 0.05:
    print("Fokuskan anggaran pada Iklan Video!")
else:
    print("Performa kedua iklan sama saja.")
