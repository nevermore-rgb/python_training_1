import requests

class CountryService:
    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1/name"

    def get_country_info(self, country):
        response = requests.get(f"{self.base_url}/{country}")
        return response.json()
