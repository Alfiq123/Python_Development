class Peternakan:
    __nama = __daftar_hewan = None

    def get_peternakan(self):
        return self.__nama

    def set_peternakan(self, nama_baru):
        self.__nama = nama_baru
        return self.__nama

    def tambah_hewan(self):
        pass


class HewanTernak:
    __nama = __jenis = __pakan = __berat = None

    def get_nama_jenis_pakan_berat(self):
        return (
            f"{self.__nama}\n"
            f"{self.__jenis}\n"
            f"{self.__pakan}\n"
            f"{self.__berat}\n"
        )

    def set_nama_jenis_pakan_berat(self, nama, jenis, pakan, berat):
        self.__nama = nama
        self.__jenis = jenis
        self.__pakan = pakan
        self.__berat = berat

        return (
            f"{self.__nama}\n"
            f"{self.__jenis}\n"
            f"{self.__pakan}\n"
            f"{self.__berat}\n"
        )

    def kebutuhan_pakan_harian(self):
        return 0 + 0


class Sapi(HewanTernak):
    pass

    def kebutuhan_pakan_harian(self):
        return 128 + 128


class Kambing(HewanTernak):
    pass

    def kebutuhan_pakan_harian(self):
        return 64 + 64


class Pakan:
    __nama = __komposisi = None


class KomposisiPakan:
    __jenis = __jumlah = None
    pakan = Pakan()




if __name__ == "__main__":
    sapi = Sapi()

    sapi.set_nama_jenis_pakan_berat(nama="Fauzi", jenis="Sapi", pakan=128, berat=256)

    print(sapi.get_nama_jenis_pakan_berat())
