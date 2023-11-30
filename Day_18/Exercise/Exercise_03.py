from turtle import *
import random

trt = Turtle()
screen = Screen()

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

directions = [0, 90, 180, 270]
trt.pensize(5)
trt.speed("fastest")

# Set up window dimensions
window_width = 800
window_height = 600
screen.setup(width=window_width, height=window_height)

for _ in range(5000):
    # Get the turtle's current position
    current_x = trt.xcor()
    current_y = trt.ycor()
    trt.color(random_color())
    # Get the turtle's current position
    current_x = trt.xcor()
    current_y = trt.ycor()

    # Check if the turtle is beyond the window borders
    if abs(current_x) > window_width / 2 or abs(current_y) > window_height / 2:
        trt.pu()
        trt.goto(0, 0)  # Reset the turtle to the center of the window
        trt.pd()
    
    trt.dot(random.randint(1, 5))
    trt.penup()
    trt.forward(10)
    trt.pendown()
    trt.dot(random.randint(1, 5))
    trt.penup()
    trt.forward(10)
    trt.pendown()
    trt.dot(random.randint(1, 5))
    
    trt.setheading(random.choice(directions))

screen.exitonclick()
