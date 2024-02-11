import random
from turtle import Turtle, Screen

tin = Turtle()
tin.shape("turtle")
tin.color("green")

# for i in  range(4):
#     tin.forward(100)
#     tin.right(90)


color = ["Orange","green","Red","Magenta","Teal"]
def draw_shape(num_side):
    angle = 360 / num_side
    for i in range(num_side):
        tin.forward(100)
        tin.right(angle)

for draw_shape_n in range(3,11):
    tin.color(random.choice(color))
    draw_shape(draw_shape_n)





for t1 in range(3):
    tin.forward(100)
    tin.right(120)
    tin.color("Orange")
for t2 in range(4):
    tin.forward(100)
    tin.right(90)
    tin.color("green")
for t3 in range(5):
    tin.forward(100)
    tin.right(72)
    tin.color("Red")
for t4 in range(6):
    tin.forward(100)
    tin.right(60)
    tin.color("Magenta")
for t5 in range(7):
    tin.forward(100)
    tin.right(51.5)
    tin.color("Purple")
for t6 in range(8):
    tin.forward(100)
    tin.right(45)
    tin.color("Blue")
for t7 in range(9):
    tin.forward(100)
    tin.right(40)
    tin.color("Teal")



screen = Screen()
screen.exitonclick()