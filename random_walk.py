from turtle import Screen
import turtle as t
import random


tim = t.Turtle()
t.colormode(255)
tim.shape("arrow")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

directions = [0, 90, 180, 270]
tim.speed("fastest")

for _ in range(200):
    tim.width(random.randint(1, 10))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))











screen = Screen()
screen.exitonclick()