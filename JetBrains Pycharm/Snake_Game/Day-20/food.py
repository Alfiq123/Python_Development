from turtle import Turtle
from random import randint

# TODO: Detect collision with food.
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("green")
        self.speed("fastest")
        self.change_position()

    def change_position(self):
        random_x = randint(a = -280, b = 280)
        random_y = randint(a = -280, b = 280)
        self.goto(random_x, random_y)
