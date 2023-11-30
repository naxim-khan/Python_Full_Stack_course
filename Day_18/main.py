from turtle import *
import colorgram  
from PIL import Image # module which pick's color's from images.
import random
# image_path='image.jpg'
# image=Image.open(image_path)
# colors=image.getcolors(30)
# colors=colorgram.extract('image.jpg',30)
tim=Turtle()
screen=Screen()
# tim.pensize(10)
tim.speed("fastest")
tim.hideturtle()
# Creating random color's
def colors():
    r=random.random()
    g=random.random()
    b=random.random()
    color=(r,g,b)
    return color

tim.pu()
tim.goto(-200,-200)
for i in range (10):
    for i in range (10):
        tim.pencolor(colors())
        tim.dot(20)
        tim.pu()
        tim.forward(50)
        tim.pd()
        # tim.dot()  
    tim.pu()  
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    tim.back(500)
    tim.pd()


screen.exitonclick()