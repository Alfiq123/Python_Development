from random import randint


class PengendalianHama:
    def __init__(self, luas_lahan, taget_hama, efektifitas):
        self.luas_lahan = luas_lahan
        self.target_hama = taget_hama
        self.efektifitas = efektifitas

    def hitung_total(self):
        raise NotImplementedError(
            "Harus diimplementasikan di subclass."
        )

    def informasi(self):
        raise NotImplementedError(
            "Harus diimplementasikan di subclass."
        )


# Konsep Pewarisan (Inheritance)
class Pestisida(PengendalianHama):
    def __init__(self, luas_lahan, taget_hama, efektifitas):
        super().__init__(luas_lahan, taget_hama, efektifitas)

    # Dosis per meter persegi = 5 milimeter
    # └── 5 Milimeter / Meter Persegi
    def hitung_total(self):  # Override dari induk
        return 5 * self.luas_lahan

    def informasi(self):
        # Konsep Overriding
        return (f"=== INFORMASI PESTISIDA ===\n"
                f"  Luas Lahan: {self.luas_lahan:,} m²\n"
                f"  Target Hama: {self.target_hama}\n"
                f"  Tingkat Efektifitas: {self.efektifitas}%\n"
                f"  Cara Kerja: Pestisida disemprotkan "
                f"secara merata di seluruh area lahan.\n"
                f"  Dosis Pestisida: {self.hitung_total():,} "
                f"milimeter\n")


# Konsep Pewarisan (Inheritance)
class PredatorAlami(PengendalianHama):
    def __init__(self, luas_lahan, taget_hama, efektifitas):
        super().__init__(luas_lahan, taget_hama, efektifitas)

    # 1 Jebakan per 100 meter persegi
    # └── 1 Jebakan / 100 meter persegi
    def hitung_total(self):  # Override dari induk
        return self.luas_lahan / 100

    def informasi(self):
        # Konsep Overriding
        return (f"=== INFORMASI PREDATOR ALAMI ===\n"
                f"  Luas Lahan: {self.luas_lahan:,} m²\n"
                f"  Target Hama: {self.target_hama}\n"
                f"  Tingkat Efektifitas: {self.efektifitas}%\n"
                f"  Cara Kerja: Predator alami dilepaskan "
                f"untuk memangsa hama secara alami.\n"
                f"  Jumlah Jebakan: {self.hitung_total():,.0f}\n")


if __name__ == "__main__":
    # Object pertama
    pest_1 = Pestisida(
        luas_lahan=10000,
        taget_hama="Kutu Daun",
        efektifitas=randint(a=20, b=80)
    )
    # Object kedua
    pred_1 = PredatorAlami(
        luas_lahan=10000,
        taget_hama="Tikus",
        efektifitas=randint(a=20, b=80)
    )

    print(f"{pest_1.informasi()}\n"
          f"{pred_1.informasi()}\n")
