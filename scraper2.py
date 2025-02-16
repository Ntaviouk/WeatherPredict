import requests
import time

API_KEY = "34ee2c0ecbe228d7c8e6e25e7354b09a"
lat, lon = 50.45, 30.52  # Координати Києва
timestamp = int(time.mktime(time.strptime("2024-02-01", "%Y-%m-%d")))  # Дата у форматі Unix

url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if "data" in data:
    for entry in data["data"]:
        print(f"Час: {entry['dt']}, Температура: {entry['temp']}°C, Тиск: {entry['pressure']} hPa, Вологість: {entry['humidity']}%, Вітер: {entry['wind_speed']} м/с")
else:
    print("Помилка отримання даних:", data)
