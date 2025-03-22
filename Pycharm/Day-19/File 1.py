import turtle

apc = turtle.Turtle()
scr = turtle.Screen()


def mov_forward():
    apc.forward(10)


scr.listen()
scr.onkey(key = "space", fun = mov_forward)
scr.exitonclick()
