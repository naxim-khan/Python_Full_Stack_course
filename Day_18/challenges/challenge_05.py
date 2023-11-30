from turtle import *
import random
tim=Turtle()
screen=Screen()
tim.speed("fastest")
tim.pensize(1)

def random_color():
    r=random.random()
    g=random.random()
    b=random.random()
    color=(r,g,b)
    return color
def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(10)




screen.exitonclick()