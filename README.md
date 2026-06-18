# 🌤️ Atlanta Weather Logger

An automated weather data logging project that fetches and records daily weather conditions for Atlanta, GA (Hartsfield-Jackson International Airport) using the Open-Meteo API and GitHub Actions.

## 📋 Project Overview

This program runs automatically once per day at 8:00am EST via GitHub Actions. It fetches current weather data from the free Open-Meteo API and appends a new row to a growing CSV log file, which is then committed and pushed back to this repository automatically.

## 🚀 How It Works

1. GitHub Actions triggers the workflow every day at 8:00am EST
2. A fresh Ubuntu virtual machine is spun up on GitHub's servers
3. Python and required libraries are installed
4. `weather_logger.py` fetches current weather data from Open-Meteo API
5. A new row is appended to `weather_log.csv`
6. The updated CSV is committed and pushed back to this repo automatically

## 📊 Data Logged

Each entry in `weather_log.csv` contains the following fields:

| Field           | Description                                        |
| --------------- | -------------------------------------------------- |
| `timestamp`     | Date and time of the reading (YYYY-MM-DD HH:MM:SS) |
| `location`      | Location name                                      |
| `temperature_f` | Temperature in Fahrenheit                          |
| `windspeed_kmh` | Wind speed in km/h                                 |

## 🔗 Accessing the Data

The CSV data is publicly accessible and can be used in other projects via its raw URL:
https://raw.githubusercontent.com/ericrion42/weather-logger/main/weather_log.csv

### Example: Load in Python

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/ericrion42/weather-logger/main/weather_log.csv")
print(df)
```

## 🛠️ Tech Stack

- **Python 3.11**
- **Open-Meteo API** — free, no API key required
- **GitHub Actions** — automated scheduling and commits
- **Libraries:** `requests`, `colorama`

## 📁 Project Structure

weather-logger/

├── .github/
└── workflows/
└── weather_update.yml # GitHub Actions workflow
├── .gitignore # Python gitignore
├── README.md # This file
├── weather_log.csv # Auto-generated weather data log
└── weather_logger.py # Main Python script

## 🔧 Running Locally

1. Clone the repository
2. Install dependencies:

```bash
pip install requests colorama
```

3. Run the script:

```bash
python weather_logger.py
```

## 📝 Notes

- GitHub Actions runs on UTC time. 8:00am EST = 12:00pm UTC
- During EDT (March–November) the log runs at 8:00am Eastern
- During EST (November–March) the log runs at 7:00am Eastern

## 👤 Credit

Built by **Eric** with assistance from [Claude.ai](https://claude.ai) as part of a Python and GitHub Actions learning experience.
