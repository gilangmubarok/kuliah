import sqlite3
import pandas as pd

# SETUP DATABASE
conn_toko = sqlite3.connect("toko.db")
kursor = conn_toko.cursor()

# Membuat tabel dan memasukkan data Penjualan
kursor.execute('''CREATE TABLE IF NOT EXISTS Penjualan (
ID_Trx INTEGER PRIMARY KEY,
Produk TEXT,
Kategori TEXT,
Harga INTEGER,
Terjual INTEGER)''')

kursor.execute('DELETE FROM Penjualan')

data_trx = [
    (1, 'Laptop', 'Elektronik', 7500000, 2),
    (2, 'Meja', 'Furniture', 1200000, 5),
    (3, 'Mouse', 'Elektronik', 150000, 10),
    (4, 'Kursi', 'Furniture', 800000, 8),
    (5, 'Monitor', 'Elektronik', 2000000, 3)
]

kursor.executemany(
    'INSERT INTO Penjualan VALUES (?, ?, ?, ?, ?)',
    data_trx
)

conn_toko.commit()

# SOAL 1 Menampilkan transaksi kategori Elektronik dan mengurutkan Terjual dari terbesar
query1 = '''
SELECT *
FROM Penjualan
WHERE Kategori = 'Elektronik'
ORDER BY Terjual DESC
'''

hasil1 = pd.read_sql_query(query1, conn_toko)

print("=== SOAL 1 ===")
print(hasil1)

# SOAL 2 Menghitung Total Barang Terjual untuk masing-masing Kategori
query2 = '''
SELECT
    Kategori,
    SUM(Terjual) AS "Total Terjual"
FROM Penjualan
GROUP BY Kategori
'''

hasil2 = pd.read_sql_query(query2, conn_toko)

print("\n=== SOAL 2 ===")
print(hasil2)

# SOAL 3 Menampilkan kategori dengan Total Terjual lebih dari 10
query3 = '''
SELECT
    Kategori,
    SUM(Terjual) AS "Total Terjual"
FROM Penjualan
GROUP BY Kategori
HAVING SUM(Terjual) > 10
'''

hasil3 = pd.read_sql_query(query3, conn_toko)

print("\n=== SOAL 3 ===")
print(hasil3)

# Menutup koneksi database
conn_toko.close()