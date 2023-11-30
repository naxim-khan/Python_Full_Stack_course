import requests
from twilio.rest import Client

parameters={
    "lat":34.015137,
    "lon":71.524918,
    # "q":"peshawar",
    "exclude":"current,minutely,daily",
    # "appid":"68a1c9816b8860b954ffe4ea44d455c6",
    "appid":"69f04e4613056b159c2761a9d9e664d2"
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
weather_data=response.json()
weather_slice= weather_data["hourly"][:12]
# message sending process  
account_sid="AC521309319f19dd461d996b0064549b19"
auth_token="f449a0aab35193bdf400029c402f596e"

will_rain=False

for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True

if will_rain:
    client=Client(account_sid,auth_token)
    message=client.messages \
    .create(
        body="It's going to rain today. Remember to bring an ☔ ",
        from_= "+447700141746",
        to="+447732883108 "
        
    )
   
    print(message.status)
else:
    client=Client(account_sid,auth_token)
    message=client.messages \
    .create(
        body="It's not going to rain today. Remember to  keep your ☔  at 🏡 ",
        from_= "+447700141746",
        to="+447732883108"
        
    )
    print(message.status)