from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(x = 0, y = 260)
        self.update_score()

    def update_score(self):
        self.write(arg = f"Score: {self.score}", move = False, align = "center", font = ("Courier", 24, "normal"))

    def game_over(self):
        self.color("red")
        self.goto(x = 0, y = 0)
        self.write(arg = f"GAME OVER", move = False, align = "center", font = ("Courier", 24, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
