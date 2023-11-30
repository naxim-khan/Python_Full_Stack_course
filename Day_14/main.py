import gameData
import random
import os
def clear():
    os.system('cls')

Data=gameData.data
SCORE=[]
GAME_OVER=False

def data_a_followers():
    randomNumber=random.randint(0,len(Data)-1)
    data_a=Data[randomNumber]
    followers_a=data_a["follower_count"]
    return followers_a

def data_b_followers():
    randomNumber=random.randint(0,len(Data)-1)
    data_b=Data[randomNumber]
    followers_b=data_b["follower_count"]
    return followers_b

def followers_a():
    A_followers=data_a_followers()
    return A_followers
def followers_b():
    B_followers=data_a_followers()
    return B_followers
        

def data_a_values():
    randomNumber=random.randint(0,len(Data)-1)
    data_a=Data[randomNumber]
    name_a=data_a["name"]
    description_a=data_a["description"]
    country_a=data_a["country"]
    print(f"Compare A: {name_a}, a {description_a}, from {country_a}\nVS")

def data_b_values():
    randomNumber=random.randint(0,len(Data)-1)
    data_b=Data[randomNumber]
    name_b=data_b["name"]
    description_b=data_b["description"]
    country_b=data_b["country"]
    print(f"Against B: {name_b}, a {description_b}, from {country_b}")


while not GAME_OVER:
    
    data_a_values()
    data_b_values()
    user_input=input("Whose has More Follower's? Type 'A' or 'B' ").lower()
    A=followers_a()
    B=followers_b()
    if user_input=='a' and A>=B:
        clear()
        SCORE.append(1)
        print(f"Correct! Score= {SCORE}")
    elif user_input =='b' and B>=A:
        clear()
        SCORE.append(1)
        print(f"Correct! Score= {SCORE}")
    else: 
        clear()
        print("Wrong!! 🤣")
        break

score=sum(SCORE)
if score<6:
    print(f"Your Score is {score} You Loose!😂🤣\n6 Score points are required to Win...")
    GAME_OVER=True
elif score>=6:
    print(f"You Win !! with 😍 {score} Number of Scores. ")
    GAME_OVER=True











