class Kampus:
    nama: str = str
    alamat: str = str
    kota: str = str


class Mahasiswa:
    nim: int = int
    nama: str = str

    def perkenalan(self):
        return f"Halo, nama saya |{self.nama}|"

    def hello(self, nama: str):
        return f"Halo {nama}, nama saya {self.nama}"


class Mobil:
    nama: str = str
    warna: str = str
    merk: str = str


if __name__ == "__main__":
    kampus_1 = Kampus()
    kampus_1.nama = "Universitas Brawijaya"
    kampus_1.kota = "Malang"

    kampus_2 = Kampus()
    kampus_2.nama = "Universitas Gajah Mada"
    kampus_2.kota = "Yogyakarta"

    mahasiswa_1 = Mahasiswa()
    mahasiswa_1.nim = 123456
    mahasiswa_1.nama = "Arya"

    mahasiswa_2 = Mahasiswa()
    mahasiswa_2.nim = 789012
    mahasiswa_2.nama = "Budi"

    Mobil.nama = "SUV WR-V,"
    Mobil.warna = "Putih"
    Mobil.merk = "Mobil Bagus"

    print(
        f"Tipe: {type(kampus_1)}\n"
        f"Tipe: {type(kampus_2)}\n"
        "\n"
        f"Tipe: {type(mahasiswa_1)}\n"
        f"Tipe: {type(mahasiswa_2)}\n"
    )

    print(
        f"Nama Kampus: {kampus_1.nama}\n"
        f"Kota Kampus: {kampus_1.kota}\n"
        "\n"
        f"Nama Kampus: {kampus_2.nama}\n"
        f"Kota Kampus: {kampus_2.kota}\n"
    )

    print(
        f"NIM Mahasiswa: {mahasiswa_1.nim}\n"
        f"Nama Mahasiswa: {mahasiswa_1.nama}\n"
        f"{mahasiswa_1.perkenalan()}\n"
        f"{mahasiswa_1.hello(nama='Diki')}\n"
        "\n"
        f"NIM Mahasiswa: {mahasiswa_2.nim}\n"
        f"Nama Mahasiswa: {mahasiswa_2.nama}\n"
        f"{mahasiswa_2.perkenalan()}\n"
        f"{mahasiswa_2.hello(nama='Intan')}\n"
    )

    print(
        f"Nama Mobil: {Mobil.nama}\n"
        f"Warna Mobil: {Mobil.warna}\n"
        f"Merk Mobil: {Mobil.merk}\n"
    )
