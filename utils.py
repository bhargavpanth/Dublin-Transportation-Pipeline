'''
Split JSON object into chunks of certain size being passed in the init
'''

import json

class Utilities:
	""" Utilities class defines utilities such as chunking JSON file """
	'''
	Model details - route_id, stop_id - total size 115 (Dublin bus)
	'''
	bus_model_path = json.load(open('model/stops.json'))

	def chunk_json_object(self, start_index, end_index):
		# return the chunk of JSON object from start_index and end_index
		routes = []
		for each_route in self.bus_model_path[int(start_index) : int(end_index) + 1]:
			routes.append(each_route)
		return routes


'''

## Transfer this stub to test cases

def main():
	utils = Utilities()
	json_ob = utils.chunk_json_object(0,2)
	# print type(json_ob)
	print len(json_ob)
	print json_ob

if __name__ == '__main__':
	main()

'''