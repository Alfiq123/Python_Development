# Contoh0702.py

class Bentuk:
    _nama = _luas = _keliling = None
    
    # definisi setter & getter
    def setNama(self, nm): self._nama = nm

    def getNama(self): return self._nama
    
    def setLuas(self, luas): self._luas = luas
        
    def getLuas(self): return self._luas
    
    def setKeliling(self, keliling): self._keliling = keliling
        
    def getKeliling(self): return self._keliling
    
    # definisi method Lainnya
    def hitungLuas(self):
        print("hitungLuas bentuk ini belum diimplementasikan.")
        
    def hitungKeliling(self):
        print("hitungKeliling bentuk ini belum diimplementasikan.")
        
    def info(self):
        print("\nNama bangun :", self._nama)
        print("→ Luas      :", self._luas)
        print("→ Keliling  :", self._keliling)


class Persegi(Bentuk):
    def __init__(self, nama, sisi):
        super().setNama(nama)
        self.sisi = sisi
        
    # overriding metode hitungLuas dari superclass
    def hitungLuas(self):
        super().setLuas(self.sisi ** 2)
        print(f"→ Luas {super().getNama()} : {super().getLuas()}")
        
    # overriding metode hitungKeliling dari superclass
    def hitungKeliling(self):
        super().setKeliling(self.sisi * 4)
        print(f"→ Keliling {super().getNama()} : {super().getKeliling()}")


class PersegiPanjang(Bentuk):
    def __init__(self, nama, panjang, lebar):
        super().setNama(nama)
        self.panjang = panjang
        self.lebar = lebar
        
    # overriding metode hitungLuas dari superclass
    def hitungLuas(self):
        super().setLuas(self.panjang * self.lebar)
        print(super().getNama(), "→ Luas :", super().getLuas())
        
    # overriding metode hitungKeliling dari superclass
    def hitungKeliling(self):
        super().setKeliling(2 * (self.panjang + self.lebar))
        print(super().getNama(), "→ Keliling :", super().getKeliling())