import tkinter

window=tkinter.Tk()

#Creating title for window.
window.title("My First GUI Program")
# setting minimum size
window.minsize(width=500,height=300)
# setting max size
window.maxsize(width=500, height=300)
# Label's
my_label=tkinter.Label(text="I'm a Label", font=("Arial",24,"bold"))
# showing label in our window.
my_label.pack(expand="True") # side="left", side"bottom"




window.mainloop()