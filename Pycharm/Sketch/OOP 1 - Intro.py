# Object.
class Car:

    # Constructor.
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}!")

    def stop(self):
        print(f"You stop the {self.color} {self.model}!\n")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car_1 = Car("Tesla", 2000, "Green", False)
car_2 = Car("Ferrari", 1998, "Blue", True)
car_3 = Car("Mustang", 1996, "Red", False)

# Attribute access operator.
print(f"Model: {car_1.model}\nYear: {car_1.year}\nColor: {car_1.color}\nSale: {car_1.for_sale}\n")
print(f"Model: {car_2.model}\nYear: {car_2.year}\nColor: {car_2.color}\nSale: {car_2.for_sale}\n")
print(f"Model: {car_3.model}\nYear: {car_3.year}\nColor: {car_3.color}\nSale: {car_3.for_sale}\n")

car_1.drive()
car_1.stop()

car_2.drive()
car_2.stop()

car_3.drive()
car_3.stop()

car_1.describe()
car_2.describe()
car_3.describe()