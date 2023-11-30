import random
import hangman_words
import hangman_logo
import gameStages
import os

def clear():
    os.system('cls')

print(hangman_logo)
random_word = random.choice(hangman_words.word)
stages = gameStages.stages


lives = len(stages)-1
print(random_word)

randomWordlength = len(random_word)
display = []
for _ in range(randomWordlength):
    display += "_"

endOfGame = False

while not endOfGame:
    guess = input("Guess a letter: ").lower()
    clear() # used to clear console screen
    
    # checking Guess letter
    if guess in display:
        print(f"You've already guessed {guess}") 
    
    for i in range(randomWordlength):
        if guess == random_word[i]:
            display[i] = guess
            
    # checking if user is wrong
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You lose!")
    
    print(" ".join(display))
    
    if "_" not in display:
        endOfGame = True
        print("You win!")
        