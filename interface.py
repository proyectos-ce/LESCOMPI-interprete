from tkinter import *
from tkinter import messagebox


class Interface:
	def __init__(self, queue, receiving_list, token_list, context_list, final_string, semantic_interface, connected,
	             sender, opq):
		self.root = Tk()
		self.root.geometry("1000x650")
		self.root.title('Test')
		self.receiving_list = receiving_list
		self.token_list = token_list
		self.final_string = final_string
		self.context_list = context_list
		self.semantic_interface = semantic_interface
		self.sender = sender
		self.queue = queue
		listbox_xplace = 55
		listbox_yplace = 150
		self.running = True
		self.opq = opq

		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

		frame = Frame(self.root, width=1000, height=650, bg="#3b8686")
		frame.place(x=0, y=0)

		stetic_frame = Frame(self.root, width=1000, height=115, bg="#0b486b")
		stetic_frame.place(x=0, y=0)

		logo = PhotoImage(file='Lescompi.gif')

		# stetic_logo = Canvas(self.root, width=200, height=100)
		#
		# stetic_logo.create_image(200,100,logo,anchor='nw')
		# stetic_logo.place(x=0, y=0)
		bg_Image = PhotoImage(file='Lescompi.gif')
		canvaslogo = Canvas(self.root, width=410, height=98, borderwidth=0, bg="#0b486b")
		canvaslogo.create_image(201, 51, image=bg_Image)
		canvaslogo.place(x=550, y=5)

		self.connection = connected

		self.canvasonline = Canvas(stetic_frame, borderwidth=0, highlightthickness=0, bg="#0b486b")
		self.canvasonline.place(x=30, y=42)
		self.canvasonline.create_oval(30, 40, 50, 60, fill="gray", outline="#DDD", width=2)
		self.statustext = Label(stetic_frame, text="OFFLINE", width=9, height=2, font=("Helvetica", 22), bg="#0b486b")
		self.statustext.place(x=82, y=66)

		statustitle = Label(stetic_frame, text="STATUS:", width=9, height=1, font=("Helvetica", 26), bg="#0b486b")
		statustitle.place(x=30, y=40)

		# LISTBOX_______ #1
		scrollbar = Scrollbar(frame, orient=VERTICAL)


		self.listbox_1 = Listbox(frame, width=28, height=16, font=(("Helvetica", 18)), yscrollcommand=scrollbar.set)
		scrollbar.config(command=self.listbox_1.yview)
		# scrollbar.pack(side=RIGHT, fill=Y)

		statustitle = Label(frame, text="Entrantes:", width=10, height=1, font=("Helvetica", 26), bg="#3b8686")
		statustitle.place(x=listbox_xplace-14, y=listbox_yplace - 36)

		self.listbox_1.place(x=listbox_xplace, y=listbox_yplace)
		self.listbox_1.insert(END, "Esperando...")


		# LISTBOX_______ #2

		statustitle = Label(frame, text="Tokens:", width=10, height=1, font=("Helvetica", 26), bg="#3b8686")
		statustitle.place(x=listbox_xplace + 276, y=listbox_yplace - 36)

		self.listbox_2 = Listbox(frame, width=28, height=16, font=(("Helvetica", 18)), yscrollcommand=scrollbar.set)
		self.listbox_2.place(x=listbox_xplace + 300, y=listbox_yplace)

		self.listbox_2.insert(END, "Esperando...")

		# LISTBOX_______ #3

		statustitle = Label(frame, text="Contexto:", width=10, height=1, font=("Helvetica", 26), bg="#3b8686")
		statustitle.place(x=listbox_xplace + 590, y=listbox_yplace - 36)

		self.listbox_3 = Listbox(frame, width=28, height=16, font=(("Helvetica", 18)), yscrollcommand=scrollbar.set,
		                         bg="#cff09e")
		self.listbox_3.place(x=listbox_xplace + 600, y=listbox_yplace)
		self.listbox_3.insert(END, " * SIN ANALIZAR * ")
		self.listbox_3.config(state=DISABLED, bg="#c1c1c1")

		# LABEL _____________

		statustitle = Label(frame, text="Texto Final:", width=10, height=1, font=("Helvetica", 26), bg="#3b8686")
		statustitle.place(x=listbox_xplace, y=listbox_yplace + 343)


		self.position=0
		self.pos = Label(frame, text=">>>", width=3, height=1, font=("Helvetica", 24), bg="#3b8686")
		self.pos.place(x=listbox_xplace-48, y=listbox_yplace +390)

		#
		#420
		#450
		self.finaltext = Listbox(frame, width=63, height=3, font=("Helvetica", 26),yscrollcommand=scrollbar.set)
		self.finaltext.place(x=listbox_xplace, y=listbox_yplace + 390)
		self.finaltext.insert(END,"*ESCUCHANDO*")
		self.escuchando=True

		# BUTTON
		self.button = Button(stetic_frame, text="Procesar", font=("Helvetica", 22), command=self.commit)
		self.button.place(x=230, y=40)

		# BUTTON
		self.button = Button(stetic_frame, text="Limpiar", font=("Helvetica", 22), command=self.clean)
		self.button.place(x=382, y=40)

		self.root.title("Insterprete LESCOmpi")
		self.periodicCall()
		self.root.mainloop()

	def clean(self):
		del self.context_list[:]
		self.semantic_interface.clean()
		self.final_string = ""
		del self.token_list[:]
		del self.receiving_list[:]
		self.listbox3_update(self.context_list)
		with self.queue.mutex:
			self.queue.queue.clear()

	def check_connection(self):
		if self.connection[0]:
			self.statustext.config(text="ONLINE")
			self.canvasonline.create_oval(30, 40, 50, 60, fill="green", outline="#DDD", width=2)
		else:
			self.statustext.config(text="OFFLINE")
			self.canvasonline.create_oval(30, 40, 50, 60, fill="grey", outline="#DDD", width=2)

	def update_listbox(self, list1, list2):
		self.erase_first()
		self.insert_listbox_1(list1)
		self.insert_listbox_2(list2)

	def insert_listbox_1(self, lista):
		num = 1
		for i in lista:
			str1 = " Id_" + str(num) + ": {" + str(i) + "}"
			self.listbox_1.insert(END, str1)
			num += 1

	def insert_listbox_2(self, lista):
		num = 1
		for i in lista:
			str1 = " Id_" + str(num) + ": " + str(i)
			self.listbox_2.insert(END, str1)
			num += 1

	def insert_listbox_3(self, lista):
		self.listbox_3.config(state=NORMAL, bg="WHITE")
		self.listbox_3.delete(0, END)
		num = 1
		for i in lista:
			str1 = " Id_" + str(num) + ": {" + str(i) + "}"
			self.listbox_3.insert(END, str1)
			num += 1

	def insert_finaltext(self, texto):
		# if texto == "" or texto ==" ":

		if self.escuchando:
			self.escuchando = False
			self.finaltext.delete(0,END)
			self.position += 1
		elif self.position==0:
			self.position+=1
		elif self.position==1:
			self.position+=1
			self.pos.place(x=55 - 48, y=150 + 420)
		elif self.position == 2:
			self.position += 1
			self.pos.place(x=55 - 48, y=150 + 450)
		if texto != "":
			self.finaltext.insert(END,texto)
			self.finaltext.yview(END)

	def final_update(self, lista, texto):
		self.insert_listbox_3(lista)
		self.insert_finaltext(texto)

	def listbox3_update(self, lista):
		self.insert_listbox_3(lista)

	def erase_first(self):
		self.listbox_1.delete(0, END)
		self.listbox_2.delete(0, END)

	def erase_all(self):
		self.listbox_1.delete(0, END)
		self.listbox_2.delete(0, END)
		self.listbox_3.delete(0, END)
		self.listbox_3.config(state=DISABLED, bg="#c1c1c1")

	def commit(self):
		self.final_string = self.semantic_interface.parse_queue()
		self.final_update(self.context_list, self.final_string.upper())
		self.sender.send(self.final_string)

	def periodicCall(self):
		"""
		Check every 200 ms if there is something new in the queue.
		"""
		self.proccessQueue()
		if not self.running:
			# This is the brutal stop of the system. You may want to do
			# some cleanup before actually shutting it down.
			import sys
			sys.exit(1)
		self.root.after(200, self.periodicCall)

	def proccessQueue(self):
		if self.opq.qsize() > 0:
			if self.opq.get() == 98:
				self.commit()

		self.update_listbox(self.receiving_list, self.token_list)
		self.check_connection()

	def on_closing(self):
		if messagebox.askokcancel("Quit", "Do you want to quit?"):
			self.running = False
