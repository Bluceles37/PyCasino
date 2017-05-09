# -*- coding:utf-8 -*-

from tkinter import *


w = Tk()
w.title("Shit")
w.geometry('1280x720')
w.resizable(width=False, height=False)


tamer = Canvas(w, width=1280, height=720, bg="green")
Entree = Entry(tamer, textvariable="string", width=30)

Entree.pack()
tamer.pack()


w.mainloop()