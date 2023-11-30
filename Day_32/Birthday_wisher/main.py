from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL="PyBoy007@outlook.com"
PASSWORD="Py@112233"

today=datetime.now()
today_tuple=(today.month,today.day)

data=pandas.read_csv("birthdaytxts.csv")
birthdays_dict={(data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]", birthday_person["name"])

    connection=smtplib.SMTP("smtp.outlook.com",port=587)
    connection.starttls()
    connection.login(MY_EMAIL,PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=birthday_person["email"],
        msg=f"Subject:Happy birthday to me!\n\n{contents}"
        )
    
    connection.quit()

    

     
