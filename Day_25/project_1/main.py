import turtle
import pandas
import pygetwindow as gw
import time

SCORE=0

screen=turtle.Screen()
screen.setup(width=700, height=500)
icon=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_25\\project_1\\art profile.ico")
# changing icon
window = screen.getcanvas().winfo_toplevel()
window.iconbitmap(icon)

image = "F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_25\\project_1\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.goto(0,0)
tim=turtle.Turtle()


# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# answer_state=screen.textinput(title="Guess the State",prompt="What's another state's name? ").capitalize()
data=pandas.read_csv("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_25\\project_1\\50_states.csv")
states = data["state"].tolist()
missing_states_file=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_25\\project_1\\missing_states.csv")
game_is_on=True
guessed_states=[]
while game_is_on:
    counter=50
    # time.sleep(0.1)
   
    
    answer_state=screen.textinput(title=f"{SCORE}/{counter}Guess the State",prompt="What's another state's name? ").title()
    # answer_state=states[SCORE]
    if answer_state=="Exit":
        missing_states=[state for state in states if state not in guessed_states]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv(missing_states_file)
        turtle.bye()
        break

    if answer_state in states:
        # Get the row for the answer state
        state_row = data[data["state"] == answer_state]
        # Get the location coordinatesa
        x = int(state_row["x"].values[0])
        y = int(state_row["y"].values[0])
        guessed_states.append(answer_state)
        tim.pu()
        tim.hideturtle()
        tim.goto(x,y)
        tim.write(answer_state)
        SCORE+=1
        counter -= 1
    

# screen.exitonclick()
turtle.mainloop()
