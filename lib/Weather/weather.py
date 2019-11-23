# As a dependent variable for the traffic and routing analysis

class Weather():
    def __init__(self):
        self.key = 'cfdc6b207dmsh3eec0297138fb77p17598ajsnf15d8387fa96'
        self.host = 'community-open-weather-map.p.rapidapi.com'
        self.url = 'https://community-open-weather-map.p.rapidapi.com/weather'
        self.headers = { 'x-rapidapi-key': str(self.key), 'x-rapidapi-host': str(self.host) }
        pass
