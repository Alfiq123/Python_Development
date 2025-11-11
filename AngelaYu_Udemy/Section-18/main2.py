import turtle as t
import random as rn

# Initialize.
timmy = t.Turtle()
timmy.shape("turtle")

t.colormode(255)

def random_color():
    r = rn.randint(0, 255)
    g = rn.randint(0, 255)
    b = rn.randint(0, 255)
    return r, g, b

# colors = ("red", "green", "blue", "cyan", "magenta", "yellow", "black", "orange", "brown")
direction = (0, 90, 180, 270)

timmy.pensize(10)
timmy.speed(10)

for i in range(128):
    timmy.forward(30)
    timmy.setheading(rn.choice(direction))
    timmy.color(random_color())

screen = t.Screen()
screen.exitonclick()
