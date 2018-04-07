import time
import threading

from list_parser import ListParser


class Analyzer:
	def __init__(self, queue, number):
		self.list = []
		self.number = number
		self.queue = queue
		self.running = True
		self.thread = threading.Thread(target=self.repeat, daemon=True)
		self.thread.start()

		self.finalCodes = []
		self.parser = ListParser()

		self.lastCode = None

	def stop(self):
		self.running = False
		self.thread.join()

	def repeat(self):
		while self.running:
			while len(self.list) < self.number:
				self.list.append(self.queue.get())
				time.sleep(1 / (self.number / 1.5))

			data = self.parser.percent_analyzer(self.list, self.number)

			if len(data) > 1 and data[0][0] == data[1][0]:
				if data[0][1] == self.lastCode:
					if self.lastCode is not None:
						self.finalCodes.append(self.lastCode)
					self.lastCode = data[1][1]
				else:
					if self.lastCode is not None:
						self.finalCodes.append(self.lastCode)
					self.lastCode = data[0][1]

			if data[0][1] != self.lastCode:
				if self.lastCode is not None:
					self.finalCodes.append(self.lastCode)
				self.lastCode = data[0][1]

			self.list = self.list[1:]
