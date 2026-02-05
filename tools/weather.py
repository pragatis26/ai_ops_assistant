import os
import requests

def weather_lookup(city: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return {"error": "OPENWEATHER_API_KEY not set"}

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return {
            "error": "Weather API failed",
            "details": data
        }

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
