#    _   _       _               _
#   /_\ | |__ __| |_ _ _ __ _ __| |_
#  / _ \| '_ (_-<  _| '_/ _` / _|  _|
# /_/ \_\_.__/__/\__|_| \__,_\__|\__|
#

# TODO: In Python, an abstract class is a class that cannot be instantiated on its own and is designed to be a
#     blueprint for other classes. It allows you to define a common interface or set of methods that must be
#     implemented by its subclasses. Abstract classes are useful for enforcing a structure in your code and
#     ensuring that certain methods are implemented in derived classes.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car!")

    def stop(self):
        print("You stop the car!\n")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle!")

    def stop(self):
        print("You stop the motorcycle!\n")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat!")

    def stop(self):
        print("You anchor the boat!")

car = Car()
motorcycle = Motorcycle()
boat = Boat()

car.go()
car.stop()

motorcycle.go()
motorcycle.stop()

boat.go()
boat.stop()
