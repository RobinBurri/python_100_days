import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

OWD_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("API_KEY")

params = {
    "lat": 46.520,
    "lon": 6.632,
    "appid": API_KEY,
    "units": "metric",
}


def get_weather():
    res = requests.get(OWD_URL, params=params, timeout=5)
    res.raise_for_status()
    weather_data = res.json()

    main = weather_data["weather"][0]["main"]
    description = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]

    if temp > 20:
        message = client.messages.create(
            from_="+18149291349",
            body=f"today it is mainly: {main}, {description}.\nThe temperature is: {temp}°C",
            to="+41789072728",
        )
        print(message.status)
    else:
        print(
            f"today it is mainly: {main}, {description}.\nThe temperature is: {temp}°C"
        )


get_weather()
