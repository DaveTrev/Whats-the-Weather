# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import configparser
import requests
import pyfiglet


config = configparser.ConfigParser()
config.read('config.ini')


# pyfgilet used to style app greeting
welcome = pyfiglet.figlet_format("Whats the weather?")
print(welcome)


user_input = input("Enter your city: ")
print(user_input)


open_weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + \
f"{user_input}&units=metric&APPID={config['API']['key']}")

print(open_weather_data.status_code)