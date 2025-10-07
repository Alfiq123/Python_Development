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

    def cek_kesehatan(self, *args): pass


class SapiPerah(TernakSehat):
    def __init__(self):
        super().__init__()

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
    sapi = [SapiPerah() for _ in range(6)]
    ayam = [AyamPetelur() for _ in range(6)]

    print(
        f"{sapi[0].cek_kesehatan(liter=24)}\n"
        f"{ayam[0].cek_kesehatan(butir=12)}\n"
        "\n"
        f"{sapi[1].cek_kesehatan(liter=10)}\n"
        f"{ayam[1].cek_kesehatan(butir=0)}\n"
        "\n"
        f"{sapi[2].cek_kesehatan(liter=32)}\n"
        f"{ayam[2].cek_kesehatan(butir=64)}\n"
    )
