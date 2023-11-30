from turtle import *
import keyboard

tim=Turtle()
screen=Screen()

def moveForward():
    tim.forward(10)
    # pass
def moveBackward():
    #s
    tim.backward(10)

def anti_clockwise():
    # tim.left(90)
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
    
    # pass

def clock_wise():
    
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
    # pass

def clear_drawing():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()
    #C
    # pass
def pen_up():
    tim.pu()
    #U
    pass
def pen_down():
    tim.pd()
    #O

screen.listen()

screen.onkeypress(moveForward,"Up")
screen.onkeypress(moveBackward,"Down")
screen.onkeypress(anti_clockwise,"Right")
screen.onkeypress(clock_wise,"Left")
screen.onkeypress(clear_drawing,"c")
screen.onkeypress(pen_up,"u")
screen.onkeypress(pen_down,"o")



screen.exitonclick()