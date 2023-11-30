alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
# __________ ENCRYPT __________
def encrypt(plain_text,shift_amount):
    cipher_text="" # creating empty to store the newly formed texts    
        
    for i in range(0,len(plain_text)):
        for letter in plain_text:
            position=alphabet.index(letter) # position of the letter in alphabet text
            new_position = position + shift_amount # Changing the letter eg. letter a=0, + shiftamount =5 0+5=5 a=e
            # new_letter=alphabet[new_position] # storing the new formed text in new_letter vairable. eg. a is now e
            cipher_text += new_position
    

    print(f"The encode text is ' {cipher_text} '")


# ------- INPUTS -----------
direction=input("Type 'encode' to encrypt type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

# _____ ENCRYPT ________
encrypt(text,shift)