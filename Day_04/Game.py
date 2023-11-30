import random
print("Welcome to the Rock, Paper, Scissor, Game:")
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    

Paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choose=[Rock,Paper,Scissors]
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors."))
print(choose[user_choice])
computer_choice= random.randint(0,2)
print(choose[computer_choice])
if user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif computer_choice>user_choice:
    print("You lose")
elif user_choice==computer_choice:
    print("It's a Draw")
else:
    ("Sorry! you input the wrong number")