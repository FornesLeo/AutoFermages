# -*- coding: utf-8 -*-

from tkinter import *


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pourcent = StringVar()
        self.indice = StringVar()

        self.master.title("Fermages")
        self.master.geometry("400x150")

        label_indice = Label(master, text="Indice national", font=('Arial', 14))
        label_pourcent = Label(master, text="Pourcentage", font=('Arial', 14))

        entry_indice = Entry(master, textvariable=self.indice, font=('Arial', 14))
        entry_pourcent = Entry(master, textvariable=self.pourcent, font=('Arial', 14))

        button_submit = Button(master, text='Envoyer', command=self.quit, font=('Arial', 14))

        label_indice.grid(row=0, column=0, sticky=E, padx=10, pady=10)
        entry_indice.grid(row=0, column=1, padx=10, pady=10)

        label_pourcent.grid(row=1, column=0, sticky=E, padx=10, pady=10)
        entry_pourcent.grid(row=1, column=1, padx=10, pady=10)

        button_submit.grid(row=2, column=1, sticky=W, pady=10)


    def quit(self):
        self.master.quit()

    def get_pourcent(self):
        return self.pourcent.get()

    def get_indice(self):
        return self.indice.get()
