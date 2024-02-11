import turtle as t
import random


tin = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directons = [0, 90, 180, 270]
tin.pensize(10)
tin.speed('fastest')

for i in range(500):
    tin.forward(30)
    tin.color(random_color())
    tin.setheading(random.choice(directons))

screen = t.Screen()
screen.exitonclick()