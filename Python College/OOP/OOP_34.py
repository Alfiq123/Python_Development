# Latihan 4: Pengaturan Harga Jual Komoditas

# Seorang pedagang hasil tani menetapkan harga jual per kilogram untuk komoditasnya. 
# Harga tidak boleh diubah jika nilai yang dimasukkan kurang dari Rp. 0. 

# Buatlah kelas `KomoditasJual` dengan atribut private `__nama_komoditas` dan `__harga_per_kg`. 
#   • Sediakan Getter untuk kedua atribut. 
#   • Sediakan Setter untuk `__harga_per_kg` yang hanya mengizinkan harga.

class KomoditasJual:
    def __init__(self, nama_komoditas, harga_per_kg):
        self.__nama_komoditas = nama_komoditas
        self.__harga_per_kg = harga_per_kg

    # Getter → Nama Komoditas
    def getNamaKomoditas(self): return self.__nama_komoditas

    # Getter → Harga Per Kilogram
    def getHargaPerKg(self): return self.__harga_per_kg

    # Setter → Harga Per Kilogram
    def setHargaPerKg(self, hargaPerKgBaru):
        if hargaPerKgBaru > 0:
            self.__harga_per_kg = hargaPerKgBaru
        else:
            print("\n❌Harga tidak boleh dibawah Rp. 0\n")

if __name__ == "__main__":
    komoditas_jual = KomoditasJual("Jagung", 10000)
    