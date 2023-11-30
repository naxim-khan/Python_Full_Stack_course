from turtle import *
import keyboard

tim=Turtle()
screen=Screen()


def move_forward():
    tim.forward(10)
    # tim.right(90)
    # pass

screen.listen()
screen.onkey(key="space",fun=move_forward) # key= When the space key is pressed fun=call this function.

screen.exitonclick()