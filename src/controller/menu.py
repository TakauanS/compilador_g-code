import tkinter as tk
from customtkinter import CTkInputDialog

class Menu:
    
    def __init__(self, root):
        
        self.root = root # Recebe como argumento a tela principal do software
        self.root.bind('<Button-3>', self.exibir_menu) # Captura o clique do botão do mouse

        # SEÇÃO DE MENU PRINCIPAL

        self.menu = tk.Menu(master=self.root, tearoff=0) # Menu principal
        self.sub_pos = tk.Menu(master=self.menu, tearoff=0) # Sub-menu posicionamentos

        self.menu.add_cascade(label='POSICIONAMENTO', menu=self.sub_pos)
        self.menu.add_command(label='AJUDA')

        self.menu.add_separator()

        self.menu.add_command(label='SAIR', command=self.fechar_tela)

        # SEÇÃO DE SUBMENUs - POSICIONAMENTOS

        self.sub_pos.add_command(label='TROCA EM X', command=self.trocax)
        self.sub_pos.add_command(label='TROCA EM Z', command=self.trocaz)

        self.sub_pos.add_separator()

        self.sub_pos.add_command(label='AFAST. EM X')
        self.sub_pos.add_command(label='AFAST. EM Z')

    def exibir_menu(self, event):

        self.menu.post(event.x_root, event.y_root)

    def fechar_tela(self):

        self.root.destroy()

    def trocax(self):

        input_pos = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do posicionamento de segurança no eixo X.')

    def trocaz(self):

        input_pos = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do posicionamento de segurança no eixo Z.')