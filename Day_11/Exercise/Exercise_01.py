import random
"""
 Black Jack Rules:
 the deck is unlimited in size.
 the Jack/Queen/King all count as 10.
 the Ace can count as 11 or 1.
 Use the following list as the deck of cards:
 The cards in the list have equal probability of being drawn.
 cards are not removed from the deck as they are drwan.
"""
# cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,10]
# create a deal_card() function that uses the lsit below to *return*
# a random card. 11 is the Ace.
# cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card():
    """Return a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

# print(deal_card())
# next: Deal the user and computer 2 cards each using deal_card()
def calculate_score(cards):
    """Take a list of cards and return a score calculated from the cards."""
# Inside Calculate_score() check for a blackjack (a hand with only 2 cards: ace+10) and return 0 instead of the actual score. 0 will represent a black jack in our game.
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    
# Hint: Inside calculate_score() check for 11 (ace). if the score is already over 21, remove the 11 and replace it with a 1. you might need to look up append() and remove().
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)



    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw 🙃"
    elif computer_score== 0:
         return "Lose, opponent has BlackJack 😱"
    elif user_score==0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went Over. You lose 😂"
    elif computer_score > 21:
        return "Opponent went over. You win 🙄"
    elif user_score > computer_score:
        return "You win 🤥🦾"
    else:
        return "You lose 🤣"
    
user_cards=[]
computer_cards=[]
is_game_over=False
for _ in range(2):
    # new_card=deal_card()
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
     # Call calculate_score(). if the computer of the user has a blackjack (0). or if the user's score is over 21, then the game ends.
while not  is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score:{user_score}")
    print(f"Computer's first cards: {computer_cards[0]}")

    if user_score==0 or computer_score== 0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal =="y":
            user_cards.append(deal_card())
        else:
            is_game_over=True
    # print(user_cards)
    # print(computer_cards)
    # Create a function called calculate_score() that takes a list of cards 
    # as input and return the score.
    # lookup the sum function to help you do this.

# once the user is done, it's time to let the computer play. The  and comp
# computer should keep drawing cards as long as it has a score less than 17. 
while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

print(compare(user_score,computer_score))
