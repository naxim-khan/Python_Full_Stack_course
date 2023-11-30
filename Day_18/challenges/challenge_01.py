# Draw a square through turtle 
from turtle import *
import random
turtle=Turtle()
screen=Screen()
turtle.color("red")

colors= ["CornflowerBlue", "DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

for shape_side_n in range(3,11):
    # Givin different color to each line
    turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

# for _ in range(50):
#     if _ <=4:
#         turtle.right(90)
#         turtle.forward(100)
#     elif _ > (4) and _<7:
#         turtle.right(120)
#         turtle.forward(100)
#     else:
#         num=72
#         turtle.right(num)
#         num=72+72
#         turtle.forward(100)


screen.exitonclick()