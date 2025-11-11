# Latihan 3: Pencatatan Hasil Panen

# Seorang petani ingin mencatat hasil panen (dalam kilogram) sebuah komoditas.
# Hasil panen yang dicatat harus selalu berupa bilangan bulat.

# Buatlah kelas `Panen` dengan atribut private `__komoditas` dan `__jumlah_panen`.
#   • Sediakan Getter untuk kedua atribut.
#   • Sediakan Setter untuk `__jumlah_panen` yang hanya menerima masukan berupa bilangan bulat positif.

class Panen:
    def __init__(self, komoditas, jumlah_panen):
        self.__komoditas = komoditas
        self.__jumlah_panen = jumlah_panen

    # Getter → Komoditas
    def getKomoditas(self): return self.__komoditas
    
    # Getter → Jumlah Panen
    def getJumlahPanen(self): return self.__jumlah_panen

    # Setter → Jumlah Panen
    def setJumlahPanen(self, jumlahPanenBaru):
        if jumlahPanenBaru > 0:
            self.__jumlah_panen = jumlahPanenBaru
        else:
            print(
                "\n❌ Jumlah Panen harus "
                "berupa bilangan positif\n"
            )

if __name__ == "__main__":
    panens = Panen("Padi", 10000)

    print(
        f"Hasil panen ( {panens.getKomoditas()} ) "
        f"seberat: {panens.getJumlahPanen():,} Kg"
    )

    panens.setJumlahPanen(20000)
    print(
        f"Hasil panen ( {panens.getKomoditas()} ) "
        f"seberat: {panens.getJumlahPanen():,} Kg"
    )

    panens.setJumlahPanen(-30000)
    print(
        f"Hasil panen ( {panens.getKomoditas()} ) "
        f"seberat: {panens.getJumlahPanen():,} Kg"
    )
