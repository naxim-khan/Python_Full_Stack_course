# 3 basic component to arrange your component's 
# Pack , place, grid.
from tkinter import *

window=Tk()
window.title("My GUI")
window.minsize(width="500",height="300")
# adding padding to all the widgets
window.config(padx=100,pady=200)

# Label's

my_label=Label(text="I'm a label",font=("Arial",20,"bold"))
# my_label.config("New Text")
# my_label.pack()
# my_label.place(x=20,y=0) # top right corner
my_label.grid(column=0,row=0) # first column first row
my_label.config(padx=50,pady=50)






   
# Entry
input = Entry(width=30)
# input.pack()
input.grid(column=3,row=3)

# # Buttons
def clicked():
    # print("I got clicked>>>>>")
    # CHANGING THE LABEL TEXTS TO INPUT TEXTS
    new_text=input.get()
    my_label.config(text=new_text) 

button = Button(text="Click Me",command=clicked,activebackground="navy")
button.grid(column=1,row=2)

new_button = Button(text="New button",command=clicked,activebackground="navy")
new_button.grid(column=2,row=0)



window.mainloop()
