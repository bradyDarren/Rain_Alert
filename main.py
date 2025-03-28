import requests

API_KEY = '16fb8560f0c501abec59b9b2768be345'

parameters = {
    'lat': 29.7589,
    'lon': -95.3677,
    'appid': API_KEY
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast??', params=parameters)
response.raise_for_status()

data = response.json()
print(data)