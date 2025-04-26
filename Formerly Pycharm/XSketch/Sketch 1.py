class Zombie:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self):
        print("Zombie attacks and deals", self.damage, "damage!")

# Creating Zombie objects (instances)
zombie1 = Zombie(health = 20, damage = 3)
zombie2 = Zombie(health = 25, damage = 5)

zombie1.attack()  # Output: Zombie attacks and deals 3 damage!
zombie2.attack()  # Output: Zombie attacks and deals 5 damage!

class Husk(Zombie):  # Husk inherits from Zombie
    def __init__(self, health, damage):
        super().__init__(health, damage)  # Reuse Zombie's properties

    def attack(self):
        print("Husk attacks and deals", self.damage, "damage! Also inflicts hunger.")

# Creating a Husk object
husk1 = Husk(health = 30, damage = 4)
husk1.attack()  # Output: Husk attacks and deals 4 damage! Also inflicts hunger.

class Creeper:
    def __init__(self, explosion_timer):
        self.__explosion_timer = explosion_timer  # Private attribute

    def get_timer(self):
        return self.__explosion_timer  # Controlled access

creeper1 = Creeper(5)
print(creeper1.get_timer())  # Output: 5
# print(creeper1.__explosion_timer)  # This would cause an error!
