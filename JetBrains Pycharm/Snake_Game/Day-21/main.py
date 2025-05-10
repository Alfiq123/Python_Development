
# ══════════ Inheritance ══════════ #

class Animal:
    def __init__(self):
        self.num_eye = 2

    def breathe(self):
        print("inhale, Exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing something underwater")

    def swim(self):
        print("Moving in Water")

whale = Fish()
whale.swim()
whale.breathe()
