import csv

data_baru = []

#Tahap 1 & 2: Baca dan Filter di Memori Python

with open("data_mahasiswa.csv", mode="r") as file:
    pembaca = csv.reader(file)
    header = next(pembaca)
    data_baru.append(header)

    for baris in pembaca:
        # DELETE: Abaikan data Budi
        if baris[0] == "Budi":
            continue

        # UPDATE: Ubah nilai Andi
        if baris[0] == "Andi":
            baris[2] = 95

        data_baru.append(baris)

# Tahap 3: Tulis ulang file dengan data yang sudah bersih

with open("data_mahasiswa.csv", mode="w", newline="") as file:
    penulis = csv.writer(file)
    penulis.writerows(data_baru)


print("Data CSV berhasil diupdate dan dihapus!")