import threading
from semantic import Semantic
from queue import Queue


class Analyzer:
	def __init__(self, receiving_list, token_list):
		self.receiving_list = receiving_list
		self.token_list = token_list
		self.running = True
		self.thread = threading.Thread(target=self.repeat, daemon=True)
		self.thread.start()
		self.s2 = Semantic(Queue(), [], [], [], "")

	def stop(self):
		self.running = False
		self.thread.join()

	def repeat(self):
		while self.running:
			while len(self.receiving_list) is not len(self.token_list):
				try:
					token = self.s2.convert_id_to_token(self.receiving_list[len(self.token_list)])
				except:
					continue
				if isinstance(token, list):
					type = "LETRA|NUM"
				elif self.s2._safe_cast(token, int):
					type = "NUM"
				elif token == " ":
					type = "ESPACIO"
				elif len(token) > 1 and not (token == "CH" or token == "LL" or token == "RR"):
					type = "PALABRAS"
				else:
					type = "LETRA"
				self.token_list.append((token, type))
