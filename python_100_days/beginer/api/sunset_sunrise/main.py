import requests

lausanne_lat = 46.520
lausanne_long = 6.620

API_URL = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": lausanne_lat,
    "lng": lausanne_long,
    "formatted": 0
}


response = requests.get(url=API_URL, params=parameters, timeout=5)
response.raise_for_status()
data = response.json()
sunrise =  data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f"Sunrise: {sunrise.split('T')[1].split('+')[0]} / Sunset: {sunset.split('T')[1].split('+')[0]}") 