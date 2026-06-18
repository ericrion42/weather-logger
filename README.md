# --- Update README ---

# Rewrites the README.md file with the latest weather data

def update_readme(data):
readme_content = f"""# 🌤️ Atlanta Weather Logger

An automated weather logging project that records daily weather data for Atlanta, GA (Hartsfield-Jackson Airport) using the Open-Meteo API and GitHub Actions.

## 📊 Latest Weather Entry

| Field          | Value                        |
| -------------- | ---------------------------- |
| 📅 Timestamp   | {data['timestamp']}          |
| 📍 Location    | {data['location']}           |
| 🌡️ Temperature | {data['temperature_f']}°F    |
| 💨 Wind Speed  | {data['windspeed_kmh']} km/h |

## 📁 About This Project

- Weather data is automatically fetched and logged once daily at 8:00am EST
- All data is stored in `weather_log.csv` and can be freely accessed for other projects
- Built with Python and GitHub Actions as a learning project

## 🔗 Using the Data

The raw CSV data is publicly accessible at:
https://raw.githubusercontent.com/ericrion42/weather-logger/main/weather_log.csv

_Built by Eric Rion with (heavy) assistance from [Claude.ai](https://claude.ai) as part of a learning experience._
"""
with open("README.md", "w") as f:
f.write(readme_content)

    print(Fore.GREEN + "README.md successfully updated!")
