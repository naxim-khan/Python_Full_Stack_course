# **Kwargs: Many Keyworded Arguments.
def calculate(n,**kwargs): # kwargs keyword arguments.
    # print(kwargs) it'll convert it's into a dictionary. 
    # the add should be the key
    # and the value is 3
    # for key,value in kwargs.items():
    #     # print(key)
    #     # print(value)
    #     # i can also use the names of the keys.
    #     print(kwargs["add"])
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kwargs):
         self.make=kwargs.get("make")
         self.model=kwargs.get("model")
         self.color=kwargs.get("colour")

my_car=Car(make="Nissan",model="",color="red")
print(my_car.make)
print(my_car.model)
print(my_car.color)