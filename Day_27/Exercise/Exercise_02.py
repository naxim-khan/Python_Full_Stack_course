# Advanced Python Argument's 
# How to use advanced python arguments.
"""
E.g: we how key words arguments works.
Key words Arguments:

def my_function(a,b,c):
    do this with a
    do this with b 
    do this with c

my_function(c=3,a=1,b=2)

Argumets with Defaults Values:
we can do this by changing the functions declaration.
so when we create our function we can already give it some values
to start up. like below:
def my_function(a=1,b=2,c=3):
    do this with a
    do this with b 
    do this with c

adnd a,b,c are the default values here.
so that means  when i call this function i don't have actually to provide any values.
my_function()
if i want to modifed the values insde the function
i can do that like below:
my_function(b=5)
and other values would be still on the default values.


"""
# Providing default values for option arguments.

def my_function(a=1,b=2,c=3):
    a+=1
    b+=1
    c+=1
    return a,b,c

print(my_function(c=7))

# How create function which can take unlimited number's of Argument's
# You can achieve by this *args keyword 
def add(*args):
    for n in args:
        print(n)

print(add(12,13))