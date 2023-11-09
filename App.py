# -*- coding: utf-8 -*-

from tkinter import *


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pourcent = StringVar()
        self.indice = StringVar()

        Label(master, text="Indice nationnal", font=('Arial', 10)).grid(row=0)
        Label(master, text="Pourcentage", font=('Arial', 10)).grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e1["textvariable"] = self.indice
        self.e2["textvariable"] = self.pourcent

        Button(master, text='envoyer', command=self.quit).grid(row=3, column=1, sticky=W, pady=4)

    def quit(self):
        self.master.quit()

    def get_pourcent(self):
        return self.pourcent.get()

    def get_indice(self):
        return self.indice.get()
