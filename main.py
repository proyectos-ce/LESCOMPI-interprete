import threading
from queue import Queue

from fake_sender import FakeSender


def main():
	global fs
	fs = FakeSender()
	print(fs.get_queue().qsize())



if __name__ == "__main__":
	main()