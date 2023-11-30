from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()

# Set the brush size to 2 pixels
timmy_the_turtle.pensize(2)

# Set the speed of the turtle
timmy_the_turtle.speed("fastest")

# Get the window dimensions
window_width = screen.window_width()
window_height = screen.window_height()

# Function to generate a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Perform the random walk
for _ in range(5000):
    # Change color
    timmy_the_turtle.pencolor(random_color())

    # Move the turtle forward in a random direction
    timmy_the_turtle.forward(20)

    # Get the turtle's current position
    current_x = timmy_the_turtle.xcor()
    current_y = timmy_the_turtle.ycor()

    # Check if the turtle is beyond the window borders
    if abs(current_x) > window_width / 2 or abs(current_y) > window_height / 2:
        timmy_the_turtle.pu()
        timmy_the_turtle.goto(0, 0)  # Reset the turtle to the center of the window
        timmy_the_turtle.pd()
    timmy_the_turtle.setheading(random.randint(0, 359))

# This will keep the window open until you click on it
screen.exitonclick()
