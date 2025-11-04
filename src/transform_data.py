import pandas as pd
import json

def transform_weather_data():
    with open("raw_weather_data.json", "r") as f:
        data = json.load(f)

    hourly_data = data.get("hourly", {})
    df = pd.DataFrame(hourly_data)

    df["time"] = pd.to_datetime(df["time"])

    df = df.drop_duplicates()

    df.rename(columns={
        "temperature_2m": "Temperature (°C)",
        "relativehumidity_2m": "Humidity (%)",
        "windspeed_10m": "Wind Speed (m/s)"
    }, inplace=True)

    df.to_csv("clean_weather_data.csv", index=False)
    print("Cleaned weather data saved to clean_weather_data.csv")

if __name__ == "__main__":
    transform_weather_data()
