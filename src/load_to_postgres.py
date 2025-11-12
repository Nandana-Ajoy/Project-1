import psycopg2
import pandas as pd

def load_data_to_postgres():
    connection = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="weather_db",
            user="postgres",
            password="CdY9u2g44",
            port="5432"
        )

        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS weather_data (
            time TIMESTAMP,
            temperature_c REAL,
            humidity_percent REAL,
            windspeed_ms REAL
        );
        """
        cursor.execute(create_table_query)

        df = pd.read_csv("clean_weather_data.csv")

        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO weather_data (time, temperature_c, humidity_percent, windspeed_ms) VALUES (%s, %s, %s, %s)",
                (row["time"], row["Temperature (°C)"], row["Humidity (%)"], row["Wind Speed (m/s)"])
            )

        connection.commit()
        print("Data successfully loaded into PostgreSQL database!")

    except Exception as e:
        print("Error:", e)

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    load_data_to_postgres()
