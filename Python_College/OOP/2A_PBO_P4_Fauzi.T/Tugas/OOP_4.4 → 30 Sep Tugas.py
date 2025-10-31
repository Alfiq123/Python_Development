class Organisme:
    def __init__(self):
        pass

    def metode_hidup(self):
        return "Semua organisme memiliki cara hidup masing-masing."


class Hama(Organisme):
    def __init__(self, tingkat_kerusakan):
        super().__init__()
        self.tingkat_kerusakan = tingkat_kerusakan

    def metode_hidup(self):
        return "Hama biasanya hidup dengan merusak tanaman."


class Ulat(Hama):
    def __init__(self, tingkat_kerusakan):
        super().__init__(tingkat_kerusakan)

    def serang_tanaman(self):
        return (
            f"Ulat menggigit daun hingga berlubang. "
            f"Tingkat kerusakan: {self.tingkat_kerusakan}"
        )


class Wereng(Hama):
    def __init__(self, tingkat_kerusakan):
        super().__init__(tingkat_kerusakan)

    def serang_tanaman(self):
        return (
            f"Wereng menghisap cairan batang padi hingga layu. "
            f"Tingkat kerusakan: {self.tingkat_kerusakan}"
        )


if __name__ == "__main__":
    serangga_a = Organisme()
    serangga_b = Hama(tingkat_kerusakan=256)
    serangga_ba = Ulat(tingkat_kerusakan=128)
    serangga_bb = Wereng(tingkat_kerusakan=64)

    print(
        "\n"
        f"{serangga_a.metode_hidup()}\n"
        f"{serangga_b.metode_hidup()}\n"
        f"{serangga_ba.serang_tanaman()}\n"
        f"{serangga_bb.serang_tanaman()}\n"
    )
