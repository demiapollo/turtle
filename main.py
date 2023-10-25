from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.shape("arrow")

colors = ["royal blue", "lawn green", "cornsilk", "goldenrod", "light coral", "dark slate blue",
          "blue violet", "spring green", "light cyan"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        

for shape_side_n in range(3, 11):
    tim.color(choice(colors))
    draw_shape(shape_side_n)









screen = Screen()
screen.exitonclick()
