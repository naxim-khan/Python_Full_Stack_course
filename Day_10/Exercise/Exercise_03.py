# Docstring : Documentation for function.
def add(num1,num2):
    """Taking two number's as input then add 
    it and show us the result""" # the documentation for function
    result=num1+num2
    return result

n1=int(input("Enter first number: "))
n2=int(input("Enter Second number: "))

addition=add(n1,n2)
print(addition)