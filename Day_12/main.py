# choosing a random number between 1 and 100.
from random import randint
answer=randint(1,100)
# Make funtion to set difficulty.

# Let the user guess a number.

# Function to check user's guess against actual answer.
def check_answer(guess, answer):
    if guess<answer:
        print("Too Low")
    elif guess>answer:
        print("To High")
    else:
        print("You got it! The answer was {answer}.")

# Track the number of turns and reduce by 1 if they get it wrong.

#Repeat the guessing functionality if they get it wrong.
# INCOMPLETE.