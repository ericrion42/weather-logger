# --- Imports ---
# requests: fetches data from the web
# csv: reads and writes CSV files
# os: interacts with the file system
# datetime: gets the current date and time
# colorama: adds color to terminal output (cross-platform)
import requests
import csv
import os
from datetime import datetime
from colorama import init, Fore, Style

# I want orange text for outputs
ORANGE = "\033[38;2;255;165;0m"

# Initialize colorama (required for Windows color support)
init(autoreset=True)

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

    if response.status_code != 200:
        raise Exception(Fore.RED + f"API request failed with status code {response.status_code}")

    # Convert the response to Python dictionary
    data = response.json()

    # Extract desired weather data
    current = data["current_weather"]
    temperature_c = current["temperature"]
    temperature_f = temperature_c * 9/5 + 32 # Convert celsius to fahrenheit
    windspeed = current["windspeed"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "timestamp": timestamp,
        "location": LOCATION_NAME,
        "temperature_f": round(temperature_f, 1),
        "windspeed_kmh": windspeed
      }

# Write weather data to CSV
# Appends a new row to the log file each time it runs
def log_weather(data):
    file_exists = os.path.isfile(LOG_FILE)

    # Open the file in append mode
    with open(LOG_FILE, "a", newline="") as csvfile:
        fieldnames = ["timestamp", "location", "temperature_f", "windspeed_kmh"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file didn't exist before, write the header
        if not file_exists:
            writer.writeheader()

        # Write the weather data as a new row
        writer.writerow(data)
    
    print (Fore.GREEN + f"Data logged to {LOG_FILE}")

# --- Main Entry Point ---
def main():
    print(ORANGE + f"Fetching weather data for {LOCATION_NAME}...")
    weather_data = fetch_weather()
    log_weather(weather_data)
    print(Fore.GREEN + "Weather data successfully logged. Goodbye!")

# This line ensures main() only runs when we execute this file directly.
if __name__ == "__main__":
    main()