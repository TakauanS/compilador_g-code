import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkInputDialog

class Menu:
    
    def __init__(self, root):

        # SEÇÃO DE ATRIBUTOS DE POSICIONAMENTOs

        self.__posx = 400.0
        self.__posz = 1.0

        # SEÇÃO DE MENU PRINCIPAL

        self.__root = root # Recebe como argumento a tela principal do software
        self.__root.bind('<Button-3>', self.exibir_menu) # Captura o clique do botão do mouse

        self.__menu = tk.Menu(master=self.__root, tearoff=0) # Menu principal
        self.__sub_pos = tk.Menu(master=self.__menu, tearoff=0) # Sub-menu posicionamentos

        self.__menu.add_cascade(label='POSICIONAMENTO', menu=self.__sub_pos)
        self.__menu.add_cascade(label='ATUALIZAR', command=self.atualizar_tela)

        self.__menu.add_separator()

        self.__menu.add_command(label='AJUDA')

        # SEÇÃO DE SUBMENUs - POSICIONAMENTOS

        self.__sub_pos.add_command(label='SEGURANÇA (X)', command=self.posx)
        self.__sub_pos.add_command(label='SEGURANÇA (Z)', command=self.posz)

    @property
    def get_posx(self):
        return self.__posx
    
    @property
    def get_posz(self):
        return self.__posz

    @get_posx.setter
    def set_posx(self, nova_posx: float):

        if not isinstance(nova_posx, float):
            messagebox.showerror(title='Compilador G-Code', message='O valor de segurança no eixo X não foi informado. Por favor, insira um valor válido.')
            raise ValueError ('O valor de segurança no eixo X deve ser do tipo `float`.')
        
        self.__posx = nova_posx

    @get_posz.setter
    def set_posz(self, nova_posz: float):

        if not isinstance(nova_posz, float):
            messagebox.showerror(title='Compilador G-Code', message='O valor de segurança no eixo Z não foi informado. Por favor, insira um valor válido.')
            raise ValueError ('O valor de segurança no eixo Z deve ser do tipo `float`.')
        
        self.__posz = nova_posz

    def exibir_menu(self, event):

        self.__menu.post(event.x_root, event.y_root)

    def posx(self):

        self.__input_posx = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do posicionamento de segurança no eixo X.')
        self.__valor_posx = float(self.__input_posx.get_input())

        self.__posx = self.__valor_posx
        print(f' - O valor de posicionamento de segurança no eixo X foi configurado! ({self.get_posx})')

    def posz(self):

        self.__input_posz = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do posicionamento de segurança no eixo Z.')
        self.__valor_posz = float(self.__input_posz.get_input())

        self.__posz = self.__valor_posz
        print(f' - O valor de posicionamento de segurança no eixo Z foi configurado! ({self.get_posz})')

    def atualizar_tela(self):

        lista_widgets = self.__root.winfo_children()

        for widget in lista_widgets:
            widget.place_forget()

        print(' - A tela foi atualizada com o menu!')