# Soal 4: Proses Panen

# Buat kelas induk `ProdukTernak` dengan metode `proses_panen()`.
# Buat subclass `DagingSapi` dan `TelurAyam` yang mengesampingkan metode
# tersebut untuk mendeskripsikan langkah-langkah panen yang berbeda.

class ProdukTernak:
    def __init__(self): pass

    def proses_panen(self):
        pass


class DagingSapi(ProdukTernak):
    def __init__(self): super().__init__()

    def proses_panen(self):
        pass


class TelurAyam(ProdukTernak):
    def __init__(self): super().__init__()

    def proses_panen(self):
        pass


if __name__ == "__main__":
    pass
