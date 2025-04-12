import requests
from twilio.rest import Client 

API_KEY = '16fb8560f0c501abec59b9b2768be345'
ACCOUNT_SID = 'Account SSID' # Sensitive Info
AUTH_TOKEN = 'Auth Token' # Sensitive Info

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
        from_="",
        to="",
        )
        unbrella_needed = True
        print(message.status)
    

