# Soal 4: Proses Panen

# Buat kelas induk `ProdukTernak` dengan metode `proses_panen()`.
# Buat subclass `DagingSapi` dan `TelurAyam` yang mengesampingkan metode
# tersebut untuk mendeskripsikan langkah-langkah panen yang berbeda.

class ProdukTernak:
    def __init__(self): pass
    def proses_panen(self):
        raise NotImplementedError("Metode ini harus di-override di subclass.")


class DagingSapi(ProdukTernak):
    def __init__(self): super().__init__()
    def proses_panen(self):
        print(
            "  1. Memeriksa kesehatan sapi sebelum pemotongan.\n"
            "  2. Melakukan pemotongan sesuai prosedur.\n"
            "  3. Membersihkan dan memisahkan bagian daging.\n"
            "  4. Mengemas daging untuk distribusi.\n"
        )


class TelurAyam(ProdukTernak):
    def __init__(self): super().__init__()
    def proses_panen(self):
        print(
            "  1. Mengumpulkan telur dari kandang ayam.\n"
            "  2. Membersihkan telur dari kotoran.\n"
            "  3. Menyortir berdasarkan ukuran dan kualitas.\n"
            "  4. Mengemas telur ke dalam wadah karton.\n"
        )


if __name__ == "__main__":
    ayam = TelurAyam()
    sapi = DagingSapi()

    print("═════ Proses Panen Daging Sapi ═════")
    sapi.proses_panen()

    print("═════ Proses Panen Telur Ayam ═════")
    ayam.proses_panen()
