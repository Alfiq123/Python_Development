import turtle
import random

turtle.colormode(255)
turtle.bgcolor("black")

tim = turtle.Turtle()
tim.speed(0)

for i in range(36):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.circle(100)
    tim.right(10)

screen = turtle.Screen()
screen.exitonclick()
