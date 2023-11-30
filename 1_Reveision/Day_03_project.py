# Check if number of odd or even
import os
def clear():
    os.system('cls')

while True:
    num=int(input("Enter a number to check if it's Even or Odd\n"))
    number=num%2
    if number == 0:
        print(f"{num} is Even number")
    else:
        print(f"{num} is Odd number")

    option=input("\nCheck another Number\nType 'Yes' to continue\nType 'NO' to Exit\n").lower()
    if option=="no" or option=="exit":
        break
    else:
        clear()
        continue