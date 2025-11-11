import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


# Set up keyboard listeners
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

# Enable listening for key events
screen.listen()

screen.mainloop()
turtle.done()
