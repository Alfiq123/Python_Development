import turtle
import time
import random

# Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body segments
segments = []

# Score
score = 0
high_score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Game over text
game_over_text = turtle.Turtle()
game_over_text.speed(0)
game_over_text.color("white")
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.goto(0, 0)

# Functions to move the snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Function to reset the game
def reset_game():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    
    # Clear the segments list
    segments.clear()
    
    # Reset the score
    global score
    score = 0
    
    # Update the score display
    score_display.clear()
    score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
    
    # Clear game over text
    game_over_text.clear()

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
window.onkeypress(reset_game, "space")

# Main game loop
while True:
    window.update()
    
    # Check for collision with the borders
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):
        game_over_text.write("Game Over! Press Space to Restart", align="center", font=("Courier", 24, "normal"))
        
        # Update high score
        if score > high_score:
            high_score = score
        
        reset_game()

    # Check for collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        
        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("dark green")
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase the score
        score += 10
        
        # Update the score display
        score_display.clear()
        score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
    
    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    # Check for collision with the body segments
    for segment in segments:
        if head.distance(segment) < 20:
            game_over_text.write("Game Over! Press Space to Restart", align="center", font=("Courier", 24, "normal"))
            
            # Update high score
            if score > high_score:
                high_score = score
            
            reset_game()
    
    move()
    
    # Control game speed
    time.sleep(0.1)
