# Miles to KM converter.
from tkinter import *


window=Tk()
window.resizable(width=True,height=True)
window.config(padx=20,pady=20)
window.title("Miles to KM Converter")
icon_path=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_27\\Project\\icon.ico")
window.iconbitmap(icon_path)
def configure_grid(event):
    width=event.width
    height=event.height
    window.columnconfigure(0,weight=width)
    window.columnconfigure(0,weight=height)

window.bind("<Configure>",configure_grid)

# Entry
entry=Entry()
entry.grid(column=2,row=0)
label1=Label(text="Miles")
label1.grid(column=3,row=0)
label2=Label(text="is equal to")
label2.grid(column=0,row=1)
result=Label(text=0,)
result.grid(column=2,row=1)
label3=Label(text="Km")
label3.grid(column=3,row=1)

def miles_to_km():
    miles=int(entry.get())
    km=round(miles * 1.60934)
    result["text"]=km


button=Button(text="Calculate",command=miles_to_km)
button.grid(column=2,row=2)




window.mainloop()