# Latihan 5: Kontrol Suhu Ruang Penyimpanan

# Ruang penyimpanan hasil pertanian (Cold Storage) memiliki suhu aktual yang tercatat.
# Untuk menjaga kualitas, suhu tidak boleh di bawah `C` derajat celcius.

# Buatlah kelas `ColdStorage` dengan atribut private `__nama_ruangan` dan `__suhu_aktual`.
#   • Sediakan Getter untuk `__suhu_aktual`.
#   • Sediakan Setter untuk `__suhu_aktual` yang hanya mengizinkan perubahan jika suhu tidak di bawah batas minimum.

class ColdStorage:
    def __init__(self, nama_ruangan, suhu_aktual):
        self.__nama_ruangan = nama_ruangan
        self.__suhu_aktual = suhu_aktual

    # Getter → Nama Ruangan
    def getNamaRuangan(self): return self.__nama_ruangan

    # Getter → Suhu Aktual
    def getSuhuAktual(self): return self.__suhu_aktual

    # Setter → Suhu Aktual
    def setSuhuAktual(self, suhuAktualBaru):
        C = 5

        if suhuAktualBaru > C:
            self.__suhu_aktual = suhuAktualBaru
        else:
            print(f"\n❌ Suhu Aktual tidak boleh di bawah {C} \n")

# Menjalankan Program
if __name__ == "__main__":
    cold_storage = ColdStorage("Ruangan 01", 40)

    print(f"Nama Ruangan : {cold_storage.getNamaRuangan()}")
    print(f"Suhu Aktual  : {cold_storage.getSuhuAktual()}")

    # Mengganti suhu aktual diluar batas
    cold_storage.setSuhuAktual(2)
    print(f"Nama Ruangan : {cold_storage.getNamaRuangan()}")
    print(f"Suhu Aktual  : {cold_storage.getSuhuAktual()}")
