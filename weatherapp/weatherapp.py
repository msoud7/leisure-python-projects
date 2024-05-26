import tkinter as tk
from PIL import Image, ImageTk
import datetime as dt
import requests
import io

#defining the api key and the url
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "0a7c25b769d479e176bafb0690ce3a35"
city = "Alphen aan den Rijn"

data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

#get points of interest:
temperature = data.json()["main"]["temp"]
weather = data.json()["weather"][0]["main"]
mintemp = data.json()["main"]["temp_min"]
maxtemp = data.json()["main"]["temp_max"]
feelslike = data.json()["main"]["feels_like"]
humidity = data.json()["main"]["humidity"]
wind = data.json()["wind"]["speed"]
sunrise = data.json()["sys"]["sunrise"]
sunset = data.json()["sys"]["sunset"]

icon = data.json()["weather"][0]["icon"]

icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

# Convert sunrise and sunset from Unix timestamp to readable time
sunrise_time = dt.datetime.fromtimestamp(sunrise).strftime('%H:%M')
sunset_time = dt.datetime.fromtimestamp(sunset).strftime('%H:%M')


#generate GUI
base = tk.Tk()
base.title("Weather App")

#set size
base.geometry("400x550")

# Main info
title_label = tk.Label(base,
                       text="Weather App",
                       font=("YouTube Sans", 40, 'bold'),
                       fg="black",
                       bd=10)
title_label.pack(pady=10)

city_label = tk.Label(base, 
                      text=city,
                      font=("Arial", 20, "bold"))
city_label.pack(pady=5)

temperature_label = tk.Label(base,
                             text=f"{round(temperature, 1)} °C",
                             font=("YouTube Sans", 40))
temperature_label.pack(pady=5)

weather_label = tk.Label(base,
                         text=f"Weather: {weather}",
                         font=("Arial", 20, "bold"))
weather_label.pack(pady=5)

# Include weather Icon
response = requests.get(icon_url)
img_data = response.content
image = Image.open(io.BytesIO(img_data))
photo = ImageTk.PhotoImage(image)
icon_label = tk.Label(base, image=photo)
icon_label.image = photo  # Keep a reference
icon_label.pack(pady=5)

# Create a frame to hold the small info labels
info_frame = tk.Frame(base)
info_frame.pack(pady=10)

# Small info labels
mintemp_label = tk.Label(info_frame,
                         text=f"Min Temp: {round(mintemp, 1)} °C",
                         font=("Arial", 10))
mintemp_label.grid(row=0, column=0, padx=5, pady=5)

maxtemp_label = tk.Label(info_frame,
                         text=f"Max Temp: {round(maxtemp, 1)} °C",
                         font=("Arial", 10))
maxtemp_label.grid(row=0, column=1, padx=5, pady=5)

feelslike_label = tk.Label(info_frame,
                           text=f"Feels Like: {round(feelslike, 1)} °C",
                           font=("Arial", 10))
feelslike_label.grid(row=1, column=0, padx=5, pady=5)

wind_label = tk.Label(info_frame,
                      text=f"Wind Speed: {wind} m/s",
                      font=("Arial", 10))
wind_label.grid(row=1, column=1, padx=5, pady=5)

sunrise_label = tk.Label(info_frame,
                         text=f"Sunrise: {sunrise_time}",
                         font=("Arial", 10))
sunrise_label.grid(row=2, column=0, padx=5, pady=5)

sunset_label = tk.Label(info_frame,
                        text=f"Sunset: {sunset_time}",
                        font=("Arial", 10))
sunset_label.grid(row=2, column=1, padx=5, pady=5)

base.mainloop()