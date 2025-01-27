from customtkinter import CTkLabel, CTkEntry
import customtkinter as ctk

class Assents:

    def __init__(self, master):

        self.master = master

    def criar_label(self, text, x, y):

        self.label = CTkLabel(master=self.master, text=text, font=('Corbel', 23), text_color='white')
        self.label.place(x=x, y=y)

    def criar_entry(self, x, y):

        self.entry = CTkEntry(master=self.master, corner_radius=12, width=200, font=('Consola', 16))
        self.entry.place(x=x, y=y)

        return self.entry