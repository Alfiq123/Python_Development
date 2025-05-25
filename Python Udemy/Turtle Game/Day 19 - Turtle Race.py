from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(
    title="Enter your choice",
    prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    sleeper = Turtle(shape="turtle")
    sleeper.color(colors[turtle_index])
    sleeper.penup()
    sleeper.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(sleeper)

is_race_on = False

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner"
                      "!")

screen.exitonclick()
