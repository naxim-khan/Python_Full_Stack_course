from tkinter import *
from tkinter import messagebox
import pyperclip
import os
from random import random,randint,choice,shuffle
import json


FONTS = "Nunito"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numbers=['0','2','3','4','5','6','7','8','9']
    symbols=["!","@","#","$","%","^","&","*","+"]

    r_letters=[choice(letters) for _ in range(randint(8,10))]
    r_symbols=[choice(symbols) for _ in range(randint(2,4))]
    r_numbers=[choice(numbers) for _ in range(randint(2,4))]

    password_list=r_letters+r_symbols+r_numbers
    password="".join(password_list)
    # insert generated password into password entry box
    pass_entry.insert(0,password)
    # copy generated password.
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # file_name = os.path.join(script_directory, "data.json")
    file_name="F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_30\\Exercises\\3_password_manager_update\\data.json"
    
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data={website:{
        "email":email,
        "password":password,
    }}
    while True:
        if len(website)==0:
            messagebox.showinfo(title="OOPs (EMPTY WEB FIELD)",message="Hey!dont leave any of the field empty.")
            website_entry.focus()
            break
        elif len(email)==0:
            messagebox.showinfo(title="OOPs (EMPTY EMAIL FIELD)",message="Hey!dont leave any of the field empty.")
            email_entry.focus()
            break
        elif len(password)==0 or len(password)<2:
            messagebox.showinfo(title="OOPs (short/empty Password field!)",message="Password needs to be at least 5 characters or more.")
            pass_entry.delete(0,END)
            pass_entry.focus()
            break
        else:
            is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered:\n{email}\n{password}\nIs it Ok to save?")
            if is_ok:
                try:
                    with open(file_name, "r") as file:
                        # Reading old data
                        data=json.load(file)
                    
                except FileNotFoundError:
                         # If file does not exist, create an empty data dictionary
                    data = {}

                # Add the new data to the existing data dictionary
                new_data = {website: {"email": email, "password": password}}
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

                website_entry.delete(0, END)
                pass_entry.delete(0, END)
                website_entry.focus()
                break

# _______________________ find password ------------------------
def find_password():
    website=website_entry.get()
    website.capitalize()
    with open("data.json") as data_file:
        data=json.load(data_file)
        # print(data)
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
            pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
icon_path = "F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_30\\Exercises\\3_password_manager_update\\iconlogo.ico"
window.minsize(width=650, height=450)
window.maxsize(width=650, height=450)

window.config(padx=20, pady=20, bg="#6528F7")  # Set background color to a light gray

window.iconbitmap(icon_path)
window.title("Password Manager")

# Styling the fonts and colors
title_font = (FONTS, 20, "bold")
label_font = (FONTS, 12,"bold")
entry_font = (FONTS, 12)
button_font = (FONTS, 12, "bold")

label_bg_color = "#6528F7"
entry_bg_color = "#A076F9"
button_bg_color = "#A076F9"
button_hover_color = "#EDE4FF"
button_text_color = "#6528F7"

# creating image using canvas widget
canvas = Canvas(width=200, height=200, bg="#6528F7", highlightthickness=0)
image_path = PhotoImage(file="F:\\U-DEMY-COURSES\My_programms\\2nd_file\\Day_30\\Exercises\\3_password_manager_update\\logo.png")
canvas.image = image_path
canvas.create_image(100, 100, image=image_path,)
canvas.grid(row=0, column=1, sticky='s')  # Use columnspan to make the canvas span 3 columns

# label's.
website_label = Label(text="Website:", font=label_font, bg=label_bg_color,fg="#D7BBF5")
email_label = Label(text="Email/Username:", font=label_font, bg=label_bg_color,fg="#D7BBF5")
pass_label = Label(text="Password:", font=label_font, bg=label_bg_color,fg="#D7BBF5")

# Label grids.
website_label.grid(column=0, row=1, sticky="w", padx=(0, 10))
email_label.grid(column=0, row=2, sticky="w", padx=(0, 10))
pass_label.grid(column=0, row=3, sticky="w", padx=(0, 10))

# label Entries
website_entry = Entry(width=35, font=entry_font, bg=entry_bg_color, borderwidth=0)
website_entry.focus()
email_entry = Entry(width=35, font=entry_font, bg=entry_bg_color, borderwidth=0)
email_entry.insert(END, "nazeemkhanpk@gmail.com")
pass_entry = Entry(width=35, font=entry_font, bg=entry_bg_color, borderwidth=0)  # Set the width to match the other Entry widgets

# Entries Grid
website_entry.grid(column=1, row=1, columnspan=2, sticky="w", pady=5)  # Use columnspan to make the website Entry span 3 columns
email_entry.grid(column=1, row=2, columnspan=2, sticky="w", pady=5)  # Use columnspan to make the email Entry span 3 columns
pass_entry.grid(column=1, row=3, sticky="w", pady=5)  # Use columnspan to make the password Entry span 2 columns

# Buttons
search_btn=Button(text="Search", font=button_font, bg=button_bg_color, fg=button_text_color, activebackground=button_hover_color, command=find_password, width=31)
generate_password_btn = Button(text="Generate Password", font=button_font, bg=button_bg_color, fg=button_text_color, activebackground=button_hover_color, command=generate_password, width=31)
add = Button(text="Add", font=button_font, bg=button_bg_color, fg=button_text_color, activebackground=button_hover_color, command=save_password, width=31)

# Buttons grid
search_btn.grid(column=1, row=4, columnspan=2, sticky="w", pady=5)
generate_password_btn.grid(column=1, row=5, pady=5, sticky="w")  # Use sticky="e" to align the button to the right
add.grid(column=1, row=6, columnspan=2, sticky="w", pady=5)  # Use columnspan=2 and sticky="w" to make the "Add" button span 2 columns


# Adjust column weight to keep password Entry in the middle and button fixed at the right
window.grid_columnconfigure(1, weight=1)


# Adjust column weights to keep password Entry in the middle
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()
