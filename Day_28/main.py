from tkinter import *
import math
import pygame
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Nunito"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps= 0
timer= None


# ___________ sounds paths ___________
def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

start_sound = "F:/U-DEMY-COURSES/My_programms/2nd_file/Day_28/sounds/start_sound.mp3"
beep_sound="F:/U-DEMY-COURSES/My_programms/2nd_file/Day_28/sounds/beep.mp3"
checkmarksound="F:/U-DEMY-COURSES/My_programms/2nd_file/Day_28/sounds/tickmark.mp3"


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # play_sound(start_sound)
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global start_sound
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="L Break" ,fg=RED)
        for _ in range(3):
            play_sound(beep_sound)
            time.sleep(1)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="S Break" ,fg=PINK)
        for _ in range(2):
            play_sound(beep_sound)
            time.sleep(1)
    else:
        # play_sound(start_sound)
        count_down(work_sec)
        title_label.config(text="Work" ,fg=GREEN)
        
            
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec < 10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    # timer_label.config(text=f"{count_min}:{count_sec}")

    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            play_sound(checkmarksound)
            marks +="✔"
        check_mark.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro By Nazeem")
window.config(padx=100,pady=50,background=YELLOW)

icon_path=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_28\\tomato.ico")
window.iconbitmap(icon_path)
# adding image 
image_path=PhotoImage(file="F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_28\\tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image=image_path) # x=100,y=112
timer_text=canvas.create_text(105,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
# timer text
title_label=Label(text="Timer" ,font=(FONT_NAME,35,"bold"),bg=YELLOW,fg=GREEN)
title_label.grid(column=1,row=0)


# buttons hover effects
def change_cursor(event):
    event.widget.config(cursor="hand2", foreground=GREEN)


def restore_cursor(event):
    event.widget.config(cursor="",foreground="black")

# buttons
# start button
start_btn=Button(text="START",font=(FONT_NAME,15,'bold'),bg=YELLOW,activeforeground=RED,borderwidth=0,relief="flat",activebackground=YELLOW,command=start_timer)
start_btn.bind("<Enter>", change_cursor)
start_btn.bind("<Leave>", restore_cursor)
# reset button
reset_btn=Button(text="RESET",font=(FONT_NAME,15,'bold'),bg=YELLOW,activeforeground=RED,borderwidth=0,relief="flat",activebackground=YELLOW,command=reset_timer)
reset_btn.bind("<Enter>", change_cursor)
reset_btn.bind("<Leave>", restore_cursor)
start_btn.grid(column=0,row=2)
reset_btn.grid(column=2,row=2)

# tick mark
check_mark=Label(text="",font=(FONT_NAME,15,"bold"),bg=YELLOW,fg=GREEN)
check_mark.grid(column=1,row=3)

# Main Loop
window.mainloop()
