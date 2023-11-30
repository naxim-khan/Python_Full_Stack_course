
# Catching Exceptions Exercise. 
# Error file not found.

# with open ("a_file.txt") as file:
#     file.read() 
# try: something that might cause an Exception

import os

try:
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
    file_name = open("a_file.txt")
except FileNotFoundError:
    # Handle the FileNotFoundError here.
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_name = "a_file.txt"
    file_path = os.path.join(current_directory, file_name)
    with open(file_path, 'w') as new_file:
        new_file.write("Hi, I'm there")
except KeyError as error_message:
    # Handle the KeyError here.
    print(f"the key {error_message} does not exist.")
else:
    content=file_name.read()
    print(content)
finally:
    raise TypeError("This is the Error")




    