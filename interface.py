from queue import Queue
import threading
from tkinter import *


class Interface:

    def __init__(self):
        root = Tk()
        root.geometry("1000x600")
        root.title('Test')

        frame = Frame(root, width=1000, height=600, bg="RED")
        frame.place(x=0, y=0)

        # LISTBOX_______ #1
        scrollbar = Scrollbar(frame, orient=VERTICAL)
        self.listbox_1 = Listbox(frame, width=20, height=20, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox_1.yview)
        # scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox_1.place(x=100, y=100)

        self.insert_listbox_1(["42", "25", "99", "24", "12"])

        # for i in range(0, 18):
        #     self.insert_listbox_1(" Id_2: {14}")

        # LISTBOX_______ #2
        self.listbox_2 = Listbox(frame, width=20, height=20)
        self.listbox_2.place(x=300, y=100)

        lista = [("A", "Letra"), ("1", "Numero"), (" ", "Espacio"), ("Hola", "Palabra")]
        self.insert_listbox_2(lista)

        # LISTBOX_______ #3
        self.listbox_3 = Listbox(frame, width=20, height=20)
        self.listbox_3.place(x=500, y=100)
        self.listbox_3.insert(END, " * SIN ANALIZAR * ")
        self.listbox_3.config(state=DISABLED, bg="#c1c1c1")

        root.title("Interprete LESCOmpi")
        root.iconbitmap(r'icon.ico')
        root.mainloop()

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

    def insert_listbox_3(self, str):
        self.listbox_3.insert(END, str)

    def erase_all(self):
        self.listbox_1.delete(0, END)
        self.listbox_2.delete(0, END)
        self.listbox_3.delete(0, END)
