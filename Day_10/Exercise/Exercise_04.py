import os
def clear():
    os.system('cls')

def calculator(num1,operator,num2):
    """First Enter number then operator (+,-,*,/) then second
    number. then press enter to see the result"""
    result=0
    if operator=="+":
        result=num1+num2
        return result
    elif operator=="-":
        result=num1-num2
        return result
    elif operator=="*":
        result=num1*num2
        return result
    elif operator=="/":
        result=num1/num2
        return result
    else:
        print("Sorry You entered Wrong Operator!!")


while True:
    n1=int(input("Enter first Number : "))
    op=input("Enter Operator(+,-,*,/): ")
    n2=int(input("Enter Second Number: "))

    Result=calculator(n1,op,n2)
    print(Result)

    option=input("Exit. Continue\n").lower()
    if option=="exit":
        break
    else:
        clear()
        continue