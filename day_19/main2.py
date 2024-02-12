import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="make your bet", prompt="which one will win the race ? enter color:  ")
color = ['red', 'blue', 'green', 'yellow', 'black', 'orange']

position = [-150, -100, -50, 0, 50, 100]

all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is the winner")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


jam = Turtle("turtle")
jam.penup()
jam.color("orange")
jam.goto(x=-230, y=-100)

jam = Turtle("turtle")
jam.penup()
jam.color("yellow")
jam.goto(x=-230, y=-50)

jam = Turtle("turtle")
jam.penup()
jam.color("blue")
jam.goto(x=-230, y=0)

jam = Turtle("turtle")
jam.penup()
jam.color("purple")
jam.goto(x=-230, y=50)

jam = Turtle("turtle")
jam.penup()
jam.color("green")
jam.goto(x=-230, y=100)

screen.exitonclick()