import toml
import os


class Semantic:
	def __init__(self, queue):
		self.queue = queue
		self.final_string = ""
		self.final_list = []
		try:
			self.data = toml.load("lesco.toml")
		except:
			print("Error al decodificar los datos de lesco.toml. Verificar el formato del archivo.")
			os.sys.exit(2)

	def get_result(self):
		tmp = self.final
		self.final = ""
		return tmp

	def _safe_cast(self, val, to_type, default=None):
		try:
			return to_type(val)
		except (ValueError, TypeError):
			return default

	def convert_id_to_token(self, id):
		id = self._safe_cast(id, str)
		if id is not None and id in self.data["ids"]:
			return self.data["ids"][id]
		else:
			return None

	def parse_queue(self):
		while self.queue.qsize() > 0:
			self.final_list.append(self.parse_id(self.queue.get()))

		self.parse_list()

		return self.final_string

	def parse_id(self, id):
		token = self.convert_id_to_token(id)

		if token is not None:
			return token

	def parse_list(self):
		i = 0
		for token in self.list:
			if isinstance(token, list):
				if i == 0 or (len(self.list[i - 1]) > 0 and isinstance(self.list[i - 1], str)):
					# considerarSiguiente
					return None
				else:
					# considerarAnterior
					return None
			else:
				if len(token) > 1 \
					and token is not "CH" \
					and token is not "LL" \
					and token is not "RR":
						self.final_string += token + " "
				else:
					self.final_string += token

			i += 1

		self.final_list = []
		tmp = self.final_string
		self.final_string = []
		return tmp
