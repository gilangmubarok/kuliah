import json

# --- Praktik 3: bikin profil.json
profil_user = {
    "id" : 101,
    "nama" : "Ayu",
    "hobi" : ["Balap", "Kayang"],
    "aktif" : True
}

with open("profil.json", mode="w") as file:
    # json.dump = melempar (dump) data python menjadi file JSON
    # indent=4 = memberikan spasi agar susunannya rapi kebawah
    json.dump(profil_user, file, indent=4)

# --- Praktik 6: update & delete (kode baru, tambahkan di bawah) ---
with open("profil.json", mode="r") as file:
    data_profil = json.load(file)


# UPDATE status aktif
data_profil["aktif"] = False

# DELETE hobi "Coding"
data_profil["hobi"].remove("Balap")

with open("profil.json", mode="w") as file:
    json.dump(data_profil, file, indent=4)



print("File JSON berhasil diperbarui!")