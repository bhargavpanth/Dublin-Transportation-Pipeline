import json

class Utilities:
	bus_model_path = json.load(open('model/stops.json'))
	def chunk_json_object(self, start_index, end_index):
		routes = []
		for each_route in self.bus_model_path[int(start_index) : int(end_index) + 1]:
			routes.append(each_route)
		return routes
