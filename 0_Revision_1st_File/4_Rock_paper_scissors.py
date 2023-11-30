import random

Rock='''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    

Paper ='''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

Scissors = '''
SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose=[Rock,Paper,Scissors]

try:
    computer_choice=random.randint(0,2)
    user_choice=int(input("Enter you choice: 0, Rock: 1,Paper: ,2,Scissor: "))
    computer_choose=choose[computer_choice]
    user_choose=choose[user_choice]

    print(f"You Choose.\n{user_choose}\nComputer Choose\n{computer_choose}")
    if user_choice==0 and computer_choice==2:
        print("You win 🌟")
    elif computer_choice==0 and user_choice==2:
        print("Computer Win 🌟")
    elif computer_choice>user_choice:
        print("Computer Win 🌟")
    elif user_choice==computer_choice:
        print("It's a Draw")
        
except ValueError:
    print("Sorry Invalid Entry!!!\nChoose  Only in Numbers (0,1,2) ")
except IndexError:
    print("Sorry Invalid Entry!!!\nChoose between 0,1,2 Number's")
