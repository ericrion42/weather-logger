# --- Imports ---
# requests: fetches data from the web
# csv: reads and writes CSV files
# os: interacts with the file system
# datetime: gets the current date and time
import requests
import csv
import os
from datetime import datetime

# --- Location Settings ---
# Latitude and longitude for Hartsfield-Jackson Atlanta International Airport
# Change as needed
LATITUDE = 33.6407
LONGITUDE = -84.4277
LOCATION_NAME = "Atlanta, GA (Hartsfield-Jackson)"

# --- File Settings ---
# Name of the CSV file where weather data will be stored
LOG_FILE = "weather_log.csv"

# --- Fetch Weather Data ---
# Calls the Open-Meteo API and returns current weather data
def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current_weather": "true",
        "hourly": "relativehumidity_2m,precipitation"
    }

    # Make Web Request
    response = requests.get(url, params=params)

    # Convert the response to Python dictionary
    data = response.json()

    # Extract desired weather data
    current = data["current_weather"]
    temperature_c = current["temperature"]
    temperature_f = temperature_c * 9/5 + 32 # Convert celsius to fahrenheit
    windspeed = current["windspeed"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Temporary Output For QA
    print(f"Timestamp: {timestamp}")
    print(f"Location: {LOCATION_NAME}")
    print(f"Temperature: {temperature_f:.1f}°F")
    print(f"Wind Speed: {windspeed} km/h")

    return {
        "timestamp": timestamp,
        "location": LOCATION_NAME,
        "temperature_f": round(temperature_f, 1),
        "windspeed_kmh": windspeed
      }

# --- TEMPORARY: call the function so we can test it ---
fetch_weather()