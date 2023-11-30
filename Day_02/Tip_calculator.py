print("Welcome to tip Calculator")
total_bill=float(input("What was the total bill? $ "))
tip_percentage=int(input("What percent tip would like pay 10, 12 or 15? "))
num_people=int(input("How many people to split the bill? "))

#tip amount calculation tip_amount=total_bill*(tip_percentage/100)
tip_amount=total_bill*(tip_percentage/100)
total_amount=total_bill+tip_amount
#split the bill
split_amount=total_amount/num_people
print(f"Each should pay: ${split_amount:.2f}") 
#.2f to format the output as a floating-point number with two decimal places. then it should be show only two digit number after decimal .34 <-- like this.