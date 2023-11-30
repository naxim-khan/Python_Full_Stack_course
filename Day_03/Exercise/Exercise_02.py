height=float(input("Enter you Height in m.  : "))
weight=float(input("Enter you weight in kg. : "))
bmi=(weight)/(height**2)
if bmi <18.5:
    print(f"Your BMI is {bmi:.2f}, You are underweight")
elif bmi >18.5 and bmi<25:
    print(f"Your BMI is {bmi:.2f}, Your BMI is normal")
elif bmi > 24 and bmi<30:
    print(f"Your BMI is {bmi:.2f}, You are overweight.")
elif bmi > 30 and bmi<35:
    print(f"Your BMI is {bmi:.2f}, You are obese.")
else:
    print(f"Your BMI is {bmi:.2f}, You are clinically obese.")