import paho.mqtt.client as mqtt


class Receiver:
	def on_connect(self, client, userdata, flags, rc):
		print("Connected with result code ", str(rc))
		client.subscribe("leapLesco")

	def on_message(self, client, userdata, msg):
		print(msg.payload)

	def __init__(self):
		client = mqtt.Client()
		client.on_connect = self.on_connect
		client.on_message = self.on_message
		client.connect("iot.eclipse.org", 1883, 60)
		client.loop_forever()
