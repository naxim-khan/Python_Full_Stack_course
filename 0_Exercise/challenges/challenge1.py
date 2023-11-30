# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend"
import os
def creating_letter():
    names=[]

    folder_path=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\0_Exercise\\challenges\\readyTosend")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    with open("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\0_Exercise\\challenges\\invitednames.txt",)as letter:
            invitednames=letter.read().splitlines()
            # for i in range(len(invitednames)):
            #      names.append(invitednames[i])
            names=invitednames
                 
                 
    for i in range(len(names)):
        filename = "Letter_for_" + names[i]+ ".txt"
        file_path = os.path.join(folder_path, filename)  # Create the full file path

        with open("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\0_Exercise\\challenges\\starting_letter.docx",)as letter:
            letter=letter.read()

        with open(file_path, mode="w") as filename:
            filename.write(f"Dear {names[i]}\n{letter}")
                                      
            

creating_letter()