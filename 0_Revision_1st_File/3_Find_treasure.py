print("Welcome Treasure Island Game")

print("Your Mission is to find the treasure")

while True:
    user_input=input("You're at a cross road. Where do you want to go? Type 'Left' or 'right': ").lower()
    if user_input=="left":
        user_input2=input("You came to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat🚤 . Type 'swim' to swim 🏊‍♂️across: ").lower()
        if user_input2=="wait":
            user_input3=input("You arrive at the island 🏝 unharmed. There is a house 🏘 with 3 doors 🚪. One red 🟥, one yellow🟨 and one blue 🟦. Which color do you choose?")
            if user_input3=="blue":
                print("Congratulation's You find a box full of Diamonds. 💎🔷💍")
                break
            else:
                print("It's a room full of fire 🔥🎇🎆🔥, Game Over !!!")
                break
        else:
            print("Shark attacked on You and cut your throat 🦈 . Game Over!!!")
            break
    else:
        print("You fall into a sea 🌊. Game over!!! 🎲")
        break
    



