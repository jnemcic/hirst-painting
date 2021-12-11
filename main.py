import random
import colorgram
from turtle import Turtle, Screen, colormode


def extract_colors(image, num_of_colors):
    colors = colorgram.extract(image, num_of_colors)
    global rgb_colors
    for color in colors:
        r = color.rgb.r
        b = color.rgb.b
        g = color.rgb.g
        new_color = (r, b, g)
        rgb_colors.append(new_color)


# Turtle initialization
timmy = Turtle()
timmy.speed(20)
timmy.penup()
timmy.goto(-250, -200)
timmy.pendown()
colormode(255)

rgb_colors = []
extract_colors("hirst.jpg", 20)

# Turtle drawing
space = 50
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.penup()
        timmy.forward(50)
    timmy.goto(-250, -200 + space)
    space += 50

my_screen = Screen()
my_screen.exitonclick()
