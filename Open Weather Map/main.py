import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = os.getenv("OWM_ENDPOINT")
API_KEY = os.getenv("API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_PHONE = os.getenv("FROM_PHONE")
TO_PHONE = os.getenv("TO_PHONE")

weather_params = {
    "lat":31.046051,
    "lon":34.851612,
    "appid":API_KEY,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body="It's going to rain today. Remember to bring an umbrella.", from_=FROM_PHONE,
        to=TO_PHONE)

    print(message.status)
