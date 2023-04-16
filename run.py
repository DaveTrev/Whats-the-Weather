# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Todo list
colour program title  **
add menu options **
add clouds and rain
give option to repeat program or quit


readme
heroku deploy
"""
# Import libraries
import configparser
import requests
import pyfiglet
from colorama import Fore

# Use configparser to read config.ini file
config = configparser.ConfigParser()
config.read("config.ini")

# pyfgilet used to style app greeting
welcome = pyfiglet.figlet_format("Whats the weather?")
print(Fore.GREEN + welcome)

while True:
    print("1) Current Weather")
    print("2) Forcast")
    print("3) Quit")

    choice = input("Enter Choice: ")
    # using strip method to removing leading trailing white space
    choice = choice.strip()

    # Prompt user to enter a city
    if choice == "1":
        user_input = input("Enter your city: ")
        print(user_input)

        # Request data from openweather.com
        open_weather_data_c = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + f"{user_input}&units=metric&APPID="
            + f"{config['API']['key']}",
            timeout=5,
        )

        # Error handling for data request, no city found / print data
        if open_weather_data_c.json()["cod"] == "404":
            print("No City Found")
        else:
            current_weather = open_weather_data_c.json()["weather"][0]["main"]
            temp = round(open_weather_data_c.json()["main"]["temp"])
            humid = open_weather_data_c.json()["main"]["humidity"]
            clouds = open_weather_data_c.json()["clouds"]["all"]

            print(Fore.BLUE + f"The weather in {user_input} is: {current_weather}")
            print(Fore.BLUE + f"The temperature in {user_input} is: {temp}°C")
            print(Fore.BLUE + f"The humidity in {user_input} is: {humid}%")
            print(Fore.BLUE + f"The cloud cover in {user_input} is: {clouds}")

    elif choice == "2":
        user_input = input("Enter your city: ")
        print(user_input)

        # Request data from openweather.com
        open_weather_data_f = requests.get(
            " https://api.openweathermap.org/data/2.5/forecast?q="
            + f"{user_input}&units=metric&APPID="
            + f"{config['API']['key']}", timeout=5,
        )
        print(open_weather_data_f.content)




        """
        # Error handling for data request, no city found / print data
        if open_weather_data.json()["cod"] == "404":
            print("No City Found")
        else:
            current_weather = open_weather_data.json()["weather"][0]["main"]
            temp = round(open_weather_data.json()["main"]["temp"])

            print(Fore.BLUE + f"The weather in {user_input} is: {current_weather}")
            print(Fore.BLUE + f"The temperature in {user_input} is: {temp}°C")
        """
    elif choice == "3":
        break
    else:
        print("Invalid option. Please Try Again.")
