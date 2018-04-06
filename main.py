from analyzer import Analyzer
from fake_sender import FakeSender
from interface import Interface
import ctypes
import os

if os.name == 'nt':
	myappid = 'cr.tec.lescompi'
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


def main():
	global fs, analyzer
	fs = FakeSender()
	analyzer = Analyzer(fs.get_queue(), 11)
	interface = Interface()


# print(fs.get_queue().qsize())


if __name__ == "__main__":
	main()
