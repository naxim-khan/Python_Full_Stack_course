import math
height=float(input("Height: "))
weight=int(input("Weight: "))
# How we can use raise: method to raise an Error
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")


bmi= weight / height **2
print(bmi)


