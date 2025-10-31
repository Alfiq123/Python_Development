# Buatlah Class Diagram beserta kode program (Python) sesuai kasus berikut:

# Kasus Sederhana: Kebutuhan Pakan Ternak

#   1. `Peternakan` memiliki berbagai jenis `HewanTernak` (Kelas Induk).
#   2. `Sapi` dan `Kamabing` adalah jenis khusus dari `HewanTernak` (Inheritance).
#   3. Setiap `HewanTernak` memiliki kebutuhan `Pakan` sepesifik per hari.
#   4. Sebuah `Peternakan` memiliki (Mengelola) banyak `HewanTernak` (Aggregation).
#   5. Setiap `Pakan` terdiri dari beberapa `KomposisiPakan` (Misalnya: Jenis Serat, Protein, Mineral)

class Peternakan:
    __nama: str = str

    def get_peternakan(self):
        return self.__nama

    def set_peternakan(self, nama: str):
        self.__nama = nama


class HewanTernak:
    __nama: str = str
    __umur: int = int
    __berat: int = int

    # Nama
    @property
    def nama_hewan(self):
        return self.__nama

    @nama_hewan.setter
    def nama_hewan(self, nama: str):
        self.__nama = nama

    # Umur
    @property
    def umur_hewan(self):
        return self.__umur

    @umur_hewan.setter
    def umur_hewan(self, umur: int):
        self.__umur = umur

    # Berat
    @property
    def berat_hewan(self):
        return self.__berat

    @berat_hewan.setter
    def berat_hewan(self, berat: int):
        self.__berat = berat

    def kebutuhan_pakan_harian(self):
        pass


class Sapi(HewanTernak):
    def kebutuhan_pakan_harian(self):
        return self.berat_hewan * 0.03


class Kambing(HewanTernak):
    def kebutuhan_pakan_harian(self):
        return self.berat_hewan * 0.04


class KomposisiPakan:
    __jenis: str = str
    __jumlah: int = int


class Pakan:
    __nama: str = str
    __komposisi: list[str] = []

    @property
    def nama_pakan(self):
        return self.__nama

    @nama_pakan.setter
    def nama_pakan(self, nama: str):
        self.__nama = nama

    @property
    def komposisi_pakan(self):
        return self.__nama

    @komposisi_pakan.setter
    def komposisi_pakan(self, komposisi: list[str]):
        self.__komposisi = komposisi

    def tambah_komposisi(self, komposisi):
        self.__komposisi.append(komposisi)


if __name__ == "__main__":
    sapi_1 = Sapi()

    sapi_1.nama_hewan = "Ujang"
    sapi_1.umur_hewan = 10
    sapi_1.berat_hewan = 256

    print(
        f"Nama Hewan: {sapi_1.nama_hewan}\n"
        f"Umur Hewan: {sapi_1.umur_hewan}\n"
        f"Berat Hewan: {sapi_1.berat_hewan}\n"
        f"Kebutuhan Pakan: {sapi_1.kebutuhan_pakan_harian()}\n"
    )

    kambing_1 = Kambing()

    kambing_1.nama_hewan = "Ajar"
    kambing_1.umur_hewan = 5
    kambing_1.berat_hewan = 128

    print(
        f"Nama Hewan: {kambing_1.nama_hewan}\n"
        f"Umur Hewan: {kambing_1.umur_hewan}\n"
        f"Berat Hewan: {kambing_1.berat_hewan}\n"
        f"Kebutuhan Pakan: {kambing_1.kebutuhan_pakan_harian()}\n"
    )

    komp_1 = Pakan()

    print(komp_1.tambah_komposisi(komposisi="Protein"))
