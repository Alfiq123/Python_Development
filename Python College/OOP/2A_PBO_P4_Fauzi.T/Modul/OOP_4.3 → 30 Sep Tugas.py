class Kendaraan:
    def __init__(self, kapasitas_muatan):
        self.kapasitas_muatan = kapasitas_muatan

    def angkut(self):
        return (
            f"Kendaraan ... sedang mengangkut hasil tani seberat "
            f"{self.kapasitas_muatan} Kg"
        )


class Pickup(Kendaraan):
    def __init__(self, kapasitas_muatan):
        super().__init__(kapasitas_muatan)

    # Override → `angkut()`
    def angkut(self):
        return (
            f"PickUp dengan kapasitas {self.kapasitas_muatan} Kg. "
            f"Sedang mengangkut hasil tani dengan kecepatan tinggi "
            f"di jalan desa."
        )


class Truk(Kendaraan):
    def __init__(self, kapasitas_muatan):
        super().__init__(kapasitas_muatan)

    # Override → `angkut()`
    def angkut(self):
        return (
            f"Truk dengan kapasitas {self.kapasitas_muatan} Kg. Sedang "
            "Mengangkut hasil tani dalam jumlah besar ke pasar kota."
        )


if __name__ == "__main__":
    kendaraan_a = Kendaraan(kapasitas_muatan=1000)
    kendaraan_b = Pickup(kapasitas_muatan=2000)
    kendaraan_c = Truk(kapasitas_muatan=3000)

    print(
        "\n"
        f"{kendaraan_a.angkut()}\n"
        f"{kendaraan_b.angkut()}\n"
        f"{kendaraan_c.angkut()}\n"
    )
