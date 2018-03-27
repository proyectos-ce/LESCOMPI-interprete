from queue import Queue
import threading

class Receiver:
	"""
	Does something
	"""

	def __init__(self):
		self.queue = Queue()
	#   self.thread = threading.Thread(target=self.repeat, daemon=True)
	#	self.thread.start()

	def stop(self):
		self.status = False
		self.thread.join()

	# def repeat(self):
	# 	while self.status:
	# 		self.queue.put(self.random_number())
	# 		time.sleep(1/80)

	def get_queue(self):
		return self.queue
