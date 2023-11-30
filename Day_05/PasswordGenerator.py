# import random
# # printing letter's from A-to-Z including small's and capital
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# numbers=['0','2','3','4','5','6','7','8','9']
# symbols=["!","@","#","$","%","^","&","*","+"]
# print("Welcome to the PyPassword Generator!")
# nr_letters=input("How many letters would like in your password: ")
# nr_letters=int(nr_letters)

# nr_symbols=int(input("How many symbol's you want in your password: "))
# nr_numbers=int(input("How many number's you want in your password: "))

# # Character's
# import random

# letters_length = len(letters)
# letters_length -= 1

# symbols_length = len(symbols)
# symbols_length -= 1

# numbers_length = len(numbers)
# numbers_length -= 1

# for a in range(nr_letters):
#     random_letter = random.randint(0, letters_length)
#     l_store = letters[random_letter]

#     for b in range(nr_symbols):
#         random_symbol = random.randint(0, symbols_length)
#         s_store = symbols[random_symbol]

#         for c in range(nr_numbers):
#             random_num = random.randint(0, numbers_length)
#             n_store = numbers[random_num]

# print(s_store + l_store + n_store)

    #   print(n_Store)

#Number's
# length_n=len(numbers)
# length_n-=1
# for i in range(0,nr_numbers):
#     randomNums=random.randint(0,length_n)
#     n_Store=numbers[randomNums]
#     print(n_Store)

# print(f"Your Password is: {l_Store}{s_Store}{n_Store}")
# import random

# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['0', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "+"]

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password: "))
# nr_symbols = int(input("How many symbols would you like in your password: "))
# nr_numbers = int(input("How many numbers would you like in your password: "))

# password = ""

# for _ in range(nr_letters):
#     random_letter = random.choice(letters)
#     password += random_letter

# for _ in range(nr_symbols):
#     random_symbol = random.choice(symbols)
#     password += random_symbol

# for _ in range(nr_numbers):
#     random_number = random.choice(numbers)
#     password += random_number

# shuffled_password = ''.join(random.sample(password, len(password)))

# print("Your generated password is:", shuffled_password)

import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers=['0','2','3','4','5','6','7','8','9']
symbols=["!","@","#","$","%","^","&","*","+"]
print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters you want in your password: "))
nr_symbols=int(input("How many symbols you want in your password: "))
nr_numbers=int(input("How many numbers you want in your password: "))
password=""
for char in range(nr_letters):
    password+=random.choice(letters)
for char in range(nr_symbols):
    password+=random.choice(symbols)
for char in range(nr_numbers):
    password+=random.choice(numbers)

randomPassword=''.join(random.sample(password,len(password))) 
print("Your Password is: ",randomPassword)