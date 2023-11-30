from turtle import Turtle,Screen # Graphic Module.

turtle=Turtle() # Blue print for making Grphics

# Setting the color
turtle.color("white")
turtle.penup()

screen = Screen()
# Set the background color of the turtle window to bluewish dark
screen.bgcolor("#16191E")
# Starting the turtle from the left side of window
turtle.goto(screen.window_width()/-3, screen.window_height()/3)

turtle.pd()
turtle.pensize(10)
# cursor facing downward
turtle.setheading(270)
turtle.forward(200)
turtle.penup()
turtle.setheading(-270)
turtle.forward(200)
turtle.pu()
# turtle.setheading(0)
turtle.setheading(-65)
turtle.pd()
turtle.forward(211)
turtle.setheading(90)
turtle.forward(200)
# Starting heart shape
turtle.pu()
turtle.setheading(0)
turtle.forward(150)
turtle.setheading(-90)
turtle.forward(200)
turtle.setheading(0)
turtle.pd()

# turtle.begin_fill()
# turtle.color("red")  # Set the fill color to red
# turtle.left(-140)
# turtle.forward(80)
# turtle.circle(-40, 180)
# turtle.right(-120)
# turtle.circle(-40, 180)
# turtle.forward(100)
# turtle.end_fill()

def drawcurve():
    
    for i in range(200):
        # Defining step by step curve motion
        turtle.right(1)
        turtle. forward(1)

# Set the fill color to pink and border color to Red
turtle.color('red', 'pink')
 # Start filling the color
turtle.begin_fill()
turtle.left(140)

 # Draw the left line
turtle.forward(111.65)
# Draw the left curve
drawcurve()
turtle.left(120)
drawcurve()
 # Draw the right line
turtle.forward(111.65)
 # end_fill() : This method fills the polygon with the current fill color by closing it between the current position and the initial position.
turtle.end_fill()
turtle.penup()

# setting head to right side 
turtle.color("white")
turtle.setheading(0)
turtle.forward(200)
turtle.setheading(90)
turtle.pd()
turtle.forward(200)
# the previous n code 
turtle.setheading(-90)
turtle.forward(200)
turtle.penup()
turtle.setheading(-270)
turtle.forward(200)
turtle.pu()
# turtle.setheading(0)
turtle.setheading(-65)
turtle.pd()
turtle.forward(211)
turtle.setheading(90)
turtle.forward(200)
turtle.pu()

# drawing bottom line
turtle.setheading(0)
turtle.forward(50)
turtle.setheading(-90)
turtle.forward(300)
turtle.setheading(180)
turtle.color("blue")
turtle.pd()
turtle.forward(600)

# draw white little line
turtle.pencolor("red")
turtle.pu()
turtle.setheading(-90)
turtle.forward(20)
turtle.pensize(5)
turtle.setheading(0)
turtle.pd()
turtle.forward(600)

# turtle.forward(100)
# This will keep the window open until you click on it
screen.exitonclick()