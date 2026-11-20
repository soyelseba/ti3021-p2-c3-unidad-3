import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_url = "https://api.weatherapi.com/v1/current.json"
api_key = f"?key={ os.getenv("weather_api_token") }"
ciudad = "&q=Santiago"
try:
    res = requests.get(api_url+api_key+ciudad, timeout=10)
    data = res.json()
    print(data)
except requests.exceptions.Timeout:
    print("Timeout")