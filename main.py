from analyzer import Analyzer
from fake_sender import FakeSender
from interface import Interface
import ctypes
import os
import toml

if os.name == 'nt':
	myappid = 'cr.tec.lescompi'
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


def main():
	try:
		data = toml.load("lesco.toml")
	except:
		print("Error al decodificar los datos de lesco.toml. Verificar el formato del archivo.")
		os.sys.exit(2)

	print(data)
	global fs, analyzer
	fs = FakeSender()
	analyzer = Analyzer(fs.get_queue(), 11)
	interface = Interface()


# print(fs.get_queue().qsize())


if __name__ == "__main__":
	main()
