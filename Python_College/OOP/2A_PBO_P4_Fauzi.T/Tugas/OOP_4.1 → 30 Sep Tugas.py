class AlatPertanian:
    def __init__(self, nama, tenaga):
        self.nama = nama
        self.tenaga = tenaga

    def gunakan(self):
        return f"{self.nama} → Menggunakan Alat..."


class Cangkul(AlatPertanian):
    def __init__(self, nama, tenaga):
        super().__init__(nama, tenaga)
        pass

    # Override → `gunakan()` dari `AlatPertanian`
    def gunakan(self):
        return f"{self.nama} → Menggali Tanah Secara Manual..."


class Traktor(AlatPertanian):
    def __init__(self, nama, tenaga):
        super().__init__(nama, tenaga)
        pass

    # Override → `gunakan()` dari `AlatPertanian`
    def gunakan(self):
        return f"{self.nama} → Membajak Lahan Dengan Mesin..."


if __name__ == "__main__":
    tani = AlatPertanian(nama="PT Suka Kerja", tenaga="Manual / Mesin")
    tani_b = Cangkul(nama="PT Suka Cangkul", tenaga="Manual")
    tani_c = Traktor(nama="PT Suka Traktor", tenaga="Mesin")

    print(
        "\n"
        f"{tani.gunakan()}\n"
        f"{tani_b.gunakan()}\n"
        f"{tani_c.gunakan()}\n"
    )
