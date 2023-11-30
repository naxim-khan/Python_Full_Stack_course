# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height=float(height)
weight=int(weight)
bmi=(weight)/(height**2)
print(weight," ÷ (",height," x ",height,") = ",bmi)
print(int(bmi))