from turtle import *# A Blue print which some body else is created.
# import another_module 
# print(another_module.another_variable)

timmy=Turtle() # Here we construct an object from a class
# and we saved that object inside timmy.
print(timmy)
color('red','yellow')
begin_fill()
while True:
    
    forward(100)
    left(100)
    
    if abs(pos())<1:
        break
end_fill()

# How to call the object attribute. E.g; Car.speed car(object) (speed) attribute.
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()