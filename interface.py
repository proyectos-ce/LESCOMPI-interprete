from tkinter import *


class Interface:

    def __init__(self):
        root = Tk()
        root.geometry("1000x650")
        root.title('Test')

        listbox_xplace = 55
        listbox_yplace = 150


        frame = Frame(root, width=1000, height=650, bg="#3b8686")
        frame.place(x=0, y=0)

        stetic_frame = Frame(root, width=1000, height=115, bg="#0b486b")
        stetic_frame.place(x=0, y=0)

        logo = PhotoImage(file = 'Lescompi.gif')

        # stetic_logo = Canvas(root, width=200, height=100)
        #
        # stetic_logo.create_image(200,100,logo,anchor='nw')
        # stetic_logo.place(x=0, y=0)
        bg_Image = PhotoImage(file='Lescompi.gif')
        canvaslogo = Canvas(root, width=410, height=98,borderwidth=0,bg="#0b486b")
        canvaslogo.create_image(201, 51, image=bg_Image)
        canvaslogo.place(x=550, y=5)

        # LISTBOX_______ #1
        scrollbar = Scrollbar(frame, orient=VERTICAL)
        self.listbox_1 = Listbox(frame, width=28, height=16,font= (("Helvetica", 18)), yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox_1.yview)
        # scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox_1.place(x=listbox_xplace, y=listbox_yplace)
        self.listbox_1.insert(END, "Esperando...")

        # for i in range(0, 18):
        #     self.insert_listbox_1(" Id_2: {14}")

        # LISTBOX_______ #2
        self.listbox_2 = Listbox(frame, width=28, height=16,font= (("Helvetica", 18)),yscrollcommand=scrollbar.set)
        self.listbox_2.place(x=listbox_xplace+300, y=listbox_yplace)

        self.listbox_2.insert(END, "Esperando...")

        # LISTBOX_______ #3
        self.listbox_3 = Listbox(frame, width=28, height=16,font= (("Helvetica", 18)),yscrollcommand=scrollbar.set, bg="#cff09e")
        self.listbox_3.place(x=listbox_xplace+600, y=listbox_yplace)
        self.listbox_3.insert(END, " * SIN ANALIZAR * ")
        self.listbox_3.config(state=DISABLED, bg="#c1c1c1")

        # LABEL _____________
        self.finaltext = Label(frame, text="Hello, world!",width=38, height=2, font=("Helvetica", 42))
        self.finaltext.place(x=listbox_xplace, y=listbox_yplace + 370)
        self.finaltext.config(text="*ESCUCHANDO*")

        #self.erase_all()

        root.title("Interprete LESCOmpi")
        root.mainloop()

    def update_listbox(self,list1,list2):
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

    def insert_listbox_3(self, str):
        self.listbox_3.insert(END, str)

    def erase_first(self):
        self.listbox_1.delete(0, END)
        self.listbox_2.delete(0, END)

    def erase_all(self):
        self.listbox_1.delete(0, END)
        self.listbox_2.delete(0, END)
        self.listbox_3.delete(0, END)
        self.finaltext.config(text=" *En Proceso* ")

