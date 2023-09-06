import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

def get_weather(city):
    API_Key = "05aeb6730d14a9008e66a69bb5e58014"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(city, API_Key)
    res = requests.get(url)
    print(res)
    if res.status_code == 404:
        messagebox.showerror("ERROR", "City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    humidity = weather['main']['humidity']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = "https://openweathermap.org/img/wn/{}@2x.png".format(icon_id)
    return (icon_url, temperature, humidity, description, city, country)

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url, temperature, humidity, description, city, country = result
    location_label.configure(text="{},{}".format(city, country))
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text="Termerature: {:.2f}°C".format(temperature))
    humidity_label.configure(text="Humidity: {}%".format(humidity))
    description_label.configure(text="Description: {}".format(description))


root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.insert("Enter City Name")
city_entry.pack(pady=10)

search_button = ttkbootstrap.Button(root,text="Search", command=search, bootstyle="warning" )
search_button.pack(pady=10)

location_label = tk.Label(root, font="Helvetica, 18")
location_label.pack(pady=20)

icon_label=tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

humidity_label = tk.Label(root, font="Helvetica, 20")
humidity_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()


