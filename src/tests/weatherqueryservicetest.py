import unittest
from weatherpy2.src.python.services import weatherqueryservice


class WeatherServiceTest(unittest.TestCase):

    def test_weatherservicedoesnotreturnnone(self):
        weatherservice = weatherqueryservice.WeatherQueryService()
        self.assertIsNotNone(weatherservice.get_current_weather())


if __name__ == '__main__':
    unittest.main()