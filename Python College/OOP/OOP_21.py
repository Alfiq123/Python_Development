# Contoh0701.py

class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
    
    def infoKendaraan(self):
        return f"{self.merk} {self.tahun}"

class Mobil(Kendaraan):
    def __init__(self, merk, tahun, model, warna):
        super().__init__(merk, tahun)
        self.model = model
        self.warna = warna
    
    def infoMobil(self):
        return (
            f"{self.merk} {self.model} "
            f"Warna {self.warna} "
            f"Tahun {self.tahun}"
        )

kendaraan1 = Kendaraan("Toyota", 2022)
mobil1 = Mobil("Honda", 2022, "Mobilio", "Merah")
mobil2 = Mobil("Suzuki", 2021, "Ertiga", "Silver")
mobil3 = Mobil("Daihatsu", 2023, "Xenia", "Hitam")

print("kendaraan1.infoKendaraan() :", kendaraan1.infoKendaraan())
print("mobil1.infoKendaraan() :", mobil1.infoKendaraan())
print("mobil1.infoMobil() :", mobil1.infoMobil())
print("mobil2.infoKendaraan() :", mobil2.infoKendaraan())
print("mobil2.infoMobil() :", mobil2.infoMobil())
print("mobil3.infoKendaraan() :", mobil3.infoKendaraan())
print("mobil3.infoMobil() :", mobil3.infoMobil())
