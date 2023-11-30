# 1 can of paint cover 5 square meters of wall.
# given a random height and wideth of wall, calclate how many cans
# of paint you'll need to buy.
def canNeeded(width, height):
    width=float(width) 
    height=float(height)
    numbers_of_cans=(width*height)/5
    round_number=round(numbers_of_cans,2)
    # numbers_of_cans=int(numbers_of_cans)
    if numbers_of_cans<2:
        print("Sorry You can't buy only 2 cans.You've to buy more than 2")
        print(f"You need {round_number} cans for Your wall.")

w=input("Enter width of wall in meter's : ")
h=input("Enter Height of Wall in Meter's:  ")
canNeeded(w,h)
