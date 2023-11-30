# Display Art.
import os
import random
from gameData import data
def clear():
    os.system('cls')

SCORE=0
# Generate a random account from the game data.
game_should_continue=True
account_b=random.choice(data)


# Make the game repeatable
while game_should_continue:
    account_a=account_b # Making account at position B become the next account at position A.
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    # format the account data into printable format.
    def accounts_data(account):
        """Printing account Data Name, Description and country by passing random account."""
        name=account["name"]
        description=account["description"]
        country=account["country"]
        return f"{name} a {description} from {country}"

    # Check if user is correct.
    def check_answer(guess,a_followers,b_followers):
        "Take the User guess followers counts and return whether if they're true or not"
        if a_followers>b_followers:
            return guess=="a"
        else:
            return guess=="b"

    print(f"Compare A: {accounts_data(account_a)}")
    print("VS")
    print(f"Against B: {accounts_data(account_b)}")
    # Ask user for a guess.
    guess=input("Who has more follower's? Type 'A' or 'B': ").lower()

    ## Get follower of each account.
    a_followers=account_a["follower_count"]
    b_followers=account_b["follower_count"]

    # Clear the screen
    clear()
    ## Use if statement to check if user correct. 
    # Give user feedback on their guess.
    # Score Keeping.
    is_correct=check_answer(guess,a_followers,b_followers)
    if is_correct:
        SCORE+=1
        print(f"You're right! current Score: {SCORE}.")
    else:
        print(f"Sorry, That's Wrong! The final Score: {SCORE}")
        game_should_continue=False
        if SCORE >=6:
            print(f"Goob Job!! 🌟\nYou scored: {SCORE}, That's Awesome!!")
                
