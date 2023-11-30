import os
def clear():
    os.system('cls')

# Calculator

# add
def add(n1,n2):
    return n1+n2
# Subtract
def sub(n1,n2):
    return n1-n2
# Multiply
def multiply(n1,n2):
    return n1*n2
# divide
def divide(n1,n2):
    return n1/n2

operations={
            "+":add,
            "-":sub,
            "*":multiply,
            "/":divide,
            }

num1=int(input("Enter First number : "))

# Printing the symbol's
for operator in operations:
    print(operator)
# taking operator input
operation_symbol= input("Pick an operation from the line above: \n")
 
num2=int(input("Enter Second number: "))

if operation_symbol!='+' and operation_symbol!='-' and operation_symbol!='*' and operation_symbol!='/':
    print("Wrong symbol entered.!!! (+,-,*,/)")
else:
    calculation_function=operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    while True:
        option=input(f"Type 'y' to continue calculation with {answer}, or type 'n' to exit.: y\n").lower()
        if option=='n':
            break
        operation_symbol= input("Pick another operation: \n")
        
        num3=int(input("What's the next number?: "))
        calculation_function=operations[operation_symbol]
        second_answer=calculation_function(calculation_function(num1,num2),num3)
        print(f"{answer} {operation_symbol} {num3} = {second_answer}")
        
        

        
        

