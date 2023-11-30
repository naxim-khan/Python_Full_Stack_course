# write a program that calculate life in weeks.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age=int(age)
rem_years=90-age
days=rem_years*365 # one year have 364 days
weeks=rem_years*52 # one year have 52 weeks
months=rem_years*12 # one year have 12 months
output=f"You'have {days} days,{weeks} weeks, and {months} months left."
print(output)