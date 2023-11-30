import os
def clear():
    os.system('cls')

programming_dictionary={ #Key                  # Value
                        "bug"     : "An erro in a program that prevent the program from running as expected.",
                        "function": " A piece of Code that you can easily call over and over again",
                        "loop"    : " The Action of doing something over and ove Again."
                        }
# retrieving item's from dictionary.
while True:
    choice=input("Enter a word from below to know it's meaning \nBug, Function, Loop\n").lower()
    if choice == "bug":
        print("Bug : ",programming_dictionary["bug"])
    elif choice == "function":
        print("Function : ",programming_dictionary["function"])
    elif choice == "loop":
        print("Loop : ",programming_dictionary["loop"])
    else:
        print("Sorry You Enter Wrong Input!!")

    option=input("Exit, Continue\n").lower()
    if option=="exit":
        break
    else:
        clear()
        continue


# Adding new items to dictionar
# programming_dictionary["python"]="asldfkjdfj"

# Creating Empty Dictionary
# empty_dictionary={}
# Wipre an existing dictionary
# programming_dictionary={} just mention the name of the existing dictionary and set it's value to empty curley braces and all the data inside it will be wipe.

# Edit an item in a dctionary
# programming_dictionary["bug"] = "A moth in your computer."
# output: A moth in your computer.

# loop through a dictionary
# for thing in programming_dictionary:
#     print(thing," :",programming_dictionary[thing]) 
    # Out put: key with definition
    # print(thing) 
    # out put: only Key