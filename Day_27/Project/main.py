from tkinter import *
from tkinter import ttk
window = Tk()
window.resizable(width=True, height=True)
window.config(padx=20, pady=20)
window.title("Miles to KM Converter")

def configure_grid(event):
    width = event.width
    height = event.height
    window.columnconfigure(0, weight=1)  # Make column 0 resize horizontally
    window.columnconfigure(1, weight=1)  # Make column 1 resize horizontally
    window.columnconfigure(2, weight=1)  # Make column 2 resize horizontally
    window.rowconfigure(0, weight=1)     # Make row 0 resize vertically
    window.rowconfigure(1, weight=1)     # Make row 1 resize vertically
    window.rowconfigure(2, weight=1)     # Make row 2 resize vertically

window.bind("<Configure>", configure_grid)

entry = Entry()
entry.grid(column=1, row=0, padx=10, pady=10)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

result = Label(text=0)
result.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

def miles_to_km():
    miles = int(entry.get())
    km = round(miles * 1.60934)
    result["text"] = km

# Create a custom style for the button
def miles_to_km():
    miles = int(entry.get())
    km = float(miles * 1.60934)
    result["text"] = km

def on_button_hover(event):
    button["bg"] = "gray"

def on_button_leave(event):
    button["bg"] = "blue"

button = Button(text="Calculate", command=miles_to_km, bg="blue", fg="white")
button.grid(column=1, row=2, columnspan=2, padx=10, pady=10)

# Bind hover and leave events to the button
button.bind("<Enter>", on_button_hover)
button.bind("<Leave>", on_button_leave)

window.mainloop()
