import paho.mqtt.client as mqtt
import simpleaudio as sa
import tempfile
import requests
from requests.auth import HTTPBasicAuth

class Receiver:
	def on_connect(self, client, userdata, flags, rc):
		print("Connected with result code ", str(rc))
		client.subscribe("leapLescoSound")

	def on_disconnect(self, client, userdata, rc):
		print("Desconectado")

	def on_message(self, client, userdata, msg):
		data = msg.payload.decode("utf-8")
		url = f"https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio/wav&text={data}&voice=es-LA_SofiaVoice"
		username = "e034115b-f434-4cac-a248-bdeccf00498f"
		password = "DeMiAWipCouP"

		r = requests.get(url, auth=HTTPBasicAuth(username, password))

		with tempfile.NamedTemporaryFile("wb") as temp:
			temp.write(r.content)
			wave_obj = sa.WaveObject.from_wave_file(temp.name)
			play_obj = wave_obj.play()
			while play_obj.is_playing():
				continue

	def __init__(self):
		client = mqtt.Client()
		client.on_connect = self.on_connect
		client.on_message = self.on_message
		client.on_disconnect = self.on_disconnect
		client.connect("iot.eclipse.org", 1883, 60)
		client.loop_forever()

r = Receiver()