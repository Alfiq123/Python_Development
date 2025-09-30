from random import randint

class Smartphone:
    def __init__(self, merk, model, warna, harga):
        self.merk = merk
        self.model = model
        self.warna = warna
        self.harga = harga
        self.daya_baterai = randint (20, 100)  # Nilai awal daya baterai adalah 100%

    def nyalakan (self):
        print("Menyalakan", self.merk, self.model)
        print("Daya baterai saat ini:", self.daya_baterai)

    def matikan (self):
        print("Mematikan", self.merk, self.model)

    def charge(self, persentase):
        self.daya_baterai += persentase

        if self.daya_baterai > 100:
            self.daya_baterai = 100
        print("Daya baterai setelah di-charge:", self.daya_baterai)

    def info(self):
        print("Smartphone {} {} ({}) - Harga: Rp.{}"
            .format(self.merk, self.model, self.warna, self.harga))

# Membuat objek-objek berdasarkan class Smartphone
hp1 = Smartphone("Samsung", "Galaxy F34", "Hijau", 3500000) 
hp2 = Smartphone("Huawei", "Y6p", "Ungu", 2800000)
hp3 = Smartphone("Realme", "GT Neo 3T", "Kuning", 5500000)

# Menggunakan metode pada objek
hp1.nyalakan(); hp1.charge(randint(20, 100)); hp1.info(); print("") 
hp2.nyalakan(); hp2.charge(randint(20, 100)); hp2.matikan(); print("") 
hp3.nyalakan(); hp3.charge(randint(20, 100)); hp3.info(); hp3.matikan()