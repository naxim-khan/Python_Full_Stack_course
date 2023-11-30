import requests
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from googletrans import Translator
from twilio.rest import Client



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY="P59TU161XY0IV4D6"

# stock prices section.
def stockPrices():
    parameters={
        "apikey":"P59TU161XY0IV4D6",
        "function":"TIME_SERIES_DAILY",
        "symbol":STOCK,

    }
    url=f"https://www.alphavantage.co/query?"
    response=requests.get(url="https://www.alphavantage.co/query?",params=parameters)
    response.raise_for_status()
    data=response.json()
    current_date = datetime.now().date()
    refreshed_date=data["Meta Data"]["3. Last Refreshed"]
    yesterday = refreshed_date
    day_beforeyesterday=yesterday[:-1] + str(int(yesterday[-1]) - 1)

    current_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
    previous_close = float(data["Time Series (Daily)"][day_beforeyesterday]["4. close"])
    percentage_change = ((current_close - previous_close) / previous_close) * 100

    return percentage_change


# Fetch news
def collected_news():
    current_date = datetime.now().date()

    news_params = {
        "date": current_date,
        "apikey": "6f4ec88749de44d9a6efa58bc84b5f95",  
    }

    news_r = requests.get(url="https://newsapi.org/v2/top-headlines?q=tesla&sortBy=publishedAt", params=news_params)
    news_r.raise_for_status()
    news = news_r.json()

    # Check if news articles are available
    if "articles" in news and len(news["articles"]) > 0:
        article = news["articles"][0]
        headline = article["title"]
        description = article["content"]

        # Initialize the translator
        translator = Translator()

        # Detect the language of the input text
        detected_language_headline = translator.detect(headline).lang
        detected_language_description = translator.detect(description).lang

        # Translate the text to English
        if detected_language_headline != 'en':
            headline = translator.translate(headline, src=detected_language_headline, dest='en').text

        if detected_language_description != 'en':
            description = translator.translate(description, src=detected_language_description, dest='en').text

        return f"Headline:{headline}.\nDescription: {description}"
    else:
        return f"No news articles found."
    

percentage_change=stockPrices()
account_sid = 'AC521309319f19dd461d996b0064549b19'
auth_token = 'f449a0aab35193bdf400029c402f596e'

if percentage_change>0:
    increase_msg=f"TSLA: 🔺 { percentage_change:.2f}\n{collected_news()}%",
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+447700141746',
    body=increase_msg,
    to='+447732883108'
    )
    print("send decrease")

elif percentage_change<0:
    message=f"TSLA: 🔻 { percentage_change:.2f}\n{collected_news()}%"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+447700141746',
    body=message,
    to='+447732883108'
    )
    print("send drecrease")

print(message.sid)

"""

TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

