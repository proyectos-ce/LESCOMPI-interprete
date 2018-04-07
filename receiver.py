import paho.mqtt.client as mqtt
import json

class Receiver:
	def on_connect(self, client, userdata, flags, rc):
		print("Connected with result code ", str(rc))
		client.subscribe("leapLescoParse")

	def on_message(self, client, userdata, msg):
		data = msg.payload.decode("utf-8")
		print(data)
		self.queue.put(str(json.loads(data)["id"]))
		self.receivingList.append(str(json.loads(data)["id"]))

	def __init__(self, queue, receivingList):
		client = mqtt.Client()
		client.on_connect = self.on_connect
		client.on_message = self.on_message
		client.connect("iot.eclipse.org", 1883, 60)
		client.loop_start()
		self.queue = queue
		self.receivingList = receivingList
