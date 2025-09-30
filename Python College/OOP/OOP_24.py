# Contoh0704.py

class Hewan:
    def suara(self):
        return "\nHewan umumnya bersuara."

class Anjing(Hewan):
    def suara(self): # overriding metode suara dari superclass
        return "  • Anjing menggonggong."

class Kucing(Hewan):
    def suara(self): # overriding metode suara dari superclass
        return "  • Kucing mengeong.\n"

# Contoh pemanggilan metode suara dari objek-objek
hewan_umum = Hewan()
dog = Anjing()
cat = Kucing()

print(hewan_umum.suara(), dog.suara(), cat.suara(), sep='\n')
