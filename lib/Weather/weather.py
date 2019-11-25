# As a dependent variable for the traffic and routing analysis
import requests

class Weather():
    def __init__(self, location):
        # Use better key management - key is practically free
        self.key = 'cfdc6b207dmsh3eec0297138fb77p17598ajsnf15d8387fa96'
        self.host = 'community-open-weather-map.p.rapidapi.com'
        self.url = 'https://community-open-weather-map.p.rapidapi.com/weather'
        self.headers = { 'x-rapidapi-key': str(self.key), 'x-rapidapi-host': str(self.host) }
        self.querystring = { 'q': str(location), 'mode':'json', 'units': 'imperial' }

    def get_weather_data(self):
        return requests.request('GET', self.url, headers=self.headers, params=self.querystring)


