# Create where you can pass as many argumen'ts as you want
# and it'll add all the number's and give you the result.
def add(*args): # *args you can give it any name like *numbers
    result=0
    for n in args:
        result += n
    return print(f"{result}")

add(1,2,3,5)
