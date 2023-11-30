# Debugging 
# 1. Describe the problem.
# def my_function():
#     for i in range(1,20):
#         if i==20:
#             print("You got it")
#             break
        
# there is a bug in the above function it'll not print (you got it)
# It's because of range function the range function works when
# say for i in range (20) it'll start from 0 and goes upto 19
# if you say for i in range (1,20) it'll goes from 1 upto 19 and does not include 20.
# Below is the debug solution. 
def my_function():
    for i in range(1,21):
        if i==20:
            print("You got it")
            break

my_function()

