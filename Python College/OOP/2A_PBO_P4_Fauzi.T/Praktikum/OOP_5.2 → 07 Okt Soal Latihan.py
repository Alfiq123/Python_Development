# Soal 2: Laporan Kesehatan

# Buatlah kelas induk `TernakSehat` dengan metode `cek_kesehatan()`.
# Buat subclass `SapiPerah` dan `AyamPetelur` yang mengesampingkan
# metode tersebut untuk memberikan laporan kesehatan khusus.
# • `SapiPerah`: Cek produksi susu (normal jika liter/hari).
# • `AyamPetelur`: Cek jumlah telur (normal jika butir/hari).

# Tugas: Cetak laporan kesehatan untuk Sapi Perah (produksi 22 liter)
#        dan Ayam Petelur (produksi 0 butir).

class TernakSehat:
    def __init__(self): pass
    def cek_kesehatan(self): pass

class SapiPerah(TernakSehat):
    def __init__(self):
        super().__init__()

    # noinspection PyMethodOverriding
    def cek_kesehatan(self, liter):
        if liter <= 21:
            return (
                f"Sapi menghasilkan susu {liter} / hari, "
                f"Status Sapi: Tidak Sehat"
            )
        else:
            return (
                f"Sapi menghasilkan susu {liter} / hari, "
                f"Status Sapi: Sehat"
            )

class AyamPetelur(TernakSehat):
    def __init__(self):
        super().__init__()

    # noinspection PyMethodOverriding
    def cek_kesehatan(self, butir):
        if butir <= 0:
            return (
                f"Ayam menghasilkan telur {butir} / hari, "
                f"Status Ayam: Tidak Sehat"
            )
        else:
            return (
                f"Ayam menghasilkan telur {butir} / hari, "
                f"Status Ayam: Sehat"
            )

if __name__ == "__main__":
    sapi_1, sapi_2, sapi_3 = SapiPerah(), SapiPerah(), SapiPerah()
    ayam_1, ayam_2, ayam_3 = AyamPetelur(), AyamPetelur(), AyamPetelur()

    print(
        f"{sapi_1.cek_kesehatan(liter=24)}\n"
        f"{ayam_1.cek_kesehatan(butir=12)}\n"
        "\n"
        f"{sapi_2.cek_kesehatan(liter=10)}\n"
        f"{ayam_2.cek_kesehatan(butir=0)}\n"
        "\n"
        f"{sapi_3.cek_kesehatan(liter=32)}\n"
        f"{ayam_3.cek_kesehatan(butir=64)}\n"
    )
