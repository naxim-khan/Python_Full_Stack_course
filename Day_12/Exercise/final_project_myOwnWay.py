import random
import os
def clear():
    os.system('cls')

RANDOM_NUMBER=random.randint(1,100)

# Game level's Hard , Easy hard give option of 5 and Easy give option of 10

# print(RANDOM_NUMBER)
game_over=False
print("I'm Thinking of a number between 1 and 100.")
difficulty_type=input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
attempts=0
if difficulty_type == "hard":
        attempts=5
elif difficulty_type=="easy":
        attempts=10

while attempts!=0:
    print(f"You've {attempts} attempts remaining!")
    guessed_number=int(input("Make a Guess: "))
    if guessed_number==RANDOM_NUMBER:
        clear()
        print(f"The number is: {RANDOM_NUMBER} You win!! 🎉")
        break
    if guessed_number!=RANDOM_NUMBER :
        attempts-=1
        if guessed_number<RANDOM_NUMBER:
            print(f"Too Low")
        elif guessed_number>RANDOM_NUMBER:
            print("Too high")
        if attempts==0:
            clear()
            print("Game Over\nYou Loose!🤣")