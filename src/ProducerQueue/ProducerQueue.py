
import pika
import json
import datetime
import time

class ProducerPipeline:

	# replace with remote URL (if required)
	# host = 'localhost'

	def __init__(self, flag, host):
		self.flag = flag
		self.host = host
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue= self.flag)

	def send_message(self, message):
		self.channel.basic_publish(exchange='', routing_key=self.flag, body=json.dumps(message))
		## generating log
		#print ('sent ', message, datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		return True

	def terminate_connection(self):
		self.connection.close()
