from turtle import *
import random
trt=Turtle()
screen=Screen()
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)
direction1=[0,90,180,270]

trt.pensize(10)
trt.speed("fastest")

# Set up window dimensions
window_width = 800
window_height = 600
screen.setup(width=window_width, height=window_height)

for _ in range(200):

    # Get the turtle's current position
    current_x = trt.xcor()
    current_y = trt.ycor()
    trt.color(random_color())
    if abs(current_x) > window_width / 2 or abs(current_y) > window_height / 2:
        trt.pu()
        trt.goto(0,0)

    trt.pd()
    trt.forward(30)
    trt.setheading(random.choice(direction1))
    

screen.exitonclick()