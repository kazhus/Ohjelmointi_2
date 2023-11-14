


"""import requests

api_key = "YOUR_API_KEY_HERE"
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"] - 273.15
description = data["weather"][0]["description"]

print(f"The temperature in {city} is {temperature:.1f}°C and the weather is {description}.")
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()

print(data["value"])
"""
"""


import requests

print(requests.get("https://www.metropolia.fi"))

# query = "emmer"
query = input("Anna hakusana >")
req = f"https://api.tvmaze.com/search/shows?q={query}"

def print_show_data(show_data):
    for show in show_data:
        # show film score greater than 0,5 points
        if show["score"] > 0.5:
            print(show["show"]["name"])
            print(show["score"])
            # printing genres in show
            for genre in show["show"]["genres"]:
                print(f" - {genre}")
#try always finish with execpt
try:
    response_content = requests.get(req).json()
    #print(response_content)
    print_show_data(response_content)
#what type of error will print out
except requests.exceptions.RequestException as error:
    print("Network connection failed")
    print(error)
    #print(error)
"""