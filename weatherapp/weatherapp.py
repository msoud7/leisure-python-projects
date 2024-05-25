import tkinter as tk
import datetime as dt
import requests

#defining the api key and the url
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "0a7c25b769d479e176bafb0690ce3a35"
city = "Alphen aan den Rijn"

data = requests.get(
	f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

print(data.json())

#get points of interest:
temperature = data.json()["main"]["temp"]
weather = data.json()["weather"][0]["main"]
mintemp = data.json()["main"]["temp_min"]
maxtemp = data.json()["main"]["temp_max"]
feelslike = data.json()["main"]["feels_like"]
humidity = data.json()["main"]["humidity"]
wind = data.json()["wind"]["speed"]
sunrise = data.json()["sys"]["sunrise"]
sunset =data.json()["sys"]["sunset"]


#generate GUI
base = tk.Tk()
base.title("Weather App")

#set size
base.geometry("400x400")


# Main info
title_label = tk.Label(base,
                       text="Weather App",
                       font=("Arial", 40, 'bold'),
                       fg="black",
                       bg="white",
                       bd=10,
                       compound="bottom")
title_label.pack(pady=10)

city_label = tk.Label(base, 
	text = city,
	font = ("Arial", 20))
city_label.pack(pady=5)


temperature_label = tk.Label(base,
                             text=f"{round(temperature, 1)} °C",
                             font=("Arial", 40))
temperature_label.pack(pady=5)

weather_label = tk.Label(base,
                         text=f"Weather: {weather}",
                         font=("Arial", 20))
weather_label.pack(pady=5)


#Small info 
# Small info
mintemp_label = tk.Label(base,
                         text=f"Min Temp: {mintemp} °C",
                         font=("Arial", 10))
mintemp_label.pack(pady=5)

maxtemp_label = tk.Label(base,
                         text=f"Max Temp: {maxtemp} °C",
                         font=("Arial", 10))
maxtemp_label.pack(pady=5)

feelslike_label = tk.Label(base,
                           text=f"Feels Like: {feelslike} °C",
                           font=("Arial", 10))
feelslike_label.pack(pady=5)

humidity_label = tk.Label(base,
                          text=f"Humidity: {humidity} %",
                          font=("Arial", 10))
humidity_label.pack(pady=5)

wind_label = tk.Label(base,
                      text=f"Wind Speed: {wind} m/s",
                      font=("Arial", 10))
wind_label.pack(pady=5)

sunrise_label = tk.Label(base,
                         text=f"Sunrise: {sunrise}",
                         font=("Arial", 10))
sunrise_label.pack(pady=5)

sunset_label = tk.Label(base,
                        text=f"Sunset: {sunset}",
                        font=("Arial", 10))
sunset_label.pack(pady=5)


base.mainloop()