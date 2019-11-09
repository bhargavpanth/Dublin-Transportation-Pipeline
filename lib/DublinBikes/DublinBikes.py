import requests
import urllib
import json

class DublinBikes(object):
	def __init__(self):
		self._url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&'
		self.val = "eae2a42f57ee0e99c46335e5960c1619eea2ded4"
		self.query_parameter = { 'apiKey' : self.val}
		self.url = self._url + urllib.parse.urlencode(self.query_parameter)

	def get_route_information(self):
		response = requests.get(self.url)
		return json.loads(response.text)
