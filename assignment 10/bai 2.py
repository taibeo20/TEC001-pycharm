import requests

API_KEY = "0c8c9df9c48a4815e7b86b56c487df5a"

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    description = data["weather"][0]["description"]

    print(f"Weather: {description}")
    print(f"Temperature: {temp_celsius:.2f}°C")
else:
    print("City not found or error")