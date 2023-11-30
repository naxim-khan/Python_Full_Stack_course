# Draw a dash line
from turtle import *
turtle=Turtle()
screen=Screen()

turtle.pensize(2)
for _ in range (15):
    turtle.forward(10)
    turtle.pu()
    turtle.forward(10)
    turtle.pd()

screen.exitonclick()