import smtplib
import pandas as pd
import random
import datetime as dt

PLACE_HOLDER="[NAME]"
MY_EMAIL="PyBoy007@outlook.com"
PASSWORD="Py@112233"




def send_message():
    global PLACE_HOLDER
    global MY_EMAIL
    global PASSWORD
    name=input("Enter name:")
    file_path="F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_32\\"
    with open(file_path+"birthdaytxts.txt", "r") as letter:
        letter=letter.read()

    # Replace the [NAME] placeholder with the entered name
    letter = letter.replace(PLACE_HOLDER, name)

    with open (file_path+f"letter_for_{name}.txt" , "w") as let:
        let.write(f"{letter}")

    with open (file_path+f"letter_for_{name}.txt" , "r") as sending_letter:
        message=sending_letter.read()

    connection=smtplib.SMTP("smtp.outlook.com",port=587)
    connection.starttls()
    connection.login(MY_EMAIL,PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs="syednimra92@gmail.com",msg=f"Subject:Happy Birthday!\n\n{message}")
    connection.quit()

month=dt.datetime.now().month
day=dt.datetime.now().day
hour = dt.datetime.now().hour
minute = dt.datetime.now().minute
# You can set the date minute according to your birthday
if month==7 and day==28:
    if hour==hour and minute==minute: 
        send_message()
        print("send Successfully!!!!!!!")
    else:
        print("not the correct time to send")
else:
    print("Not correct month and date to send")




