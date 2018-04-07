from analyzer import Analyzer
from fake_sender import FakeSender
from interface import Interface
import ctypes
import os
from semantic import Semantic
from queue import Queue
from receiver import Receiver
import json
from sender import Sender

def main():
	# global fs, analyzer
	# fs = FakeSender()
	# analyzer = Analyzer(fs.get_queue(), 11)

	q = Queue()
	receiving_list = []
	token_list = []
	context_list = []
	final_string = ""
	connected = [0]
	r = Receiver(q, receiving_list, connected)
	a = Analyzer(receiving_list, token_list)
	s = Semantic(q, receiving_list, token_list, context_list, final_string)
	sender = Sender()

	interface = Interface(q, receiving_list, token_list, context_list, final_string, s, connected, sender)



# print(fs.get_queue().qsize())


if __name__ == "__main__":
	main()
