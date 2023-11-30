import os
from art import logo
def clear():
    os.system('cls')

print(logo)
print("Welcome to the secret auction program.")
auction_list={}

# def adding_people(names,bidPrice):
#     new_dic={}
#     new_dic["Name"]=names
#     new_dic["Bid_Price"]=bidPrice
#     auction_list.append(new_dic)

def find_high(bidding_record):
    highest_bid=0
    winner = ""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
            clear()
    print(f"The Winner is {winner}, with a bid of ${highest_bid}")


while True:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))
    # adding_people(name,bid)
    auction_list[name]=bid
    option=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if option=="no":
        find_high(auction_list)
        break
    else:
        clear()
        continue

# length=len(auction_list)
# for i in range(0,length):
#     print(auction_list[i])
# print(auction_list)