import requests

API_KEY = "34ee2c0ecbe228d7c8e6e25e7354b09a"
city = "Kyiv"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print("Температура:", data["main"]["temp"])
print("Тиск:", data["main"]["pressure"])
print("Вологість:", data["main"]["humidity"])
print("Швидкість вітру:", data["wind"]["speed"])
