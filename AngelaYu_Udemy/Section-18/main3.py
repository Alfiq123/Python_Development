import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

n = 36  # Number of circles
h = 0  # Hue value

for i in range(n):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    t.circle(100)  # Draw a circle
    t.right(10)  # Slight turn for rotation effect
    h += 1/n

turtle.done()
