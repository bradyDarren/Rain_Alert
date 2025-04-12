import requests
import os 
from twilio.rest import Client 

API_KEY = os.environ.get('OWM_API_KEY')
ACCOUNT_SID = os.environ.get('OWM_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('OWM_AUTH_TOKEN')

parameters = {
    'lat': 29.7589,
    'lon': -95.3677,
    'appid': API_KEY,
    'cnt':4
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast??', params=parameters)
response.raise_for_status()

data = response.json()
weather_data = data['list']

unbrella_needed = False

for time in range(len(weather_data)):
    weather_id = weather_data[time]['weather'][0]['id']
    if weather_id < 700 and not unbrella_needed: 
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
        body="It's going to rain today, Remeber to bring an ☔️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+17135828104",
        )
        unbrella_needed = True
        print(message.status)
    

