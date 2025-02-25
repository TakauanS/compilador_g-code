from tkinter import messagebox
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(base_dir)

from src.model.assents import Assents
from src.controller.utils import Utils

from src.controller.back_cycles.cycles_parametrizados.back_faceamento import BackFaceamento
from src.controller.back_cycles.cycles_parametrizados.back_desbaste import BackDesbaste
from src.controller.back_cycles.cycles_parametrizados.back_canais import BackCanais

from src.controller.back_cycles.cycles_funcionais.back_faceamentof import BackFaceamentoF
from src.controller.back_cycles.cycles_funcionais.back_desbastef import BackDesbasteF
from src.controller.back_cycles.cycles_funcionais.back_canaisf import Back_CanaisF

class ButtonHandler:

    def __init__(self, master):

        self.master = master
        self.assents = Assents(master=self.master)
        self.utils_cmds = Utils(master=self.master)
        
        self.comandos = {
            "! compile -c: faceamento": self.back_faceamento,
            "! compile -c: desbaste": self.back_desbaste,
            "! compile -c: canais": self.back_canais,
            "! compile -c: faceamento (f)": self.back_faceamentof,
            "! compile -c: desbaste (f)": self.back_desbastef,
            "! compile -c: canais (f)": self.back_canaisf
        }

        self.utils = {
            '! compile -list': self.list,
            '! compile -list: cycles': self.list_cycles
        }

        self.lista_comandos = [self.comandos, self.utils]

    def executar_comando(self, comando):

        if comando in self.comandos:
            print(f' - Você chamou o comando: {comando}')
            self.comandos[comando]()
            return

        if comando in self.utils:
            print(f' - Você chamou o comando: {comando}')
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

    def back_faceamentof(self):

        self.utils_cmds.limpar_tela()
        self.__faceamentof = BackFaceamentoF(master=self.master)

    def back_canaisf(self):

        self.utils_cmds.limpar_tela()
        self.__canaisf = Back_CanaisF(master=self.master)

    # SEÇÃO DE MÉTODOS UTILs

    def list(self):
        
        self.utils_cmds.limpar_tela()
        self.utils_cmds.list_comands()

    def list_cycles(self):

        self.utils_cmds.limpar_tela()
        self.utils_cmds.list_cycles()