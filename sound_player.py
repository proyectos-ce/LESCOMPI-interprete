import paho.mqtt.client as mqtt
import requests
from requests.auth import HTTPBasicAuth
import uuid
from subprocess import call

class Receiver:
	def on_connect(self, client, userdata, flags, rc):
		print("Connected to sound with result code ", str(rc))
		client.subscribe("leapLescoSound")

	def on_disconnect(self, client, userdata, rc):
		print("Desconectado")

	def on_message(self, client, userdata, msg):
		data = msg.payload.decode("utf-8")
		url = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio/wav&text=" + data + "&voice=es-LA_SofiaVoice"
		username = "e034115b-f434-4cac-a248-bdeccf00498f"
		password = "DeMiAWipCouP"

		r = requests.get(url, auth=HTTPBasicAuth(username, password))

		unique_filename = str(uuid.uuid4())

		with open(unique_filename + ".wav", "wb") as temp:
			temp.write(r.content)
			print("Reproduciendo " + temp.name)
			call(["cvlc", "--play-and-exit", temp.name])

	def __init__(self):
		client = mqtt.Client()
		client.on_connect = self.on_connect
		client.on_message = self.on_message
		client.on_disconnect = self.on_disconnect
		client.connect("iot.eclipse.org", 1883, 60)
		client.loop_forever()

r = Receiver()