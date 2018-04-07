from analyzer import Analyzer
from fake_sender import FakeSender
from interface import Interface
import ctypes
import os
from semantic import Semantic
from queue import Queue
import requests
from requests.auth import HTTPBasicAuth
import simpleaudio as sa
import tempfile
from receiver import Receiver
import json
def main():
	# global fs, analyzer
	# fs = FakeSender()
	# analyzer = Analyzer(fs.get_queue(), 11)

	q = Queue()
	receiving_list = []
	token_list = []
	context_list = []
	final_string = ""
	r = Receiver(q, receiving_list)
	a = Analyzer(receiving_list, token_list)
	s = Semantic(q, receiving_list, token_list, context_list, final_string)

	interface = Interface(receiving_list, token_list, context_list, final_string, s)

	while True:
		if q.qsize() > 4:
			text = s.parse_queue()
			print(text)
			url = f"https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio/wav&text={text}&voice=es-LA_SofiaVoice"
			username = "e034115b-f434-4cac-a248-bdeccf00498f"
			password = "DeMiAWipCouP"

			r = requests.get(url, auth=HTTPBasicAuth(username, password))

			with tempfile.NamedTemporaryFile("wb") as temp:
				temp.write(r.content)
				wave_obj = sa.WaveObject.from_wave_file(temp.name)
				play_obj = wave_obj.play()
				while play_obj.is_playing():
					continue


# print(fs.get_queue().qsize())


if __name__ == "__main__":
	main()
