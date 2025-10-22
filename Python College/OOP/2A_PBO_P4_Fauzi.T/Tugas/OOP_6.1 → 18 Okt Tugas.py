# Soal 1: Sistem lahan pertanian

# Sebuah sistem sederhana diperlukan untuk mengelola berbagai jenis lahan pertanian.
# Semua lahan memiliki atribut dasar (luas dan lokasi) dan memerlukan operasi penanaman,
# cara penanaman dan pemeliharaannya berbeda sesuai jenis lahan.
# Output berupa informasi tentang tanaman yang ditanam di sawah dan lahan kering.

# 1. Kelas `Lahan` (Superkelas) memiliki atribut dan metode secara umum.
# 2. Kelas `Sawah` (Subkelas) diidentifikasi dengan jenis irigasinya dan memiliki metode penanaman spesifik untuk padi.
# 3. Kelas `KebunKering` (Subkelas) tidak memerlukan irigasi
#    dan memiliki metode penanaman spesifik untuk tanaman palawija.
# 4. Kelas `Sawah` dan `KebunKering` adalah kelas anak yang dibuat dengan mewarisi atribut
#    dan metode dari kelas induk (Lahan) menggunakan `super().__init__()`.
#    Kedua kelas anak ini memiliki `luasHektar` dan `lokasi` serta metode `panen()`tanpa harus mendefinisikannya ulang.

class Lahan:
    def __init__(self, luashektar, lokasi):
        self.luashektar = luashektar
        self.lokasi = lokasi

    def tanam(self):
        raise NotImplementedError(
            "Subclass harus mengimplementasikan metode `tanam()` ini"
        )

    def panen(self):
        return (f"Panen telah dilakukan di lahan seluas "
                f"|{self.luashektar}| hektar di |{self.lokasi}|")


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
    sawah_1 = Sawah(
        luashektar=16,
        lokasi="Desa SukaMundur",
        jenis_irigasi="Otomatis"
    )

    sawah_2 = Sawah(
        luashektar=24,
        lokasi="Desa TaniJaya",
        jenis_irigasi="Manual"
    )

    print(f"{sawah_1.tanam()}\n"
          f"{sawah_1.panen()}\n")

    print(f"{sawah_2.tanam()}\n"
          f"{sawah_2.panen()}\n")

    kebun_kering_1 = KebunKering(
        luashektar=32,
        lokasi="Desa MajuJaya"
    )

    kebun_kering_2 = KebunKering(
        luashektar=48,
        lokasi="Desa MundurMundur"
    )

    print(f"{kebun_kering_1.tanam()}\n"
          f"{kebun_kering_1.panen()}\n")

    print(f"{kebun_kering_2.tanam()}\n"
          f"{kebun_kering_2.panen()}\n")
