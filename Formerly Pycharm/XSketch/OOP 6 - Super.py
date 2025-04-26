#  ___
# / __|_  _ _ __  ___ _ _
# \__ \ || | '_ \/ -_) '_|
# |___/\_,_| .__/\___|_|
#          |_|

# TODO: super() = Function used in a child class to call methods from a parent class (superclass).
#       Allow you to extend the functionality of the inherited methods.

# TODO: In Python, the super() function is used to call methods from a parent or sibling class in the context of
#       inheritance. It is particularly useful for accessing overridden methods in the parent class, allowing you
#       to extend or modify the behavior of inherited methods without completely rewriting them.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
            print(f"It is {self.color} and {'Filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)

        # self.color = color
        # self.filled = filled

        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {(22/7) * self.radius:.2f}cm²")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)

        # self.color = color
        # self.filled = filled

        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm²")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)

        # self.color = color
        # self.filled = filled

        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.height / 2}cm²")

circle = Circle("Green", True, 5)
square = Square("Blue", False, 12)
triangle = Triangle("Yellow", True, 7, 7)

circle.describe()
square.describe()
triangle.describe()

print()
print(f"Circle: \n  🔹 Color: {circle.color}\n  🔹 Filled: {circle.filled}\n  🔹 Radius: {circle.radius}cm\n")
print(f"Square: \n  🔹 Color: {square.color}\n  🔹 Filled: {square.filled}\n  🔹 Width: {square.width}cm\n")
print(f"Triangle: \n  🔹 Color: {triangle.color}\n  🔹 Filled: {triangle.filled}\n  🔹 Width: {triangle.width}cm\n  🔹 Height: {triangle.height}cm")
