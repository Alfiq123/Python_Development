import turtle
import random

actual_colors = [(246, 242, 244), (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def draw_random_dots_grid(grid_size = 10, dot_size = 25, spacing = 30):
    """
    Draws a grid of random colored dots with white dots in between.

    Args:
        grid_size: The number of dots in each row and column.
        dot_size: The size of each dot.
        spacing: The spacing between the center of each dot.
    """

    turtle.colormode(255)

    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.hideturtle()

    start_x = -((grid_size * 2 - 1) * spacing) / 2
    start_y = ((grid_size * 2 - 1) * spacing) / 2

    for row in range(grid_size):
        t.goto(start_x, start_y - row * spacing * 2)
        for col in range(grid_size):
            # color = (random.choice(actual_colors))  # Generate random RGB color
            t.dot(dot_size, random.choice(actual_colors))
            t.penup()
            t.forward(spacing)
            t.dot(dot_size, "white")
            t.penup()
            t.forward(spacing)

    turtle.done()

draw_random_dots_grid() # default 10x10
# draw_random_dots_grid(5, 15, 30) #example with different size, dot size, and spacing.