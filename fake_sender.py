import time
from queue import Queue
from random import randrange
import threading

class FakeSender:
	"""
	Does something
	"""

	def __init__(self):
		self.running = True
		self.queue = Queue()
		self.thread = threading.Thread(target=self.repeat, daemon=True)
		self.thread.start()

	def random_number(self):
		return randrange(0, 20)

	def stop(self):
		self.running = False
		self.thread.join()

	def repeat(self):
		while self.running:
			self.queue.put(self.random_number())
			time.sleep(1/2)

	def get_queue(self):
		return self.queue


