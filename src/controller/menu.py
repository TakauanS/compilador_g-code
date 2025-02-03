import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkInputDialog

class Menu:
    
    def __init__(self, root):

        # SEÇÃO DE ATRIBUTOS DE POSICIONAMENTOs

        self._posx = None
        self._posz = None

        # SEÇÃO DE MENU PRINCIPAL

        self.root = root # Recebe como argumento a tela principal do software
        self.root.bind('<Button-3>', self.exibir_menu) # Captura o clique do botão do mouse

        self.menu = tk.Menu(master=self.root, tearoff=0) # Menu principal
        self.sub_pos = tk.Menu(master=self.menu, tearoff=0) # Sub-menu posicionamentos

        self.menu.add_cascade(label='POSICIONAMENTO', menu=self.sub_pos)
        self.menu.add_cascade(label='ATUALIZAR', command=self.atualizar_tela)

        self.menu.add_separator()

        self.menu.add_command(label='AJUDA')

        # SEÇÃO DE SUBMENUs - POSICIONAMENTOS

        self.sub_pos.add_command(label='SEGURANÇA (X)', command=self.posx)
        self.sub_pos.add_command(label='SEGURANÇA (Z)', command=self.posz)

    @property
    def get_posx(self):
        return self._posx
    
    @property
    def get_posz(self):
        return self._posz

    def exibir_menu(self, event):

        self.menu.post(event.x_root, event.y_root)

    def posx(self):

        self.input_pos = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do posicionamento de segurança no eixo X.')
        self.valor_posx = float(self.input_pos.get_input())

        if self.valor_posx <= 800 or self.valor_posx > 1000:

            messagebox.showerror(title='Compilador G-Code', message='O valor de segurança de ferramenta no eixo X deve estar entre 800 e 1000. Por favor, insira um valor dentro desse intervalo.')
            return

        else:
            messagebox.showinfo(title='Compilador G-Code', message='O valor de troca de segurança no eixo X foi salvo com sucesso e já está registrado no sistema.')
            self._posx = self.valor_posx

    def posz(self):

        self.input_pos = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do posicionamento de segurança no eixo Z.')
        self.valor_posz = float(self.input_pos.get_input())

        if self.valor_posz <= 800 or self.valor_posz > 1000:

            messagebox.showerror(title='Compilador G-Code', message='O valor de segurança de ferramenta no eixo Z deve estar entre 800 e 1000. Por favor, insira um valor dentro desse intervalo.')
            return

        else:
            messagebox.showinfo(title='Compilador G-Code', message='O valor de troca de segurança no eixo Z foi salvo com sucesso e já está registrado no sistema.')
            self._posz = self.valor_posz
            
    def atualizar_tela(self):

        lista_widgets = self.root.winfo_children()

        for widget in lista_widgets:
            widget.place_forget()

        print('- A tela foi atualizada com o menu!')