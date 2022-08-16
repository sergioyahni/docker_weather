import pandas as pd

import requests as requests


class GetWeather:
    def __init__(self):
        url = 'https://api.open-meteo.com/v1/forecast'
        params = {
            "latitude": "31.7857",
            "longitude": "35.2007",
            "hourly": ["temperature_2m", "cloudcover"],
            "daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
            "timezone": "Asia/Jerusalem"
        }
        weather = requests.get(url, params=params).json()

        self.data = {
            'time': weather['daily']['time'],
            'temperature_min': weather['daily']['temperature_2m_min'],
            'temperature_max': weather['daily']['temperature_2m_max'],
            'sunrise': weather['daily']['sunrise'],
            'sunset': weather['daily']['sunset']
        }

    def weather(self):
        return pd.DataFrame.from_dict(self.data)

if __name__ == '__main__':
    w = GetWeather()
    print(w.weather().columns)