import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def clear():
    os.system('cls')

# Emerging work of two functin's into one function
def ceaser(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
            shift_amount *= -1
            # 5* -1 = -5
    for letter in start_text:
        position=alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is ' {end_text} '")
    

# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position = position +shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encode text is ' {cipher_text} '")

# def decrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position = position -shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The decode text is ' {cipher_text} '")



# ------- INPUTS ----------

print('''
  /$$$$$$                                                /$$$$$$  /$$           /$$                          
 /$$__  $$                                              /$$__  $$|__/          | $$                          
| $$  \__/ /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$       | $$  \__/ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$      |____  $$ /$$_____/ /$$__  $$ /$$__  $$      | $$      | $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$       /$$$$$$$|  $$$$$$ | $$$$$$$$| $$  \__/      | $$      | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$    $$/$$__  $$ \____  $$| $$_____/| $$            | $$    $$| $$| $$  | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$            |  $$$$$$/| $$| $$$$$$$/| $$  | $$|  $$$$$$$| $$      
 \______/ \_______/|_______/  \_______/|__/             \______/ |__/| $$____/ |__/  |__/ \_______/|__/      
                                                                     | $$                                    
                                                                     | $$                                    
                                                                     |__/                                    

''')
while True:
    direction=input("Type 'encode' to encrypt type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    # clear()
    ceaser(text,shift,direction)
    # if direction=="encode":
    #     encrypt(text,shift)
    # else:
    #     decrypt(text,shift)
    
    choice=input("Exit 'or' Continue\n").lower()
    if choice =="exit":
        break
