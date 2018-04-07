import paho.mqtt.client as mqtt
import json

class Sender:
	def on_connect(self, client, userdata, flags, rc):
		print("Connected with result code ", str(rc))

	def on_disconnect(self, client, userdata, rc):
		print("Desconectado")

	def send(self, msg):
		self.client.publish("leapLescoSound", payload=msg, qos=0)

	def __init__(self):
		self.client = mqtt.Client()
		self.client.on_connect = self.on_connect
		self.client.on_disconnect = self.on_disconnect
		try:
			self.client.connect("iot.eclipse.org", 1883, 60)
			self.client.loop_start()
		except:
			print("No se puede conectar sonido")