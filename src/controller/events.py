from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(base_dir)

from src.model.assents import Assents
from src.controller.utils import Utils

from src.controller.back_cycles.back_faceamento import BackFaceamento
from src.controller.back_cycles.back_desbaste import BackDesbaste
from src.controller.back_cycles.back_canais import BackCanais

from src.controller.back_cycles.back_desbastef import BackDesbasteF

class ButtonHandler:

    # SEÇÃO DE EXPORTAÇÃO DE IMAGEs

    img_linha = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha.png'), size=(825, 20))
    img_code = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/code.png'), size=(24, 24))

    def __init__(self, master):

        self.master = master
        self.assents = Assents(master=self.master)
        self.utils_cmds = Utils(master=self.master)
        
        self.comandos = {
            "! compile -c: desbaste": self.back_desbaste,
            "! compile -c: canais": self.back_canais,
            "! compile -c: faceamento": self.back_faceamento,
            "! compile -c: desbaste (f)": self.back_desbastef
        }

        self.utils = {
            '! compile -list': self.list,
            '! compile -list: cycles': self.list_cycles
        }

        self.lista_comandos = [self.comandos, self.utils]

    def executar_comando(self, comando):

        if comando in self.comandos:
            self.comandos[comando]()
            return

        if comando in self.utils:
            self.utils[comando]()
            return

        else:
            messagebox.showerror(title='Compilador G-Code', message='O comando informado não existe no sistema. Por favor, verifique e tente novamente.')
            return

    # SEÇÃO DE MÉTODOS DE CICLOS PARAMETRIZADOs

    def back_desbaste(self):

        self.utils_cmds.limpar_tela()
        self.__desbaste = BackDesbaste(master=self.master)

    def back_canais(self):

        self.utils_cmds.limpar_tela()
        self.__canais = BackCanais(master=self.master)

    def back_faceamento(self):

        self.utils_cmds.limpar_tela()
        self.__faceamento = BackFaceamento(master=self.master)

    # SEÇÃO DE MÉTODOS DE CICLOS FUNCIONAIs

    def back_desbastef(self):

        self.utils_cmds.limpar_tela()
        self.__desbastef = BackDesbasteF(master=self.master)

    # SEÇÃO DE MÉTODOS UTILs

    def list(self):
        
        self.utils_cmds.limpar_tela()
        self.utils_cmds.list_comands()

    def list_cycles(self):

        self.utils_cmds.limpar_tela()
        self.utils_cmds.list_cycles()