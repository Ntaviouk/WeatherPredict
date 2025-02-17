from meteostat import Daily, Point
from datetime import datetime


def get_weather_data(param):
    kyiv = Point(50.45, 30.52)
    start = datetime(2020, 1, 1)
    end = datetime(2024, 12, 1)
    data = Daily(kyiv, start, end).fetch()

    if param in data.columns:  # Перевіряємо, чи є параметр у даних
        return data[param].fillna(0).tolist()  # Замінюємо NaN на 0 і конвертуємо в список
    else:
        raise ValueError(f"Параметр '{param}' не знайдено у даних!")



# # Встановлення координат міста (Київ)
# kyiv = Point(50.45, 30.52)
#
# # Встановлення періоду (від - до)
# start = datetime(2024, 1, 1)
# end = datetime(2024, 12, 1)
#
# # Отримання погодних даних
# data = Daily(kyiv, start, end).fetch()
#
# # Вивід потрібних параметрів
# # print(data[['tavg', 'tmin', 'tmax', 'pres', 'wspd']])
#
# print(data.columns)
#
# tavg_list = data['wspd'].tolist()
# print(tavg_list)
