import toml
import os


class Semantic:
	def __init__(self, queue):
		self.queue = queue
		self.final_string = ""
		self.list = []
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
			self.list.append(self.parse_id(self.queue.get()))

		self.parse_list()

		tmp = self.final_string.strip()
		self.final_string = ""

		return tmp

	def parse_id(self, id):
		token = self.convert_id_to_token(id)

		if token is not None:
			return token

	def is_word_start(self, token):
		if (len(token) > 1 \
			and token is not "CH" \
			and token is not "LL" \
			and token is not "RR") \
			or token is " ":
				return True
		else:
			return False

	def _debug_print(self, text):
		if __debug__:
			print(text)

	def parse_list(self):
		i = 0
		for token in self.list:
			if isinstance(token, list):
				if i == 0 or (len(self.list[i - 1]) > 0 and isinstance(self.list[i - 1], str)) or (len(self.list[i - 1]) > 0 and isinstance(self.list[i - 1], list)):
					if i + 1 is len(self.list):
						next = None
					else:
						next = self.list[i + 1]

					j = 1
					while next is not None and isinstance(next, list):
						j += 1
						try:
							next = self.list[i + j]
						except IndexError:
							next = None

					if next is None:
						self.final_string += " " + token[0] + " o " + token[1]
						self._debug_print("C0 " + self.final_string)
					else:
						if self._safe_cast(next, int) is not None:
							self.final_string += token[1]
							self._debug_print("C1 " + self.final_string)
						elif self.is_word_start(next):
							self.final_string += " " + token[0] + " o " + token[1]
							self._debug_print("C20 " + self.final_string)
						else:
							self.final_string += token[0]
							self._debug_print("C2 " + self.final_string)
				else:
					if self._safe_cast(self.list[i - 1], int) is not None:  # Si el anterior es número
						self.final_string += token[1]  # Commit del número
						self._debug_print("C3 " + self.final_string)
					else:
						self.final_string += token[0]  # Commit del string
						self._debug_print("C4 " + self.final_string)
			else:
				if self.is_word_start(token):
						self.final_string += " " + token + " "  # Parsear palabras
				else:
					self.final_string += token

			i += 1

		self.list = []