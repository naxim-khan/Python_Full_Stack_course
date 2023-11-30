# when you clicked the button it should change the 
# label text's

import tkinter

window=tkinter.Tk()
window.minsize(width=500,height=300)
label=tkinter.Label(text="I'm a label",font=("Arial",20,"bold"))
label.pack()
def change_text():
    label.config(text="Don't Click me Again ")

button=tkinter.Button(text="Click Me",command=change_text)
button.pack()

window.mainloop()