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
				self.token_list.append((self.s2.convert_id_to_token(self.receiving_list[len(self.token_list)]), "TEST"))
