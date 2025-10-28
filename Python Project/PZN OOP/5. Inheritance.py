class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Merek: {self.merk}, Tahun: {self.tahun}"

    def nyalakan(self):
        print(f"{self.merk} dinyalakan...")


# Class Child: Mobil
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_roda):
        super().__init__(merk, tahun)
        self.jumlah_roda = jumlah_roda

    def klakson(self):
        print(f"Mobil {self.info()} memiliki klakson besar")


# Class Child: Motor
class Motor(Kendaraan):
    def klakson(self):
        print(f"Motor {self.info()} memiliki klakson kecil")

    def nyalakan(self):
        # Jika ingin menggunakan method `nyalakan` dari parent class
        # `super().nyalakan`
        print(f"Motor {self.merk} dinyalakan secara otomatis...")


class Pesawat(Kendaraan):
    pass


class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji


class KaryawanTetap(Karyawan):
    pass


class Manager(KaryawanTetap):
    pass


class VicePresident(Manager):
    pass


class Designer(Karyawan):
    pass


class Developer(Karyawan):
    pass


class BisaBerenang:
    @staticmethod
    def berenang():
        print("Bisa berenang")


class BisaBerlari:
    @staticmethod
    def berlari():
        print("Bisa berlari")


class Atlit(BisaBerenang, BisaBerlari):
    def __init__(self, nama):
        self.nama = nama


# Diamond Problem
class A:
    def method(self):
        return "Method from A"


class B(A):
    def method(self):
        return "Method from B"


class C(A):
    def method(self):
        return "Method from C"


class D(B, C):
    pass


if __name__ == "__main__":
    avanza = Mobil(merk="Avanza", tahun=2019, jumlah_roda=4)
    avanza.nyalakan()
    avanza.klakson()
    print(avanza.jumlah_roda)

    print()

    scoopy = Motor(merk="Scoopy", tahun=2018)
    scoopy.nyalakan()
    scoopy.klakson()

    print()

    eko = Atlit("Eko")
    eko.berenang()
    eko.berlari()

    print()

    d = D()

    print(d.method())
    print()
    print(D.__mro__)
    print()

    ekod = Karyawan(nama="Eko", gaji=1000000)
    tono = KaryawanTetap(nama="Tono", gaji=1000000)
    budi = Manager(nama="Budi", gaji=1000000)
    joko = VicePresident(nama="Joko", gaji=1000000)

    print(isinstance(ekod, Karyawan))  # True
    print(isinstance(tono, Karyawan))  # True
    print(isinstance(budi, Karyawan))  # True
    print(isinstance(joko, Karyawan))  # True
