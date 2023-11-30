from tkinter import *

# Creating a new window
Window=Tk()
Window.title("Widget Examples.")
Window.minsize(width="500",height="500")

# Label
label=Label(text="This is old text")
label.config(text="This is new text")
label.pack()

def action():
    print("Do something")

# Call action() when pressed
button=Button(text="Click Me",command=action)
button.pack()

# Entries
entry=Entry(width=30)
# Add some texts to begin with
entry.insert(END,string="Some text to begin with")
# Gets text in entry
print(entry.get())
entry.pack()
# Text
text=Text(height=5,width=30)
# puts cursor in textbox
text.focus()
# Adds some text to begin with. 
text.insert(END,"Example of multi-line text entry.")
# Get's current value in textbox at line1, character 0
print(text.get("1.0",END))
text.pack()

# Spinbox
def spinbox_used():
    # gets current value in spinbox.
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.
def scale_used(value):
    print(value)

scale=Scale(from_=0,to =100,command=scale_used)
scale.pack()

# check button

def checkbutton_used():
    # prints 1 if on button chedk,
    # otherwise 0
    print(check_state.get())
    
# variable to hold on to checked state, 0 is off, 1 is on
check_state=IntVar()
checkbutton=Checkbutton(text="Is on?",variable=check_state,command=checkbutton_used)
check_state.get()
checkbutton.pack()


# Radio Buttons
def radio_used():
    print(radio_state.get())

# Variavle to hold on to which radio button value is checked.
radio_state=IntVar()
radiobutton1=Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
radiobutton2=Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# list box
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox=Listbox(height=4)
fruits=["Apple","Pear","Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
    
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()








Window.mainloop()