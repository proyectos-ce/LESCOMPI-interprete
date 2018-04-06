from queue import Queue
import threading
from tkinter import *



class Interface:
    """
    Does something
    """

    def __init__(self):
        root = Tk()
        root.geometry("1000x600")
        canvas = Canvas(root, width=1000, height=600)
        #canvas.grid(row=0, column=0)
        root.title('Test')
        photo = PhotoImage(file='bgrnd.gif')
        canvas.create_image(480, 300, image=photo)
        canvas.pack()
        root.title("Hola mundo")
        root.iconbitmap(r'icon.ico')
        root.mainloop()
        #
        # root = Tk()
        # root.geometry("1000x600")
        # frame = Frame(root)
        # frame.pack()
        # canvas = Canvas(frame)
        # #canvas.grid(row=0, column=0)
        # photo = PhotoImage(file='bgrnd.gif')
        # canvas.create_image(0, 0, image=photo)
        # root.title("Hola mundo")
        # root.iconbitmap(r'icon.ico')
        # root.mainloop()
