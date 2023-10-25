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
    color = (r, g, b)
    return color



# Draw a circle
tim.speed("fastest")

def draw_spiograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)



draw_spiograph(5)


screen = Screen()
screen.exitonclick()