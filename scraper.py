#scraper.py
from meteostat import Daily, Point
from datetime import datetime


def get_weather_data(param):
    kyiv = Point(50.45, 30.52)
    start = datetime(2022, 5, 1)
    end = datetime(2024, 12, 1)
    data = Daily(kyiv, start, end).fetch()
    # print(data[['prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun','tavg']])
    if param in data.columns:
        return data[param].tolist()
    else:
        raise ValueError(f"Параметр '{param}' не знайдено у даних!")


# get_weather_data("snow")


