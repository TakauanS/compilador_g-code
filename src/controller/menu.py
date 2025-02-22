import tkinter as tk
from tkinter import messagebox
from src.model.assents import Assents

class Menu:
    
    def __init__(self, root):

        # SEÇÃO DE MENU PRINCIPAL

        self.__root = root # Recebe como argumento a tela principal do software
        self.__root.bind('<Button-3>', self.exibir_menu) # Captura o clique do botão do mouse

        self.__assents = Assents(master=self.__root)

        self.__menu = tk.Menu(master=self.__root, tearoff=0) # Menu principal
        self.__menu.add_command(label='ATUALIZAR', command=self.atualizar_tela)
        self.__menu.add_command(label='VERSION', command=self.exibir_version)

    def exibir_menu(self, event):

        self.__menu.post(event.x_root, event.y_root)

    def exibir_version(self):

        print(' - Você consultou a versão do software pelo o menu!')
        messagebox.showinfo(title='Compilador G-Code', message='A versão atual do Compilador G-Code é: 1.0')

    def atualizar_tela(self):

        lista_widgets = self.__root.winfo_children()

        for widget in lista_widgets:
            widget.place_forget()

        print(' - A tela foi atualizada com o menu!')