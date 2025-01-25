import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkInputDialog

class Menu:
    
    def __init__(self, root):

        # SEÇÃO DE ATRIBUTOS DE POSICIONAMENTOs

        self._trocax = None
        self._trocaz = None
        self._afastx = None
        self._afastz = None

        # SEÇÃO DE MENU PRINCIPAL

        self.root = root # Recebe como argumento a tela principal do software
        self.root.bind('<Button-3>', self.exibir_menu) # Captura o clique do botão do mouse

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

        self.sub_pos.add_command(label='AFAST. EM X', command=self.afastamentox)
        self.sub_pos.add_command(label='AFAST. EM Z', command=self.afastamentoz)

    @property
    def get_trocax(self):
        return self._trocax
    
    @property
    def get_trocaz(self):
        return self._trocaz

    @property
    def get_afastx(self):
        return self._afastx
    
    @property
    def get_afastz(self):
        return self._afastz

    def exibir_menu(self, event):

        self.menu.post(event.x_root, event.y_root)

    def fechar_tela(self):

        self.root.destroy()

    def trocax(self):

        self.input_pos = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do posicionamento de segurança no eixo X.')
        self.valor_trocax = float(self.input_pos.get_input())

        if self.valor_trocax <= 800 or self.valor_trocax > 1000:

            self.msg = messagebox.showerror(title='Compilador G-Code', message='O valor de troca de ferramenta no eixo X deve estar entre 800 e 1000. Por favor, insira um valor dentro desse intervalo.')
            return

        else:
            self.msg = messagebox.showinfo(title='Compilador G-Code', message='O valor de troca de ferramenta no eixo X foi salvo com sucesso e já está registrado no sistema.')
            self._trocax = self.valor_trocax

    def trocaz(self):

        self.input_pos = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do posicionamento de segurança no eixo Z.')
        self.valor_trocaz = float(self.input_pos.get_input())

        if self.valor_trocaz <= 800 or self.valor_trocaz > 1000:

            msg = messagebox.showerror(title='Compilador G-Code', message='O valor de troca de ferramenta no eixo X deve estar entre 800 e 1000. Por favor, insira um valor dentro desse intervalo.')
            return
        
        else:
            self.msg = messagebox.showinfo(title='Compilador G-Code', message='O valor de troca de ferramenta no eixo Z foi salvo com sucesso e já está registrado no sistema.')
            self._trocaz = self.valor_trocaz

    def afastamentox(self):

        self.input_pos = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do afastamento de segurança no eixo X.')
        self.valor_afastx = float(self.input_pos.get_input())

        if self.valor_afastx <= 800 or self.valor_afastx > 1000:

            msg = messagebox.showerror(title='Compilador G-Code', message='O valor de afastamento de ferramenta no eixo X deve estar entre 800 e 1000. Por favor, insira um valor dentro desse intervalo.')
            return
        
        else:
            self.msg = messagebox.showinfo(title='Compilador G-Code', message='O valor de afastamento da ferramenta no eixo X foi salvo com sucesso e já está registrado no sistema.')
            self._afastx = self.valor_afastx

    def afastamentoz(self):

        self.input_pos = CTkInputDialog(title='Compilador G-Code', text='Por favor, insira o valor do afastamento de segurança no eixo Z.')
        self.valor_afastz = float(self.input_pos.get_input())

        if self.valor_afastz <= 800 or self.valor_afastz > 1000:

            msg = messagebox.showerror(title='Compilador G-Code', message='O valor de afastamento de ferramenta no eixo Z deve estar entre 800 e 1000. Por favor, insira um valor dentro desse intervalo.')
            return
        
        else:
            self.msg = messagebox.showinfo(title='Compilador G-Code', message='O valor de afastamento da ferramenta no eixo Z foi salvo com sucesso e já está registrado no sistema.')
            self._afastz = self.valor_afastz