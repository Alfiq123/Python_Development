import turtle
import time
import random

# --- Setup the screen ---
wn = turtle.Screen()
wn.setup(width=600, height=600) # Set screen size
wn.bgcolor("black")         # Set background color
wn.title("Snake Game")      # Set window title
wn.tracer(0)                # Turn off screen updates - manual updates needed

# --- Game Variables ---
score = 0
high_score = 0
delay = 0.1  # Starting game speed (lower is faster)

# --- Create the snake head ---
head = turtle.Turtle()
head.speed(0)          # Animation speed (0 is fastest)
head.shape("square")   # Shape of the turtle
head.color("white")    # Color of the turtle
head.penup()           # Don't draw lines when moving
head.goto(0, 0)        # Start at the center
head.direction = "stop" # Initial direction

# --- Create the food ---
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)      # Start food at a different location

# --- List to hold the snake body segments ---
segments = []

# --- Create the score board ---
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square") # Shape doesn't matter as it's hidden
pen.color("white")
pen.penup()
pen.hideturtle()     # Hide the turtle icon
pen.goto(0, 260)     # Position the scoreboard at the top
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# --- Functions for movement ---
def go_up():
    # Prevent reversing direction immediately
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
        y = head.ycor()  # Get current y-coordinate
        head.sety(y + 20) # Move up 20 units (size of square)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor() # Get current x-coordinate
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# --- Keyboard Bindings ---
wn.listen() # Listen for keyboard events
wn.onkey(go_up, "Up")    # Call go_up() when Up arrow is pressed
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# --- Game Loop ---
while True:
    wn.update() # Manually update the screen

    # --- Check for collision with the border ---
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1) # Pause briefly
        head.goto(0, 0) # Send head back to center
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000) # Move off-screen

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0
        # Reset the delay (game speed)
        delay = 0.1

        # Update the score display
        pen.clear() # Clear previous score text
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # --- Check for collision with food ---
    if head.distance(food) < 20: # If head is within 20 units of food
        # Move the food to a random spot
        x = random.randint(-280, 280) # Random x within screen bounds
        y = random.randint(-280, 280) # Random y within screen bounds
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey") # Body color
        new_segment.penup()
        segments.append(new_segment) # Add to the list

        # Shorten the delay (increase speed)
        delay -= 0.001 # Adjust this value to control speed increase

        # Increase the score
        score += 10

        # Update the high score if needed
        if score > high_score:
            high_score = score

        # Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # --- Move the end segments first in reverse order ---
    # This makes the body follow the head
    for index in range(len(segments)-1, 0, -1): # Loop from last segment down to the second
        x = segments[index-1].xcor() # Get x-coordinate of the segment in front
        y = segments[index-1].ycor() # Get y-coordinate of the segment in front
        segments[index].goto(x, y)    # Move current segment to that position

    # --- Move segment 0 to where the head is ---
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # --- Move the head ---
    move()

    # --- Check for collision with the body segments ---
    for segment in segments:
        if segment.distance(head) < 20: # If head is within 20 units of a body segment
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for seg in segments:
                seg.goto(1000, 1000) # Move off-screen

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            # Reset the delay (game speed)
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # --- Control game speed ---
    time.sleep(delay)

# --- Keep the window open ---
# This line is technically redundant because the while True loop keeps it open,
# but it's good practice if you were to exit the loop.
# wn.mainloop()