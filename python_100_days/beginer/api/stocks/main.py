import datetime as dt
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from dotenv import load_dotenv

load_dotenv()
STOCK = "SNDL"
COMPANY_NAME = "SNDL Inc"
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

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


NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_URL = "https://newsapi.org/v2/everything"

today = dt.date.today().strftime("%Y-%m-%d")
five_days_ago = str(dt.date.today() - dt.timedelta(days=5))

news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

news_response = requests.get(url=NEWS_URL, params=news_params, timeout=5)
news_response.raise_for_status()
news_data = news_response.json()
# last 3 articles
articles = news_data["articles"][:3]
email_body = ""
for article in articles:
    email_body += article["title"].upper() + "\n"
    email_body += article["description"] + "\n"
    email_body += article["url"] + "\n\n"

msg = MIMEMultipart()
msg["Subject"] = f"{COMPANY_NAME} News | {movement}%"
msg.attach(MIMEText(email_body, "plain"))

MY_EMAIL = os.getenv("MY_EMAIL")
MY_DESTINATION_EMAIL = os.getenv("MY_DESTINATION_EMAIL")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
if MY_EMAIL and MY_DESTINATION_EMAIL and MY_EMAIL_PASSWORD:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=MY_DESTINATION_EMAIL, msg=msg.as_string()
        )
        print("Email sent!")
