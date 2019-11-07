'''
Can also be exported in bash/zsh profile as 
PYTHONPATH="location_of_this_folder/src/DublinBus"
PYTHONPATH="location_of_this_folder/src/DublinBikes"
'''
import argparse
import sys
import json
import unicodedata
import pymongo
from pymongo import MongoClient
import datetime
import bson
sys.path.append('lib/DublinBus/')
sys.path.append('lib/DublinBikes/')
sys.path.append('src/ProducerQueue/')
from DublinBikes import DublinBikes
from DublinBus import DublinBus
# from ProducerQueue import ProducerPipeline
import utils

def main(flag, host, start_index, end_index):
	## init the dublin bus with route_id and id
	# sample = ProducerPipeline(flag, host)
	# run the model between the indices
	# chunk the model into fragments between start and end index
	util = utils.Utilities()
	model_obj = util.chunk_json_object(start_index, end_index)

	for each_object in model_obj:
		stop_num = each_object['id']
		new_dublin_bus = DublinBus(str(stop_num))
		bus_info = new_dublin_bus.get_route_information()
		sample.send_message(bus_info)

if __name__ == '__main__':
	main('test', 'localhost', 0, 100)

'''
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	# default='bus'
	parser.add_argument('--flag', type=str, help='Name of the queue (bus | bike | luas)')
	parser.add_argument('--host', type=str, default='localhost', help='Host where RabbitMQ is running')
	parser.add_argument('--start_index', type=int, default=0, help='Starting index of the model')
	parser.add_argument('--end_index', type=int, help='Ending index of the model')

	args, unparsed = parser.parse_known_args()
	main(args.flag, args.host, args.start_index, args.end_index)
'''