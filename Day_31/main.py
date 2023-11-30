from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
file_path=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_31\\images\\")
# ____________ FUNCTIONS(COMMANDS) ____________
flip_timer=3000
data_file_path=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_31\\data\\french_words.csv")
data=pandas.read_csv(data_file_path)
to_learn=data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(3000,func=flip_card)
    

def flip_card():
    global current_card
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_image)

def is_known():
    global file_path
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("2nd_file/Day_31/data/words_to_learn.csv")
    next_card()


    
# ______________ UI ________________
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
file_path=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_31\\images\\")

card_front_img=PhotoImage(file="F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_31\\images\\card_front.png")
card_back_image=PhotoImage(file="F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_31\\images\\card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,150, text="",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
cross_image=PhotoImage(file=file_path+"wrong.png")
unkown_button=Button(image=cross_image,highlightthickness=0,borderwidth=0,command=next_card)
unkown_button.grid(row=1,column=0)

check_image=PhotoImage(file=file_path+"right.png")
known_button=Button(image=check_image,highlightthickness=0,borderwidth=0,command=is_known)
known_button.grid(row=1,column=1)
#  next card
next_card()
# ____



window.mainloop()