import requests

api_key = "<KEY>"
city = api_key (input("Enter your city name: ")).json()
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + f"&appid={api_key}"
response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"] -100
description = data["weather"][0]["description"]
print(f" The temperature of {city} is {temperature} Celisus and"
      f"the weather is {description}.")