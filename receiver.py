import paho.mqtt.client as mqtt
import json

class Receiver:
	def on_connect(self, client, userdata, flags, rc):
		print("Connected with result code ", str(rc))
		client.subscribe("facebook")

	def on_message(self, client, userdata, msg):
		data = msg.payload.decode("utf-8")
		print(data)
		#self.queue.put(str(json.loads(data)["id"]))

	def __init__(self, queue):
		client = mqtt.Client()
		client.on_connect = self.on_connect
		client.on_message = self.on_message
		client.connect("iot.eclipse.org", 1883, 60)
		client.loop_start()
		self.queue = queue
