class Lahan:
    __luashektar: float = float
    __lokasi: str = str

    @property
    def luas_hektar(self):
        return self.__luashektar

    @luas_hektar.setter
    def luas_hektar(self, luashektar):
        self.__luashektar = luashektar

    @property
    def lokasi(self):
        return self.__luashektar

    @lokasi.setter
    def lokasi(self, lokasi):
        self.__lokasi = lokasi

    def tanam(self):
        raise NotImplementedError(
            "Subclass harus mengimplementasikan metode `tanam()` ini"
        )

    def panen(self):
        return (f"Panen telah dilakukan di lahan seluas "
                f"|{self.luas_hektar}| hektar di |{self.lokasi}|")


class Sawah(Lahan):
    def __init__(self, luashektar, lokasi, jenis_irigasi):
        super().__init__(luashektar, lokasi)
        self.jenis_irigasi = jenis_irigasi

    def tanam(self):
        return (f"Menanam padi di sawah |{self.lokasi}| "
                f"dengan irigasi |{self.jenis_irigasi}|")


class KebunKering(Lahan):
    def __init__(self, luashektar, lokasi):
        super().__init__(luashektar, lokasi)

    def tanam(self):
        return f"Menanam palawija di kebun kering |{self.lokasi}|"


if __name__ == "__main__":
    ...

    # sawah_1 = Sawah(luashektar=16,
    #                 lokasi="Desa SukaMundur",
    #                 jenis_irigasi="Otomatis")

    # sawah_2 = Sawah(luashektar=24,
    #                 lokasi="Desa TaniJaya",
    #                 jenis_irigasi="Manual")

    # print(f"{sawah_1.tanam()}\n"
    #       f"{sawah_1.panen()}\n")

    # print(f"{sawah_2.tanam()}\n"
    #       f"{sawah_2.panen()}\n")

    # kebun_kering_1 = KebunKering(luashektar=32,
    #                              lokasi="Desa MajuJaya")

    # kebun_kering_2 = KebunKering(luashektar=48,
    #                              lokasi="Desa MundurMundur")

    # print(f"{kebun_kering_1.tanam()}\n"
    #       f"{kebun_kering_1.panen()}\n")

    # print(f"{kebun_kering_2.tanam()}\n"
    #       f"{kebun_kering_2.panen()}\n")
