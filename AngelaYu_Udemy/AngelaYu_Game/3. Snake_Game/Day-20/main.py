# import turtle as t
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Udemy Snake Game")
screen.tracer(False)

# * Snake Object
snake = Snake()
food = Food()
score = Scoreboard()

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

    # ══════════ Detect collision with food ══════════ #
    if snake.head.distance(food) < 15:
        food.change_position()
        snake.extend()
        score.add_score()

    # ══════════ Detect collision with wall ══════════ #
    elif snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("Fuck You! - You Dead")
        score.game_over()
        quit()
        break

    # ══════════ Detect collision with tail ══════════ #
    for segment in snake.snake_body[1:]:
        # if segment == snake.head:
            # pass
        if snake.head.distance(segment) < 10:
            score.game_over()
            quit()
            break

screen.mainloop()
# screen.exitonclick()
