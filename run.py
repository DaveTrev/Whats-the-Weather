# Import libraries
import os
import configparser
import sys
import time
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


def clear_console():
    """
    Clears the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def intro():
    """
    Weather app greeting message and menu options
    """
    # pyfgilet used to style app greeting
    welcome = pyfiglet.figlet_format("Whats the weather?")
    print(Fore.GREEN + welcome)


intro()


def main():
    """
    Main function of program
    """


while True:
    print("1) Current Weather")
    print("2) Cut to the chase..... is it going to rain?")
    print("3) Quit")
    print(Style.RESET_ALL)

    choice = input("Enter Choice:\n ")
    # using strip method to removing leading trailing white space
    choice = choice.strip()

    # Prompt user to enter a city
    if choice == "1":
        user_input = input("Enter your city:\n ")
        time.sleep(2)
        clear_console()
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
        else:   # gets current weather data
            current_weather = open_weather_data_c.json()["weather"][0]["main"]
            temp = round(open_weather_data_c.json()["main"]["temp"])
            feels_like = open_weather_data_c.json()["main"]["feels_like"]
            humid = open_weather_data_c.json()["main"]["humidity"]
            clouds = open_weather_data_c.json()["clouds"]["all"]
            wind = open_weather_data_c.json()["wind"]["speed"]
            # Print weather requests of user reqeusted city
            print(Fore.BLUE + f"The weather in {user_input} is: "
                              f"{current_weather}")
            print(Fore.BLUE + f"The temperature in {user_input} is: {temp}°C")
            print(Fore.BLUE + f"It feels like in {user_input} is: "
                              f"{feels_like}°C")
            print(Fore.BLUE + f"The humidity in {user_input} is: {humid}%")
            print(Fore.BLUE + f"The cloud cover in {user_input} is: {clouds}")
            print(Fore.BLUE + f"The wind speed in {user_input} is: {wind}m/s2")
            print()
            # checks if weather data contains rain
            if 'Rain' in current_weather:
                print(Fore.YELLOW + "bring a jacket & a umbrella,"
                                    "looks like rain.")
                print()
            else:
                print(Fore.YELLOW + "Looks like no rain is due for today!")
                print()
    # Gives user option to return to menu and search another city or quit.
            while True:
                print(Fore.GREEN + "Select what you would like to do next")
                print(Fore.GREEN + "1) Return to main menu.")
                print(Fore.GREEN + "2) Quit the program.")
                choice = input(Fore.GREEN + "Enter your choice: 1 or 2:\n ")
                """
                Removes or truncates the given characters from
                    the beginning
                    and the end of the original string
                """
                choice = choice.strip()

                if choice == "1":
                    break
                elif choice == "2":
                    time.sleep(2)
                    clear_console()
                    print(Fore.YELLOW + "Thanks for using DaveTrev's "
                                        "Whats the weather app")
                    sys.exit()  # give user option to quit or run again
                else:
                    print(Fore.RED + "Invalid option, please try again.")
                    print(Style.RESET_ALL)
    # alternate option to check rainfall for user input city
    elif choice == "2":
        user_input = input("Enter your city,"
                           "to check for predicted rainfall:\n ")
        time.sleep(2)
        clear_console()
        # Request data from openweather.com
        open_weather_data_c = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + f"{user_input}&units=metric&APPID="
            + f"{config['API']['key']}",
            timeout=5,
        )
        if open_weather_data_c.json()["cod"] == "404":  # Error handling 4 data
            print(Fore.RED + "No City Found")
        else:  # gets weather data for the next five days
            current_weather = open_weather_data_c.json()["weather"][0]["main"]
            # checks if weather data contains rain
            if 'Rain' in current_weather:
                print(Fore.YELLOW + "its a day for the ducks.....Rain!")
                print()
            else:
                print(Fore.YELLOW + "No rain is due for today, Hooray!")
                print()
            while True:
                print(Fore.GREEN + "Select what you would like to do next")
                print(Fore.GREEN + "1) Return to main menu.")
                print(Fore.GREEN + "2) Quit the program.")
                choice = input(Fore.GREEN + "Enter your choice: 1 or 2:\n ")
                """
                Removes or truncates the given characters from
                    the beginning
                    and the end of the original string
                """
                choice = choice.strip()
                # menu option, main menu or quit program
                if choice == "1":
                    break
                elif choice == "2":
                    time.sleep(2)
                    clear_console()
                    print("Thanks for using DaveTrev's Whats the weather app")
                    sys.exit()  # give user option to quit or run again
                else:
                    print(Fore.RED + "Invalid option, please try again.")
                    print(Style.RESET_ALL)

    elif choice == "3":
        print(Fore.YELLOW + "Thanks for using DaveTrev's "
                            "Whats the weather app")
        break
    else:
        print(Fore.RED + "Invalid option. Please Try Again.")
        print(Style.RESET_ALL)

main()
