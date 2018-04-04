'''
Building the Dublin Bikes into a pyton module
'''

import requests
import urllib
import json

class DublinBikes(object):
	""" DublinBikes Module """

	_url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&"
	key = "apiKey"
	val = "eae2a42f57ee0e99c46335e5960c1619eea2ded4"

	def __init__(self):
		self.query_parameter = { DublinBikes.key : self.val}
		self.url = self._url + urllib.urlencode(self.query_parameter)

	def get_route_information(self):
		response = requests.get(self.url)
		# type - <class 'requests.models.Response'>
		return json.loads(response.text)

## stub - comment out

# def main():
# 	r = DublinBikes()
# 	resp = r.get_route_information()
# 	print (json.loads(resp.text))

# main()