### https://api.openweathermap.org/data/2.5/weather?b25115s914ecd4d3d0f9g666e042d25&q=mumbai

import requests, json
import os
from gtts import gTTS
import time

api_key = "Enter your API key."
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()


if x['cod'] != "404":
    y = x['main']
    temp = y['temp']
    pressure = y['pressure']
    humid = y['humidity']
    z = x['weather']
    desc = z[0]['description']
    print(desc)
    print("Temperature (K) = {0} | Atmospheric pressure (hPa) = {1} | Humidity (%) = {2}".format(temp,pressure,humid))
    data = "Place is" + str(city_name) + "Weather is" + str(desc) + "now" + "Temperature" + str(temp) + "Pressure" + str(pressure) + "Humidity" + str(humid)
    voice = gTTS(text=data, lang = 'en', slow = False)
    voice.save("output.mp3")
    os.system("start output.mp3")
    time.sleep(13)
    os.remove("output.mp3")
else:
    print("City not found")
