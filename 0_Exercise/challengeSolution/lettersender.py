# Create a letter using starting_letter.txt
# for each namme in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend"

import os
PLACE_HOLDER='["name"]'
folder_path=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\0_Exercise\\challengeSolution\\ready_to_send\\")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\0_Exercise\\challengeSolution\\invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\0_Exercise\\challengeSolution\\starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        striped_name=name.strip()
        new_letter=letter_contents.replace(PLACE_HOLDER,striped_name)
        # print(new_letter)
        with open(f"F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\0_Exercise\\challengeSolution\\ready_to_send\\letter_for_{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

