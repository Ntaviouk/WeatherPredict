from meteostat import Daily, Point
from datetime import datetime

kyiv = Point(50.45, 30.52)
start = datetime(2024, 2, 1)
end = datetime(2024, 2, 7)

data = Daily(kyiv, start, end)
df = data.fetch()
df.to_csv("temp.csv")  # Зберігаємо у файл

print("Файл збережено як historical_weather.csv")
