# Weather Data Pipeline 

This project demonstrates an **end-to-end data pipeline** for weather data collection, cleaning, transformation, and storage using Python and PostgreSQL.  
The pipeline fetches hourly weather data from the **Open-Meteo API** for Trivandrum, cleans it, and loads it into a PostgreSQL database using a relational schema.  



## Tech Stack

- **Python**: `requests`, `pandas`, `psycopg2`  
- **PostgreSQL**: Relational database  
- **Docker** : Run PostgreSQL in a container  
- **Git & GitHub**: Version control  

---

## Project Structure
```
Project-1/
│
├── src/
│   ├── fetch_weather.py
│   ├── transform_data.py
│   ├── load_to_postgres.py
│   ├── raw_weather_data.json
│   └── clean_weather_data.csv
│
├── docker-compose.yml
├── venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── .gitignore
├── README.md
└── requirements.txt
└── requirements.txt
```
## Setup Instructions

1. **Clone Repository**

git clone https://github.com/Nandana-Ajoy/Project-1.git

2. **Create Python Environment & Install Dependencies**

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

3. **Run the Pipeline**

python src/fetch_weather.py
python src/transform_data.py
python src/load_to_postgres.py

## Database Schema

erDiagram
    CITY_INFO {
        int city_id PK
        string city_name
        string country
    }

    WEATHER_DATA {
        int weather_id PK
        datetime time
        float temperature_c
        float humidity_percent
        float windspeed_ms
        int city_id FK
    }

## Sample CRUD Operations

-- Insert a city
INSERT INTO city_info (city_name, country) VALUES ('Trivandrum', 'India');

-- Insert weather data
INSERT INTO weather_data (time, temperature_c, humidity_percent, windspeed_ms, city_id)
VALUES ('2025-11-05 10:00:00', 29.5, 78, 3.5, 1);

-- Query weather data
SELECT * FROM weather_data;

-- Update temperature
UPDATE weather_data SET temperature_c = 32.0 WHERE weather_id = 1;

-- Delete a record
DELETE FROM weather_data WHERE weather_id = 3;

## References
Open-Meteo API
PostgreSQL Documentation
psycopg2 Documentation
