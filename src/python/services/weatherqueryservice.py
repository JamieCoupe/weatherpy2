import json
import requests
import datetime
from weatherpy2.src.python.model import weatherreport

class WeatherReport(object):

    def __init__(self, weatherdata):
        self.__dict__ = json.loads(weatherdata)


class WeatherQueryService:

    def __init__(self):

        # Read the open weather api info from the secrets json
        with open('../../data/config/weather_secret.json') as json_file:
            config = json.load(json_file)

            api_key = config['apikey']
            location = config['location']
            search_url = config['searchurl']

        # Compile the complete url including api key and location
        self.complete_url = search_url.format(location, api_key)

    def get_current_weather(self):

        # Get the weather from open weather map
        response = requests.get(self.complete_url)

        if response.status_code == 200:
            openweatherreport = json.loads(response.text)

            print(openweatherreport.get("weather", "This attribute doesnt exist"))
            # Parse the results and create new object

            timestamp = datetime.datetime.fromtimestamp(int(openweatherreport['dt'])).strftime('%H:%M - %A, %d of %B ')

            # Weather
            weathermain = openweatherreport["weather"][0]["main"]
            weatherdesc = openweatherreport["weather"][0]["description"]

            # Temperature
            currenttemp = openweatherreport["main"]["temp"]
            maxtemp = openweatherreport["main"]["temp_max"]
            mintemp = openweatherreport["main"]["temp_min"]

            # Wind
            windspeed = openweatherreport["wind"]["speed"]
            winddirection = openweatherreport["wind"]["deg"]

            # Time
            sunrise = datetime.datetime.fromtimestamp(int(openweatherreport["sys"]["sunrise"])).strftime(
                '%H:%M')
            sunset = datetime.datetime.fromtimestamp(int(openweatherreport["sys"]["sunset"])).strftime(
                '%H:%M')

            # Other
            pressure = openweatherreport["main"]["pressure"]
            humidity = openweatherreport["main"]["humidity"]

            # Location
            location = openweatherreport["name"]
            currentweather = weatherreport.WeatherReport(timestamp,
                                                         weathermain, weatherdesc,
                                                         currenttemp, maxtemp, mintemp,
                                                         windspeed, winddirection,
                                                         sunrise, sunset,
                                                         pressure, humidity,
                                                         location)
            return currentweather

        else:
            print("There was an error polling the data")
