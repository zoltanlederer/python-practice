import requests
import os
from dotenv import load_dotenv

load_dotenv()

CITIES = {
    "budapest": {"latitude": "47.4984", "longitude": "19.0404"},
    "london": {"latitude": "51.5074", "longitude": "-0.1278"},
}

print(CITIES)

city = os.getenv('CITY')

if city not in CITIES:
    city = 'london'

latitude = CITIES[city]['latitude']
longitude = CITIES[city]['longitude']

api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m'

response = requests.get(api_url)
data = response.json()
current_date = data['current']['time']
current_temperature = data['current']['temperature_2m']

print(latitude)
print(longitude)
print(api_url)
print(current_date)
print(current_temperature)

