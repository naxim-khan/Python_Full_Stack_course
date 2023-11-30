print("Welcome to the tip calculator")
total=float(input("What was the total bill? :$ "))
people_n=int(input("How many people to split the bill:$ "))
tip_percentage=int(input("What percentage of tip you would like to give? 10, 12, or 15: "))

tip_amount=total*(tip_percentage/100)
total_amount=tip_amount+total
split_amount=total_amount/people_n

print(f"Each person should pay: {split_amount:2f}$ of amount.")