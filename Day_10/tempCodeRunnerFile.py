operation_symbol= input("Pick another operation: \n")
num3=int(input("What's the next number?: "))
calculation_function=operations[operation_symbol]
second_answer=calculation_function(calculation_function(num1,num2),num3)
print(f"{answer} {operation_symbol} {num3} = {second_answer}")