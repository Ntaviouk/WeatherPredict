from meteostat import Daily, Point
from datetime import datetime

# Встановлення координат міста (Київ)
kyiv = Point(50.45, 30.52)

# Встановлення періоду (від - до)
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 1)

# Отримання погодних даних
data = Daily(kyiv, start, end).fetch()

# Вивід потрібних параметрів
#print(data[['tavg', 'tmin', 'tmax', 'pres', 'wspd']])

tavg_list = data['prcp'].tolist()
print(tavg_list)
