print("Welcome to love Calculator")
name1=input("Enter your name: ")
name2=input("Enter his/her name:")
combinedNames=name1+name2
lowecasenames=combinedNames.lower()
t=combinedNames.count("t")
r=combinedNames.count("r")
u=combinedNames.count("u")
e=combinedNames.count("e")
true=t+r+u+e
l=combinedNames.count("l")
o=combinedNames.count("o")
v=combinedNames.count("v")
e=combinedNames.count("e")
love=l+o+v+e
loveScore=int(str(true)+str(love))
if loveScore <10 or loveScore >90:
    print(f"Your love score is {loveScore}, you go together like coke and mentos")
elif loveScore>=40 and loveScore <=50:
    print(f"Your love score is {loveScore}, you are alright")
else:
    print(f"Your love score is {loveScore}")