import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 34.025917 # Your latitude
MY_LONG = -71.560135 # Your longitude
my_email="PyBoy007@outlook.com"
password="Py@112233"

def is_iss_overhead():
    

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #If the ISS is close to my current position

    if MY_LAT-5 <=iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <=MY_LONG+5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >=sunset or time_now<=sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("Look Up!")
        connection=smtplib.SMTP("smtp.outlook.com")
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="syednimra92@gmail.com",
            msg="Subject:Look Up!\n\nThe ISS is above You in the sky."
        )
    else:
        print("not here")



