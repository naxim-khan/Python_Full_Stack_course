from tkinter import *
import requests
def quote():
    response=requests.get(url="http://api.kanye.rest/")
    response.raise_for_status()
    quote=response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)
    

bg_path="F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_33\\Challenges\\background.png"
kanye_img="F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_33\\Challenges\\kanye.png"

# _______ CREATING UI _________

window=Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img=PhotoImage(file=bg_path)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)
kanye_img = PhotoImage(file=kanye_img)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=quote,borderwidth=0)
kanye_button.grid(row=1, column=0)



window.mainloop()
