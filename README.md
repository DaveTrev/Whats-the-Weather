![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome DaveTrev,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!


Resources Used for project ----
api from openweather.com
hiding api keys https://blog.netwrix.com/2022/11/14/how-to-hide-api-keys-github/#:~:text=So%20how%20can%20we%20hide,control%20(e.g.%2C%20gitignore).
configparser - reading config file, hiding api key
configparser - https://www.tutorialandexample.com/how-to-write-a-configuration-file-in-python
https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
youtube - https://www.youtube.com/watch?v=baWzHKfrvqw
setting timeout for requests - https://reqbin.com/code/python/3zdpeao1/python-requests-timeout-example
python checker - https://www.pythonchecker.com/
python import statements - https://careerkarma.com/blog/python-import/#:~:text=import%20Python%3A%20Using%20the%20from,can%20use%20the%20from%20statement.
https://www.geeksforgeeks.org/print-colors-python-terminal/
https://www.geeksforgeeks.org/print-colors-python-terminal/
https://stackoverflow.com/questions/42475681/using-openweather-json-api-how-to-fetch-the-temperature

----need to add requests.get
https://datagy.io/python-requests-timeouts/

Data returned from open weather for request "berlin"
{'coord': {'lon': 13.4105, 'lat': 52.5244}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 6.29, 'feels_like': 3.99, 'temp_min': 4.49, 'temp_max': 8.3, 'pressure': 990, 'humidity': 90}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 210}, 'clouds': {'all': 0}, 'dt': 1681362490, 'sys': {'type': 2, 'id': 2011538, 'country': 'DE', 'sunrise': 1681359231, 'sunset': 1681408782}, 'timezone': 7200, 'id': 2950159, 'name': 'Berlin', 'cod': 200}
