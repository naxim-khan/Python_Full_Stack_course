# Fizz Buzz Game.
# You're program should print Each number from 1 t0 100 in turn.
nums=100
nums+=1
for i in range(1,nums):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)