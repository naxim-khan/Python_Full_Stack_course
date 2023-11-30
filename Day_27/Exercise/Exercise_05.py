import tkinter

window=tkinter.Tk()
window.title("My GUI")
window.minsize(width="500",height="300")

# Label's

my_label=tkinter.Label(text="I'm a label",font=("Arial",20,"bold"))
my_label.pack()
# Below is the procedure that how can we update the property of 
# Particular componenet. that we've created.
my_label["text"]="New Text"




def clicked():
    # print("I got clicked>>>>>")
    # CHANGING THE LABEL TEXTS TO INPUT TEXTS
    new_text=input.get()
    my_label.config(text=new_text) 
   
# Entry
input= tkinter.Entry(width=30)
input.pack()

# Buttons

button = tkinter.Button(text="Click Me",command=clicked,activebackground="navy")
button.pack()



window.mainloop()
