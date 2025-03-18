#  __  __      _ _   _      _       ___      _            _ _
# |  \/  |_  _| | |_(_)_ __| |___  |_ _|_ _ | |_  ___ _ _(_) |_ __ _ _ _  __ ___
# | |\/| | || | |  _| | '_ \ / -_)  | || ' \| ' \/ -_) '_| |  _/ _` | ' \/ _/ -_)
# |_|  |_|\_,_|_|\__|_| .__/_\___| |___|_||_|_||_\___|_| |_|\__\__,_|_||_\__\___|
#                     |_|

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunt")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Deadeye")
hawk = Hawk("Hank")
fish = Fish("Relentless")

rabbit.flee()
rabbit.eat()
