from abc import ABC, abstractmethod
from math import pi


class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "Hewan bersuara"


class Anjing(Hewan):
    def suara(self):  # Override method dari parent
        return "Guk guk!"


class Kucing(Hewan):
    def suara(self):  # Override method dari parent
        return "Meow!"


class Sapi(Hewan):
    def suara(self):  # Override method dari parent
        return "Mooo!"


class Mobil:
    @staticmethod
    def start():
        return "Mesin mobil menyala"


class Motor:
    @staticmethod
    def start():
        return "Mesin motor menyala"


class Perahu:
    @staticmethod
    def start():
        return "Mesin perahu menyala"


# Function yang polymorphic
def operasikan_kendaraan(kendaraan):
    print(kendaraan.start())


class Apple:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def __add__(self, other):
        return Apple(jumlah=self.jumlah + other.jumlah)

    def __sub__(self, other):
        return Apple(jumlah=self.jumlah - other.jumlah)

    def __str__(self):
        return f"Apple: {self.jumlah}"


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


if __name__ == "__main__":
    # Polymorphism in action
    hewan_list = [
        Anjing(nama="Buddy"),
        Kucing(nama="Whiskers"),
        Sapi(nama="Bessie")
    ]

    # Polymorphism dengan duck typing
    kendaraan_list = [
        Mobil(),
        Motor(),
        Perahu()
    ]

    shape = [
        Rectangle(length=5, width=3),
        Circle(2)
    ]

    # Method yang sama, behavior berbeda
    for hewan in hewan_list:
        print(hewan.suara())

    for kendaraan in kendaraan_list:
        operasikan_kendaraan(kendaraan)

    for s in shape:
        print(f"Area is {s.area()}")

    apple_1 = Apple(jumlah=5)
    apple_2 = Apple(jumlah=3)

    print(apple_1 + apple_2)
    print(apple_1 - apple_2)
