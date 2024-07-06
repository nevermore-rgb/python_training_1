from weather_service import WeatherService
from country_service import CountryService
from wikipedia_service import WikipediaService

class LocationInfo:
    def __init__(self, weather_api_key):
        self.weather_service = WeatherService(weather_api_key)
        self.country_service = CountryService()
        self.wikipedia_service = WikipediaService()

    def get_location_info(self, location):
        weather = self.weather_service.get_weather(location)
        country_info = self.country_service.get_country_info(location)
        wikipedia_summary = self.wikipedia_service.get_summary(location)
        
        return {
            "weather": weather,
            "country_info": country_info,
            "wikipedia_summary": wikipedia_summary
        }
