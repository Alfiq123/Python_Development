# import turtle as t
import time

from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width = 1080, height = 1080)
screen.bgcolor("black")
screen.title("Udemy Snake Game")
screen.tracer(False)

# * Snake Object
snake = Snake()


# TODO 1: Create a Snake Body.
## // Move to snake.py

# TODO 3: Control the Snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


# TODO 2: Move The Snake.
## // Move to snake.py
while True:
    screen.update()
    time.sleep(0.05)

    snake.move()


screen.mainloop()
# screen.exitonclick()
