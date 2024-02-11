import turtle as t
import random


tin = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tin.speed('fastest')
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tin.circle(100)
        tin.color(random_color())
        tin.setheading(tin.heading() + size_of_gap)
draw_spirograph(3)
screen = t.Screen()
screen.exitonclick()