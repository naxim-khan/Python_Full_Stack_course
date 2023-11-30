import random
items=[
"""
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
,
"""
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
,
"""
Scissors:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
]
user_choice=int(input("What do you choose? \nType 0 for Rock, 1 For Paper, 2 for Scissors: "))
computer_choice=random.randint(0,2)
print (f"You choose:\n{items[user_choice]}")
print(f"Computer choose:\n{items[computer_choice]}\n")

if user_choice==computer_choice:
    print("It's a Tie😊!")
elif ((user_choice==0 and computer_choice==2)or(user_choice==1 and computer_choice==0)or(user_choice==2 and computer_choice==1)):
    print ("You Win!! 😊")
else:
    print ("You loose!! 😆")
    
