# Contoh0703.py

from OOP_22 import Bentuk
from OOP_22 import Persegi
from OOP_22 import PersegiPanjang

# Membuat objek dari superclass dan subclass
bentuk_umum = Bentuk()
square = Persegi("Persegi ABCD", 5)
rectangle = PersegiPanjang("Persegi Panjang EFGH", 10, 8)

# Memanggil metode hitungLuas, hitungKeliling dan info dari tiap objek
bentuk_umum.hitungLuas()
bentuk_umum.hitungKeliling()
bentuk_umum.info()
print("")

square.hitungLuas()
square.hitungKeliling()
square.info()
print("")

rectangle.hitungLuas()
rectangle.hitungKeliling()
rectangle.info()
