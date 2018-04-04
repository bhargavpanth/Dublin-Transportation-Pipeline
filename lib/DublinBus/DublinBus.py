'''
Building the Dublin Bus into a pyton module
'''

import requests
import urllib
import json
import sys
import os
import numpy as np

class DublinBus:
	#values = dict()
	""" DublinBus Module """
	# _url = "https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?"
	_url = "https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?"
	
	def __init__(self, stop_id):
		# route_id,
		# route_id - include with the previous URL
		self.stop_id = stop_id
		# self.route_id = route_id
		self.query_parameter = { 'stopid' : stop_id }
		# 'routeid' : route_id - include with previous URL
		self.url = self._url + urllib.urlencode(self.query_parameter)

	def select_response(self,response):
		values = dict()
		res = response.json()
		values[str(self.stop_id)] = res["results"]
		return json.dumps(values)
		# self.filter_data(self.values)


	def get_route_information(self):
		response = requests.get(self.url)
		#self.values = dict()
		n = str(self.select_response(response))
		return json.loads(n)



'''
## optional static method to prettify json
	
	@staticmethod
	def prettify_json(obj):
		json_ = json.loads(obj)
		return json.dumps(json_, indent=4, sort_keys=True)
'''