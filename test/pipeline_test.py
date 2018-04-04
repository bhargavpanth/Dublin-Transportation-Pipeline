import unittest
import json
import pika

# utilities - consists of model access
import sys
sys.path.append('../utils/')
from utils import Utilities

'''
Note - unittest module expects that method names start with test_
ex: test_return_formatted_url
'''

class Producer_Pipeline(unittest.TestCase):
	""" test suit class """

	def test_rabbitmq_init(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue= 'test_queue')

	def test_return_correct_size_of_model(self):
		utils = Utilities()
		json_ob = utils.chunk_json_object(0,2)
		assertEqual(len(json_ob), 2)


		
if __name__ == '__main__':
	unittest.main()