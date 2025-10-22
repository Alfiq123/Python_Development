import turtle as t
from random import choice

# Initialize.
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")

# # 1. Triangle.
# for i in range(3):
#     timmy.forward(100)
#     timmy.right(120)
# 
# # 2. Square.
# for i in range(4):
#     timmy.forward(100)
#     timmy.color("#2F4F4F") # Change Color.
#     timmy.right(90)
# 
# # 3. Pentagon.
# for i in range(5):
#     timmy.forward(100)
#     timmy.color("#00CED1") # Change Color.
#     timmy.right(72)
# 
# # 4. Hexagon.
# for i in range(6):
#     timmy.forward(100)
#     timmy.color("#008000") # Change Color.
#     timmy.right(60)
# 
# # 5. Heptagon.
# for i in range(7):
#     timmy.forward(100)
#     timmy.color("#FFD700") # Change Color.
#     timmy.right(360 / 7)
# 
# # 6. Octagon.
# for i in range(8):
#     timmy.forward(100)
#     timmy.color("#7FFF00") # Change Color.
#     timmy.right(45)
# 
# # 7. Nonagon.
# for i in range(9):
#     timmy.forward(100)
#     timmy.color("medium blue") # Change Color.
#     timmy.right(360 / 9)
# 
# # 8. Decagon.
# for i in range(10):
#     timmy.forward(100)
#     timmy.color("light slate blue") # Change Color.
#     timmy.right(360 / 10)

# Actual Answer.
colors = ["royal blue", "light sea green", "beige", "linen", "snow", "dark green", "gray", "aquamarine"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    timmy.color(choice(colors))
    draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()
