# InfoFinder

InfoFinder is an application that provides comprehensive information about a location, including weather, country details, and a brief historical summary from Wikipedia.

## Features

- Fetches current weather information for a city or country using the [OpenWeatherMap API](https://openweathermap.org/api).
- Retrieves country information using the [RestCountries API](https://restcountries.com/).
- Provides a brief historical summary of the location using the [Wikipedia API](https://wikipedia-api.readthedocs.io/en/latest/).

## Requirements

- Python 3.6+
- `requests` library
- `wikipedia-api` library

## Example
```Python
Enter a country or a city: London

Weather Information:
Location: London, GB
Temperature: 15°C
Weather: light rain

Country Information:
Name: United Kingdom
Capital: London
Region: Europe
Population: 67215293
Area: 243610 km²

Wikipedia Summary:
London is the capital and largest city of England and the United Kingdom. The city stands on the River Thames in the south-east of England, at the head of a 50-mile (80 km) estuary down to the North Sea, and has been a major settlement for two millennia...
```

