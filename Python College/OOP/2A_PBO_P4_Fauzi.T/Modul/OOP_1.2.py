class Hitung:
    angka1, angka2 = 0, 0

    def jumlah_static(bill, bil2): 
        return bill + bil2
    
    def kali_static(bill, bil2): 
        return bill * bil2
    
    def __init__(self, A, B):
        self.angkal = A
        self.angka2 = B
        
    def jumlah(self):
        return self.angkal + self.angka2 
    
    def kali(self):
        return self.angkal * self.angka2

hasil1 = Hitung.jumlah_static(10, 20)
hasil2 = Hitung.kali_static(3, 7)
print("10 + 20 =", hasil1, "\n3 * 7 =", hasil2)

objHitung = Hitung(5, 7)
print("5 + 7 =", objHitung.jumlah(), "\n5 * 7 =", objHitung.kali())
