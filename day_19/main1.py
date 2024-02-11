from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turnleft():
    tim.left(10)


def turnright():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(move_forward, "f")
screen.onkey(move_backward, "b")
screen.onkey(turnright, "r")
screen.onkey(turnleft, "l")
screen.onkey(clear, "c")







screen.exitonclick()