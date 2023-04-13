# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Import libraries
import configparser
import requests
import pyfiglet


# Use configparser to read config.ini file
config = configparser.ConfigParser()
config.read('config.ini')


# pyfgilet used to style app greeting
welcome = pyfiglet.figlet_format("Whats the weather?")
print(welcome)

# Prompt user to enter a city
user_input = input("Enter your city: ")
print(user_input)

# Request data from openweather.com 
open_weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + \
f"{user_input}&units=metric&APPID={config['API']['key']}")


current_weather = open_weather_data.json()['weather'][0]['main']
temp = open_weather_data.json()['main']['temp']

print(current_weather, temp)
