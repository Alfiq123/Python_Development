# Latihan 1: Manajemen Stok Pupuk

# Seorang petani ingin mencatat jumlah stok sebuah pupuk di gudang. Jumlah stok
# harus selalu bernilai positif. 

# Buatlah kelas `Pupuk` dengan atribut private `__nama_pupuk` dan `__stok`.
#   • Sediakan Getter untuk kedua atribut.
#   • Sediakan Setter untuk __stok yang hanya mengizinkan perubahan jika nilai stok baru .

class Pupuk:
    # Inisialisasi
    def __init__(self, namaPupuk, stok):
        self.__namaPupuk = namaPupuk
        self.__stok = stok

    # Getter → Nama Pupuk
    def getNamaPupuk(self): return self.__namaPupuk

    # Getter → Stok Pupuk
    def getStok(self): return self.__stok

    # Setter → Stok
    def setStok(self, stokBaru):
        if stokBaru > 0:
            self.__stok = stokBaru
        elif stokBaru == self.__stok:
            print("❌ Stok tidak boleh sama")
        else:
            print("❌ Stok harus positif!")

    def tambahStok(self, jumlah):
        "Metode untuk menambah stok"
        if jumlah > 0:
            self.__stok += jumlah
        else:
            print("❌ Penambahan barang harus positif!")

    def kurangiStok(self, jumlah):
        if 0 < jumlah <= self.__stok: 
            self.__stok -= jumlah
        else:
            print("❌ Jumlah pengurangan tidak valid!")

# ===== Menjalankan Program =====
if __name__ == "__main__":
    pupuk = Pupuk("Urea", 100)

    # Menampilkan Stok Pupuk
    print(
        f"Nama Pupuk: {pupuk.getNamaPupuk()}\n"
        f"Stok Pupuk Saat Ini: {pupuk.getStok()}\n"
    )

    # Mengubah Stok Pupuk
    pupuk.setStok(50)
    print(f"Stok Pupuk Baru: {pupuk.getStok()}\n")

    # Menghasilkan Error
    pupuk.setStok(-10)
    print(f"Stok Pupuk Baru: {pupuk.getStok()}")
