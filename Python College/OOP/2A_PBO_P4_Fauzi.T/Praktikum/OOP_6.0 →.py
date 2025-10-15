class Mahasiswa:
    def __init__(self, npm: int, nama: str) -> None:
        self.__npm = npm
        self.__nama = nama

    def get_npm(self) -> int:
        return self.__npm

    def set_npm(self, npm_baru: int) -> int:
        self.__npm = npm_baru
        return self.__npm

    def get_nama(self) -> str:
        return self.__nama

    def set_nama(self, nama_baru: str) -> str:
        self.__nama = nama_baru
        return self.__nama

    # noinspection PyMethodMayBeStatic
    def input_krs(self, krs: int) -> int:
        return krs


class MahasiswaB:
    __npm = __nama = None

    def get_npm(self) -> int:
        return self.__npm

    def set_npm(self, npm_baru: int) -> int:
        self.__npm = npm_baru
        return self.__npm

    def get_nama(self) -> str:
        return self.__nama

    def set_nama(self, nama_baru: str) -> str:
        self.__nama = nama_baru
        return self.__nama

    # noinspection PyMethodMayBeStatic
    def input_krs(self, krs: int) -> int:
        return krs


if __name__ == "__main__":
    # Dengan __init__
    mahasiswa = Mahasiswa(nama="Fauzi", npm=2413020083)

    # Tanpa __init__
    mahasiswa2 = MahasiswaB()

    # Set → NPM dan Nama
    mahasiswa.set_npm(npm_baru=2413020083)
    mahasiswa.set_nama(nama_baru="Fauzi")

    # Print (Menampilkan) → NPM dan Nama
    print(
        f"Nama Mahasiswa: "
        f"{mahasiswa.get_npm()}\n"
        f"NPM Mahasiswa: "
        f"{mahasiswa.get_nama()}\n"
    )

    # Set (Ganti) → NPM dan Nama Baru
    mahasiswa.set_npm(npm_baru=2413020000)
    mahasiswa.set_nama(nama_baru="Izuaf")

    # Print (Menampilkan) → NPM dan Nama Baru
    print(
        f"Nama Mahasiswa Baru: "
        f"{mahasiswa.get_npm()}\n"
        f"NPM Mahasiswa Baru: "
        f"{mahasiswa.get_nama()}\n"
    )

    k_r_s = int(input("Masukkan KRS: "))
    print(f"KRS Kamu: {mahasiswa.input_krs(krs=k_r_s)}")
