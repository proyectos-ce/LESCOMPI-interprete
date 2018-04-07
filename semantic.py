import toml
import os


class Semantic:
	def __init__(self, queue, receiving_list, token_list, context_list, final_string):
		self.queue = queue
		self.final_string = final_string
		self.context_list = context_list
		self.list = []
		self.receiving_list = receiving_list
		self.token_list = token_list
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
		if self.queue.qsize() > 0:
			while self.queue.qsize() > 0:
				self.list.append(self.parse_id(self.queue.get()))

			self.parse_list()
			self.final_string = self.final_string.replace("[CNTX]", "")
			self.final_string = self.final_string.replace("  ", " ")
			return self.final_string
		else:
			self.parse_list()
			self.final_string = self.final_string.replace("[CNTX]", "")
			self.final_string = self.final_string.replace("  ", " ")
			return self.final_string

	def parse_id(self, id):
		token = self.convert_id_to_token(id)

		if token is not None:
			return token

	def is_word_start(self, token):
		token = token.strip().upper()
		if (len(token) > 1 and not (token == "CH" or token == "LL" or token == "RR")) or token == " ":
				return True
		else:
			return False

	def _debug_print(self, text):
		if __debug__:
			print(text)

	def commit(self, value, representation=None):
		if representation:
			self.context_list.append(representation.strip() + " [CNTX]")
			self.final_string += representation
		else:
			self.context_list.append(value.strip())
			self.final_string += value

	def clean(self):
		self.final_string = ""
		del self.context_list[:]
		del self.list[:]

	def parse_list(self):
		del self.context_list[:]
		self.final_string = ""
		i = 0
		for token in self.list:
			if token == " ":
				i += 1
				continue

			if isinstance(token, list):
				print("is list")
				if i == 0 or (len(self.list[i - 1]) > 1 and isinstance(self.list[i - 1], str) and not (self.list[i - 1] == "CH" or self.list[i - 1] == "RR" or self.list[i - 1] == "LL")) or (len(self.list[i - 1]) > 1 and isinstance(self.list[i - 1], list)):
					if isinstance(self.list[i - 1], str) and self.list[i - 1].strip().upper() == "CUMPLEAÑOS":
						self.commit(token[1])  # Commit del número
						self.list[i] = token[1]
						i += 1
						continue

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
						self.commit(" " + token[0] + " o " + token[1] + " ")
						self._debug_print("C0 " + self.final_string)
					else:
						if self._safe_cast(next, int) is not None:
							self.commit(token[1])
							self._debug_print("C1 " + self.final_string)
						elif self.is_word_start(next):
							self.commit(" " + token[0] + " o " + token[1] + " ")
							self._debug_print("C20 " + self.final_string)
						else:
							self.commit(token[0])
							self._debug_print("C2 " + self.final_string)
				else:
					if self._safe_cast(self.list[i - 1], int) is not None:  # Si el anterior es número
						self.commit(token[1])  # Commit del número
						self.list[i] = token[1]
						self._debug_print("C3 " + self.final_string)
					else:
						self.commit(token[0])  # Commit del string
						self.list[i] = token[0]
						self._debug_print("C4 " + self.final_string)
			else:
				if token.strip().upper() == "CUMPLEAÑOS":
					self.commit(" " + token + " ", " cumple ")
					self.list_add_after(i + 1, " años [CNTX]")
				elif token.strip().upper() == "YO" and len(self.list) > i + 1 and self.list[i + 1].strip().upper() == "NOMBRE":
					self.commit(token, " mi ")
					self.commit(" nombre ", " nombre es ")
					self.list[i + 1] = " "
				elif token.strip().upper() == "YO" and len(self.list) > i + 1 and self.list[i + 1].strip().upper() == "CASA":
					self.commit(" " + token + " ")
					self.commit(" vivo ", " vivo en ")
					self.list[i + 1] = " "
				elif token.strip().upper() == "DÓNDE" and len(self.list) > i + 1:
					self.commit(" " + token + " ", " dónde está ")
				elif self.is_word_start(token):
					self.commit(" " + token + " ")  # Parsear palabras
				else:
					self.commit(token)

			i += 1

	def list_add_after(self, position, token):
		for i in range(len(self.list)):
			if i + 1 == len(self.list):
				self.list.append(token)
				return
			if i > position:
				if len(self.list[i] > 1 and not (self.list[i] == "CH" or self.list[i] == "LL" or self.list[i] == "RR")):
					self.list.insert(token, i)
