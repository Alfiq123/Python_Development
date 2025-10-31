# * 🡣 Membuat **Class**.
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ! Kalau menggunakan **list** kodenya akan susah dibaca.
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]


# * Contoh: Kelas - Anjing.
class DogPark:
    species = "Toy Group"  # 🡠 Class Attributes / Atribut Kelas.

    def __init__(self, name, age):  # 🡠 `.__init__()` Digunakan untuk inisialisasi objek.
        """ 🡢 Kode ini disebut: **Instance Attributes** 🡠 """
        self.name = name  # // Attributes / Atribut
        self.age = age  # // Attributes / Atribut


# Membuat object baru dari class disebut **instantiating**.
## * Cara menggunakannya 🡣:
### Dog()  # ! Kode ini akan menghasilkan error.


# * Versi benarnya 🡣:
chihuahua = DogPark(name="Chihuahua", age=4)  # 🡠 Keyword Argument.
pomeranian = DogPark(name="Pomeranian", age=9)  # 🡠 Keyword Argument.

# * Cara mengakses atribbut di atas 🡩:
## * Pastikan menggunakan 🡢 . 🡠

# - Chihuahua - #
print(
    f"Dog Name: {chihuahua.name}\n"
    f"Dog Age: {chihuahua.age}\n"
)

# - Pomeranian - #
print(
    f"Dog Name: {pomeranian.name}\n"
    f"Dog Age: {pomeranian.age}\n"
)

# * Class Attribute dapat diakses dengan cara:
print(
    f"Dog Species: {chihuahua.species}\n"
    f"Dog Species: {pomeranian.species}\n"
)

# * `Value` di `Attribute` dapat juga diganti:
chihuahua.age = 12
pomeranian.age = 14

chihuahua.species = "Hound Group"
pomeranian.species = "Sporting Group"

print("══════════ Value Changes ══════════\n")

print(
    f"Dog Name: {chihuahua.name}\n"
    f"Dog Age: {chihuahua.age}\n"
)

print(
    f"Dog Name: {pomeranian.name}\n"
    f"Dog Age: {pomeranian.age}\n"
)

print(
    f"Dog Species: {chihuahua.species}\n"
    f"Dog Species: {pomeranian.species}\n"
)


# Instance Methods.
## ? `Function` yang dibuat di dalam `Class` dan
## ?    hanya bisa terpanggil dari `Class` tersebut.

class Cat:
    """ 🡢 Kelas Khusus Kucing 🡠 """
    species = "Felis Catus"

    def __init__(self, name, age):
        """ 🡢 Spesies Kucing 🡠 """
        self.name = name
        self.age = age

    # * Instance Methods
    def description(self):
        return f"{self.name} is {self.age} years old"

    # * Instance Methods yang lain.
    def speak(self, sound):
        return f"{self.name} says {sound}"


print("══════════ Cat Zone ══════════\n")

persian = Cat(name="Persian", age=2)

print(
    persian.description() + "\n"
    + persian.speak(sound="Meow Meow") + "\n"
    + persian.speak(sound="Hiss Hiss") + "\n"
)


# ? Output ini tidak membantu sama sekali 🡣
# print(persian)

# * Tapi kita bisa mengakalinya 🡣
class Lion:
    species = "Panthera Leo"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


leon = Lion(name="Leo", age=20)
print(leon, "\n")


# ════════════════════ Exercise ════════════════════ #


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"


car_blue = Car(color="Blue", mileage=20000)
car_red = Car(color="Red", mileage=30000)

print(
    f"{car_blue}\n"
    f"{car_red}\n"
)


# ════════════════════ Inheritance ════════════════════ #


# * Inheritance / Pewarisan.
# ? Proses di mana suatu `class` mengambil
# ? `attributes` dan metode dari `class` lain.


# * Contoh 🡣:
class Parent:
    hair_color = "Brown"


class Child(Parent):  # ? 🡠 Inheritance
    pass


# * `Child` class juga dapat men-**override** atau men-**extend**―
# * `attributes` dari `class` induk / utama.


# * Contoh - Override 🡣:
class Parent:
    hair_color = "Brown"


class Child(Parent):
    hair_color = "Purple"  # ? 🡠 Overridden
    # // Output: Purple


# * Contoh - Extend 🡣:
class ParentB:
    speaks = ["English"]


class ChildB(ParentB):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")  # ? 🡠 Extend
        # // Output: ["English", "German"]


# ══════════ Example: Dog Park ══════════ #


class DogPark:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# ! Code has Changed.
# miles = DogPark("Miles", 4, "Jack Russell Terrier")
# buddy = DogPark("Buddy", 9, "Dachshund")
# jack = DogPark("Jack", 3, "Bulldog")
# jim = DogPark("Jim", 5, "Bulldog")


# ══════════ Parent Class vs Child Class ══════════ #


class DogB:  # ? 🡠 Parent Class
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


# ! Changed
# class JackRussellTerrier(DogB):  # ? 🡠 Child Class
# def speak(self, sound="Arf"):  # ? 🡠 Default Argument
# return f"{self.name} says {sound}"


# * Menggunakan `super()` untuk memanggil metode dari `class` induk.
class JackRussellTerrier(DogB):
    def speak(self, sound="Arf"):  # ? 🡠 super()
        return super().speak(sound)


class Dachshund(DogB):  # 🡠 Child Class
    pass


class Bulldog(DogB):  # 🡠 Child Class
    pass


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(
    f"{miles.species}\n"
    f"{miles.speak()}\n"
    f"{miles.speak('Grrr')}\n"  # ? 🡠 Overridding the Sound.
    f"{buddy.name}\n"
    f"{jack}\n"
    f"{jim.speak('Woof')}\n"
)

# * Untuk menentukan `class` mana yang dimiliki―
# * Objek tertentu, gunakan `type()`.
type(miles)  # // Output: <class '__main__.JackRussellTerrier'>

# * Gunakan `isinstance()` untuk menentukan apakah―
# * suatu objek merupakan *instance* dari suatu `class`.
isinstance(miles, DogB)  # // Output: True
isinstance(miles, Bulldog)  # // Output:  False
isinstance(jack, Dachshund)  # // Output:  False


# ════════════════════ Exercise 2 ════════════════════ #


class DogC:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(DogC):
    def speak(self, sound="Bark"):
        return super().speak(sound)
