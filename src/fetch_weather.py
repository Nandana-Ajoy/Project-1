import requests
import json
import datetime

def fetch_weather_data():
    latitude = 8.5241
    longitude = 76.9366


    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relativehumidity_2m,windspeed_10m",
        "timezone": "Asia/Kolkata"
    }

    print("Fetching weather data...")
    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()
    print("Data fetched successfully!")

    with open("raw_weather_data.json", "w") as f:
        json.dump(data, f, indent=4)

    return data

if __name__ == "__main__":
    fetch_weather_data()



