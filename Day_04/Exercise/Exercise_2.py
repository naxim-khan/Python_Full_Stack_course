import random
names=input("Enter names seperated by comma and space (harry, Janny): ")
names=names.split(", ")
randomName=random.choice(names)
print(f"{randomName} is going to buy the meal today!")
