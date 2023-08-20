import datetime as dt
import os

import requests
from dotenv import load_dotenv

load_dotenv()
STOCK = "SNDL"
COMPANY_NAME = "SNDL Inc"
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

ALPHA_URL = "https://www.alphavantage.co/query"
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}
alpha_response = requests.get(url=ALPHA_URL, params=alpha_params, timeout=5)
alpha_response.raise_for_status()
data = alpha_response.json()

last_updated = data["Meta Data"]["3. Last Refreshed"]
last_close_price = data["Time Series (Daily)"][last_updated]["4. close"]

# counting the day before the last close price
last_updated_date = dt.date.fromisoformat(last_updated)
last_closing_minus_one = last_updated_date - dt.timedelta(days=1)

day_before_last_close_price = data["Time Series (Daily)"][str(last_closing_minus_one)][
    "4. close"
]

difference = float(last_close_price) - float(day_before_last_close_price)
movement = difference * 100 / float(day_before_last_close_price)
if movement > 2 or movement < -2:
    print(f"Get News, the movement is {movement}%")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
