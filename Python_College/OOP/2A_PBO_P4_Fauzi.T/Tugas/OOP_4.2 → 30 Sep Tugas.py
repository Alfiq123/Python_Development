class Tanaman:
    def __init__(self, nama):
        self.nama = nama

    @staticmethod
    def tumbuh():
        return "Tumbuh Subur..."


class TanamanPangan(Tanaman):
    def __init__(self, nama, masa_panen):
        super().__init__(nama)
        self.masa_panen = masa_panen

    def informasi_spesifik(self):
        return (
            f"Nama: {self.nama}\n"
            f"Masa Panen: {self.masa_panen} Hari\n"
            f"{self.tumbuh()}\n"
        )


class TanamanHias(Tanaman):
    def __init__(self, nama, warna_bunga):
        super().__init__(nama)
        self.warna_bunga = warna_bunga

    def informasi_spesifik(self):
        return (
            f"Nama: {self.nama}\n"
            f"Warna Bunga: {self.warna_bunga}\n"
            f"{self.tumbuh()}\n"
        )


if __name__ == "__main__":
    tanam_a = Tanaman(nama="Kelapa")
    tanam_b = TanamanPangan(nama="Jagung", masa_panen="15 Hari")
    tanam_c = TanamanHias(nama="Mawar", warna_bunga="Merah")

    print(
        "\n"
        "═════ Tanaman Pangan ═════     \n"
        f"{tanam_b.informasi_spesifik()}\n"

        "═════ Tanaman Hias ═════       \n"
        f"{tanam_c.informasi_spesifik()}\n"
    )
