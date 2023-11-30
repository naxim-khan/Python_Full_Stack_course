# Debug odd or Even Exercise.
# Instructions:
# Read this code in main.py
# spot the problem 🐞
# Modify the Code to fix the program. 
# Fix the code so that it works and passed the tests when you submit.

# Hint: 
# 1. Review the previous lesson and go through the 10 steps to tackle
# these debugging problems.

# The Code 
# number = int(input("Which Number do you want to check?: "))
# if number % 2=0:
#     print(f"{number}This an even number.")
# else:
#     print(f"{number}This is an odd number.")

# The Solution

# number = int(input("Which Number do you want to check?: "))
# if number % 2==0: #  🐞 👈🏻 🪓
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

# Another Problem.
# year=input("Which year do you want to check? ") 
# if year%4==0:
#     if year% 100==0:
#         if year % 400==0:
#             print("Leap Year.")
#         else:
#             print("Not Leap Year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not Leap year.") 

# Type error in the above code 👆🏻

# The Solution
# year=int(input("Which year do you want to check? ")) #🐞👈🏻Spotted
# if year%4==0:
#     if year% 100==0:
#         if year % 400==0:
#             print("Leap Year.")
#         else:
#             print("Not Leap Year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not Leap year.")

# Another Problem.
# for number in range (1,101):
#     if number %3==0 or number % 5==0:
#         print("FizzBuzz")
#     if number %3==0:   🐞 👈🏻
#         print("Fizz")  🐞 👈🏻  😎
#     if number % 5 == 0:🐞 👈🏻
#         print("Buzz")
#     else:
#         print([number])

# Solution: 😎
for number in range (1,101):
    if number %3==0 and number % 5==0:
        print("FizzBuzz")
    elif number %3==0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])
