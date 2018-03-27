import time
from queue import Queue
from random import randrange
import threading

class FakeSender:
	"""
	Does something
	"""

	def __init__(self):
		self.status = True
		self.queue = Queue()
		self.thread = threading.Thread(target=self.repeat, daemon=True)
		self.thread.start()

	def random_number(self):
		return randrange(0, 100)

	def stop(self):
		self.status = False
		self.thread.join()

	def repeat(self):
		while self.status:
			self.queue.put(self.random_number())
			time.sleep(1/80)

	def get_queue(self):
		return self.queue


