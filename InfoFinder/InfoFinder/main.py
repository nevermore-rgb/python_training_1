from location_info import LocationInfo

def main():
    weather_api_key = "YOUR_API_KEY"

    location_info = LocationInfo(weather_api_key)

    location = input("Enter a Country name: ")
    info = location_info.get_location_info(location)

    print("\nWeather Information:")
    if 'weather' in info['weather']:
        weather = info['weather']
        print(f"Location: {weather['name']}, {weather['sys']['country']}")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Weather: {weather['weather'][0]['description']}")
    else:
        print(f"Could not fetch weather data: {info['weather']}")

    print("\nCountry Information:")
    if isinstance(info['country_info'], list) and len(info['country_info']) > 0:
        country = info['country_info'][0]
        print(f"Name: {country['name']['common']}")
        print(f"Capital: {country['capital'][0]}")
        print(f"Region: {country['region']}")
        print(f"Population: {country['population']}")
        print(f"Area: {country['area']} km²")
    else:
        print(f"Could not fetch country data: {info['country_info']}")

    print("\nWikipedia Summary:")
    print(info['wikipedia_summary'])

if __name__ == "__main__":
    main()
