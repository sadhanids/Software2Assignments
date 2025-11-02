import requests
import json


API_KEY = "134953a5d8b4eb107baf0f732e9b8ce1"
request_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter the name of the municipality: ").strip()
if not city:
    print("No City Entered")
request_url1 = f"{request_url}?q={city}&appid={API_KEY}"
try:
    response = requests.get(request_url1)
    data = response.json()
except requests.excepetions.RequestException:
    print ("Failed to connect to the weather service")

if 'main' in data and 'weather' in data and data['weather']:
    temperature_kelvin = data['main']['temp']
    description = data['weather'][0]['description']

    temp_celsius = temperature_kelvin - 273.15

    print("------Current Weather Reports------")
    print(f"Municipality: {city}")
    print(f"Condition: {description}")
    print(f"Temperature: {temp_celsius:.2f}C")





