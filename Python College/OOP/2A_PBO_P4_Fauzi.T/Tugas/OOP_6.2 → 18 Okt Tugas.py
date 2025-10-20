# Soal 2: Kasus Kebutuhan Pakan Ternak

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
        print(f"\n═════ Peternakan: {self.nama} ═════")
        for nomor, hewan in enumerate(self.daftar_hewan, start=1):
            print(f"{nomor}. {hewan.hitung_kebutuhan_pakan()}")


class HewanTernak:
    def __init__(self, nama, berat_badan, pakan):
        self.nama = nama
        self.berat_badan = berat_badan
        self.pakan = pakan

    def hitung_kebutuhan_pakan(self):
        raise NotImplementedError(
            "Error: Harus diimplementasikan di Subclass!"
        )


class Sapi(HewanTernak):
    def __init__(self, nama, berat_badan, pakan):
        super().__init__(nama, berat_badan, pakan)

    def hitung_kebutuhan_pakan(self):
        hijauan = self.berat_badan * 0.10
        konsentrat = self.berat_badan * 0.02

        komposisi_str = '\n'.join([
            f"       • {komp.jenis}: {komp.persentase}%"
            for komp in self.pakan.komposisi
        ])

        return (
            f"Kebutuhan Pakan Sapi |{self.nama}| "
            f"dengan berat |{self.berat_badan:,}| Kg:\n"
            f"    • Hijauan: |{hijauan:,.2f}| Kg / Hari\n"
            f"    • Konsentrat: |{konsentrat:,.2f}| Kg / Hari\n"
            f"    • Jenis Pakan: |{self.pakan.nama}| dengan komposisi:"
            f"\n{komposisi_str}"
        )


class Kambing(HewanTernak):
    def __init__(self, nama, berat_badan, pakan):
        super().__init__(nama, berat_badan, pakan)

    def hitung_kebutuhan_pakan(self):
        hijauan = self.berat_badan * 0.08
        konsentrat = self.berat_badan * 0.01

        komposisi_str = '\n'.join([
            f"       • {komp.jenis}: {komp.persentase}%"
            for komp in self.pakan.komposisi
        ])

        return (
            f"Kebutuhan Pakan Kambing |{self.nama}| "
            f"dengan berat |{self.berat_badan:,}| Kg:\n"
            f"    • Hijauan: |{hijauan:,.2f}| Kg / Hari\n"
            f"    • Konsentrat: |{konsentrat:,.2f}| Kg / Hari\n"
            f"    • Jenis Pakan: |{self.pakan.nama}| dengan komposisi:"
            f"\n{komposisi_str}"
        )


class KomposisiPakan:
    def __init__(self, jenis, persentase):
        self.jenis = jenis
        self.persentase = persentase


class Pakan:
    def __init__(self, nama):
        self.nama = nama
        self.komposisi = []

    def tambah_komposisi(self, komposisi):
        self.komposisi.append(komposisi)

    def tampilkan_komposisi(self):
        print(f"\nKomposisi Pakan |{self.nama}|")
        for komp in self.komposisi:
            print(f" • {komp.jenis}: {komp.persentase}%")


if __name__ == "__main__":
    # Pakan Sapi
    pakan_sapi = Pakan("Sapi Premium")
    pakan_sapi.tambah_komposisi(KomposisiPakan(jenis="Serat",
                                               persentase=60))
    pakan_sapi.tambah_komposisi(KomposisiPakan(jenis="Protein",
                                               persentase=30))
    pakan_sapi.tambah_komposisi(KomposisiPakan(jenis="Mineral",
                                               persentase=10))
    pakan_sapi.tampilkan_komposisi()

    # Pakan Kambing
    pakan_kambing = Pakan("Kambing Golden")
    pakan_kambing.tambah_komposisi(KomposisiPakan(jenis="Serat",
                                                  persentase=50))
    pakan_kambing.tambah_komposisi(KomposisiPakan(jenis="Protein",
                                                  persentase=25))
    pakan_kambing.tambah_komposisi(KomposisiPakan(jenis="Mineral",
                                                  persentase=25))
    pakan_kambing.tampilkan_komposisi()

    # Peternakan 1
    peternakan_1 = Peternakan(nama="Chain Reaction")

    sapi_1_1 = Sapi(nama="Zephyr",
                    berat_badan=1847,
                    pakan=pakan_sapi)
    sapi_1_2 = Sapi(nama="Optical",
                    berat_badan=1714,
                    pakan=pakan_sapi)
    kambing_1_1 = Kambing(nama="Izuaf",
                          berat_badan=128,
                          pakan=pakan_kambing)
    kambing_1_2 = Kambing(nama="Canary",
                          berat_badan=77,
                          pakan=pakan_kambing)

    peternakan_1.tambah_hewan(hewan=sapi_1_1)
    peternakan_1.tambah_hewan(hewan=sapi_1_2)
    peternakan_1.tambah_hewan(hewan=kambing_1_1)
    peternakan_1.tambah_hewan(hewan=kambing_1_2)

    peternakan_1.tampilkan_kebutuhan_pakan()

    # Peternakan 2
    peternakan_2 = Peternakan(nama="Apa Saja Bisa")

    sapi_2_1 = Sapi(nama="Ankita",
                    berat_badan=1393,
                    pakan=pakan_sapi)
    sapi_2_2 = Sapi(nama="Michail",
                    berat_badan=1558,
                    pakan=pakan_sapi)
    kambing_2_1 = Kambing(nama="Ivailo",
                          berat_badan=40,
                          pakan=pakan_kambing)
    kambing_2_2 = Kambing(nama="Giovanni",
                          berat_badan=57,
                          pakan=pakan_kambing)

    peternakan_2.tambah_hewan(hewan=sapi_2_1)
    peternakan_2.tambah_hewan(hewan=sapi_2_2)
    peternakan_2.tambah_hewan(hewan=kambing_2_1)
    peternakan_2.tambah_hewan(hewan=kambing_2_2)

    peternakan_2.tampilkan_kebutuhan_pakan()
