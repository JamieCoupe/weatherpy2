class WeatherReport(object):

    def __init__(self, timestamp, weathermain, weatherdescription,
                 currenttemp, maxtemp, mintemp,
                 windspeed, winddirection,
                 sunrise, sunset,
                 pressure, humidity,
                 location):

        self.timestamp = timestamp
        self.weather = {"weather": weathermain, "description": weatherdescription }
        self.temperature = {"current": currenttemp, "max": maxtemp, "min": mintemp}
        self.wind = {"speed": windspeed, "direction": winddirection}
        self.time = {"sunrise": sunrise, "sunset": sunset}
        self.other = {"pressure": pressure, "humidity": humidity}
        self.location = location
