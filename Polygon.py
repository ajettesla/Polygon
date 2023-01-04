import random
import turtle
from turtle import *

timmy = Turtle()

timmy.speed("fastest")

turtle.colormode(255)


def get_the_shape(sides):
    angles = 360 / sides
    timmy.pencolor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    for i in range(0, sides):
        timmy.setheading(timmy.heading() + angles)
        timmy.forward(100)


for j in range(3, 80):
    get_the_shape(j)
screen = Screen()
screen.exitonclick()
