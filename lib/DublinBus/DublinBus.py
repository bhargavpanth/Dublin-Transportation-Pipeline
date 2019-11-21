'''
Building the Dublin Bus into a pyton module
'''

import requests
import urllib
import http.client
import base64
import json
import sys
import os

class DublinBus:
	# Dublin transportation API will be deprecated end of next year
	# must move to the new one - https://api.nationaltransport.ie/gtfsrtest/?format=json
	def __init__(self, stop_id):
		self.header = { 'Cache-Control': 'no-cache', 'x-api-key': '82fd716f61ed4a2082e59ab03ceb4ca8' }
		self._url = 'https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?'
		self.stop_id = stop_id
		self.query_parameter = { 'stopid' : stop_id }
		self.url = self._url + urllib.parse.urlencode(self.query_parameter)

	def select_response(self,response):
		values = dict()
		res = response.json()
		values[str(self.stop_id)] = res["results"]
		return json.dumps(values)

	def get_route_information(self):
		response = requests.get(self.url)
		n = str(self.select_response(response))
		return json.loads(n)



'''
## optional static method to prettify json
	@staticmethod
	def prettify_json(obj):
		json_ = json.loads(obj)
		return json.dumps(json_, indent=4, sort_keys=True)
'''