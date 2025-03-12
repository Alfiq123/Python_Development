#   ___        _               _  _
#  |_ _| _ _  | |_   ___  _ _ (_)| |_  __ _  _ _   __  ___
#   | | | ' \ | ' \ / -_)| '_|| ||  _|/ _` || ' \ / _|/ -_)
#  |___||_||_||_||_|\___||_|  |_| \__|\__,_||_||_|\__|\___|
#

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEAK!")

dog = Dog("Scooby")
cat = Cat("Asteroid")
mouse = Mouse("Mice")

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()

print()

cat.speak()
dog.speak()
mouse.speak()
