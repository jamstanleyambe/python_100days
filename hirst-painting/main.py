# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
#
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,g)
#    rgb_colors.append(new_color)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tom = turtle_module.Turtle()
tom.hideturtle()
tom.penup()
color_list = [(27, 32, 32), (40, 31, 31), (201, 161, 161), (40, 27, 27), (61, 103, 103), (26, 38, 38), (111, 167, 167),
 (142, 84, 84), (64, 120, 120), (142, 72, 72), (122, 182, 182), (189, 90, 90), (199, 92, 92), (195, 133, 133),
 (84, 155, 155), (214, 200, 200), (162, 159, 159), (222, 217, 217), (214, 222, 222), (213, 219, 219),
 (39, 55, 55), (74, 152, 152), (93, 120, 120), (95, 46, 46), (39, 78, 78), (226, 214, 214), (155, 208, 208),
 (98, 48, 48), (77, 72, 72), (215, 175, 175)]

tom.setheading(225)
tom.forward(300)
tom.setheading(0)
number_of_dot = 100
tom.speed("fastest")


for i in range(1, number_of_dot + 1):
    tom.dot(20,random.choice(color_list))
    tom.forward(50)

    if i % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()