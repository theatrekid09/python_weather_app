import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

city = input('Enter a city: ')

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+os.getenv('API_KEY')+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)