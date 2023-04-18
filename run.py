# Import libraries
import os
import configparser
import sys
import requests
import pyfiglet
from colorama import Fore, Style


# Use configparser to read config.ini file
if 'API_KEY' in os.environ:
    config = {"API": {"key": None}}
    config["API"]["key"] = os.environ.get("API_KEY")
else:
    config = configparser.ConfigParser()
    config.read("config.ini")


# pyfgilet used to style app greeting
welcome = pyfiglet.figlet_format("Whats the weather?")
print(Fore.GREEN + welcome)

while True:
    print("1) Current Weather")
    print("2) Should I water the plants?")
    print("3) Quit")
    print(Style.RESET_ALL)

    choice = input("Enter Choice:\n ")
    # using strip method to removing leading trailing white space
    choice = choice.strip()

    # Prompt user to enter a city
    if choice == "1":
        user_input = input("Enter your city:\n ")
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
            print(Fore.RED + "No City Found")
        else: # gets current weather data
            current_weather = open_weather_data_c.json()["weather"][0]["main"]
            temp = round(open_weather_data_c.json()["main"]["temp"])
            feels_like = open_weather_data_c.json()["main"]["feels_like"]
            humid = open_weather_data_c.json()["main"]["humidity"]
            clouds = open_weather_data_c.json()["clouds"]["all"]
            wind = open_weather_data_c.json()["wind"]["speed"]

            print(Fore.BLUE + f"The weather in {user_input} is: {current_weather}")
            print(Fore.BLUE + f"The temperature in {user_input} is: {temp}°C")
            print(Fore.BLUE + f"It feels like in {user_input} is: {feels_like}°C")
            print(Fore.BLUE + f"The humidity in {user_input} is: {humid}%")
            print(Fore.BLUE + f"The cloud cover in {user_input} is: {clouds}")
            print(Fore.BLUE + f"The wind speed in {user_input} is: {wind}m/s2")
            if 'Rain' in current_weather: # checks if weather data contains rain
                print(Fore.YELLOW + "bring a jacket & a umbrella, looks like rain.")
            else:
                print(Fore.YELLOW + "Looks like no rain is due for today!")

            while True:
                print(Fore.GREEN + "Select what you would like to do next")
                print(Fore.GREEN + "1) Return to main menu.")
                print(Fore.GREEN + "2) Quit the program.")
                choice = input(Fore.GREEN + "Enter your choice: 1 or 2:\n ")
                # removes or truncates the given characters from the beginning and the end of the original string
                choice = choice.strip()  # change this menu option to return to main menu or quit program

                if choice == "1":
                    break
                elif choice == "2":
                    print(Fore.YELLOW + "Thanks for using DaveTrev's Whats the weather app")
                    sys.exit()  # give user option to quit or run again
                else:
                    print(Fore.RED + "Invalid option, please try again.")
                    print(Style.RESET_ALL)

    elif choice == "2":
        user_input = input("Enter your city, to check for predicted rainfall:\n ")
        print(user_input)

        # Request data from openweather.com
        open_weather_data_c = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + f"{user_input}&units=metric&APPID="
            + f"{config['API']['key']}",
            timeout=5,
        )
        if open_weather_data_c.json()["cod"] == "404":  # Error handling 4 data
            print(Fore.RED + "No City Found")
        else: # gets weather data for the next five days
            current_weather = open_weather_data_c.json()["weather"][0]["main"]
            if 'Rain' in current_weather: # checks if weather data contains rain
                print(Fore.YELLOW + "its a day for the ducks.....Rain!")
            else:
                print(Fore.YELLOW + "No rain is due for today, Hooray!")

            while True:
                print(Fore.GREEN + "Select what you would like to do next")
                print(Fore.GREEN + "1) Return to main menu.")
                print(Fore.GREEN + "2) Quit the program.")
                choice = input(Fore.GREEN + "Enter your choice: 1 or 2:\n ")
                # removes or truncates the given characters from the beginning and the end of the original string
                choice = choice.strip()        # change this menu option to return to main menu or quit program

                if choice == "1":
                    break
                elif choice == "2":
                    print("Thanks for using DaveTrev's Whats the weather app")
                    sys.exit()  # give user option to quit or run again
                else:
                    print(Fore.RED + "Invalid option, please try again.")
                    print(Style.RESET_ALL)

    elif choice == "3":
        print(Fore.YELLOW + "Thanks for using DaveTrev's Whats the weather app")
        break
    else:
        print(Fore.RED + "Invalid option. Please Try Again.")
        print(Style.RESET_ALL)
