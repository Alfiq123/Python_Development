# Soal 2: Kasus: Kebutuhan Pakan Ternak

# 1. `Peternakan` memiliki berbagai jenis `HewanTernak` (kelas induk).
# 2. `Sapi` dan `Kambing` adalah jenis khusus dari `HewanTernak` (Inheritance).
# 3. Setiap `HewanTernak` memiliki kebutuhan `Pakan` spesifik per hari.
#     - Misalkan kebutuhan pakan sapi harian terdiri dari pakan hijauan (10% dari berat badan) dan pakan konsentrat (2% dari berat badan).
#     - Sedangkan kebutuhan pakan harian kambing terdiri dari pakan hijauan (8% dari berat badan) dan pakan konsentrat (1% dari berat badan)
# 4. Sebuah `Peternakan` memiliki (mengelola) banyak `HewanTernak` (Aggregation).
#    Setiap `Pakan` terdiri dari beberapa `KomposisiPakan` (Misalnya: jenis serat, protein, mineral)

class Peternakan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_hewan = []

    def tambah_hewan(self, hewan):
        self.daftar_hewan.append(hewan)

    def tampilkan_kebutuhan_pakan(self):
        for hewan in self.daftar_hewan:
            print(hewan.hitung_kebutuhan_pakan())


class HewanTernak:
    def __init__(self, nama, berat_badan):
        self.nama = nama
        self.berat_badan = berat_badan

    def hitung_kebutuhan_pakan(self):
        raise NotImplementedError("Error: Harus diimplementasikan di Subclass!")


class Sapi(HewanTernak):
    def __init__(self, nama, berat_badan):
        super().__init__(nama, berat_badan)

    def hitung_kebutuhan_pakan(self):
        hijauan = self.berat_badan * 0.10
        konsentrat = self.berat_badan * 0.02
        return (
            f"Kebutuhan Pakan Sapi |{self.nama}|:" + "\n"
            f" • Hijauan |{hijauan:,.2f}| Kg / Hari" + "\n"
            f" • Konsentrat |{konsentrat:,.2f}| Kg / Hari" + "\n"
        )


class Kambing(HewanTernak):
    def __init__(self, nama, berat_badan):
        super().__init__(nama, berat_badan)

    def hitung_kebutuhan_pakan(self):
        hijauan = self.berat_badan * 0.08
        konsentrat = self.berat_badan * 0.01
        return (
            f"Kebutuhan Pakan Kambing |{self.nama}|:\n"
            f" • Hijauan |{hijauan:,.2f}| Kg / Hari\n"
            f" • Konsentrat |{konsentrat:,.2f}| Kg / Hari\n"
        )


class KomposisiPakan:
    def __init__(self, jenis, persentase):
        self.jenis = jenis
        self.persentase = persentase


class Pakan:
    def __init__(self):
        self.komposisi = []


if __name__ == "__main__":
    peternakan_1 = Peternakan(nama="Chain Reaction")
    peternakan_2 = Peternakan(nama="Apa Saja Bisa")

    sapi_1_1 = Sapi(nama="Zephyr", berat_badan=1847)
    sapi_1_2 = Sapi(nama="Optical", berat_badan=1714)
    kambing_1_1 = Kambing(nama="Izuaf", berat_badan=128)
    kambing_1_2 = Kambing(nama="Canary", berat_badan=77)

    sapi_2_1 = Sapi(nama="Ankita", berat_badan=1393)
    sapi_2_2 = Sapi(nama="Michail", berat_badan=1558)
    kambing_2_1 = Kambing(nama="Ivailo", berat_badan=40)
    kambing_2_2 = Kambing(nama="Giovanni", berat_badan=57)

    peternakan_1.tambah_hewan(hewan=sapi_1_1)
    peternakan_1.tambah_hewan(hewan=sapi_1_2)
    peternakan_1.tambah_hewan(hewan=kambing_1_1)
    peternakan_1.tambah_hewan(hewan=kambing_1_2)

    peternakan_2.tambah_hewan(hewan=sapi_2_1)
    peternakan_2.tambah_hewan(hewan=sapi_2_2)
    peternakan_2.tambah_hewan(hewan=kambing_2_1)
    peternakan_2.tambah_hewan(hewan=kambing_2_2)

    peternakan_1.tampilkan_kebutuhan_pakan()
    peternakan_2.tampilkan_kebutuhan_pakan()
