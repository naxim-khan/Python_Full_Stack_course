import requests
import datetime


MY_LAT=34.025917
MY_LANG=71.560135

parameters={
    "lat":MY_LAT,
    "lang":MY_LANG,
    "formatted":0,
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json() 
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
# time_now=datetime.now()
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")


