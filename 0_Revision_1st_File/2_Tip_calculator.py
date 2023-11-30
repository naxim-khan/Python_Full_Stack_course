
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $:"))
numbers_of_people=int(input("How many people to split the bill: "))
tip_percentage=int(input("What Percetage of tip would like to give? 10, 12, or 15:  "))

tip_amount=(tip_percentage/100)*total_bill
total_amount=total_bill+tip_amount
split_amount=total_amount/numbers_of_people



print(f"Each person should pay: $ {split_amount :.2f}")