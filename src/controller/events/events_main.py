from tkinter import messagebox
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(base_dir)

from src.model.assents import Assents
from src.controller.events.events_utils import Utils

# SEÇÃO DE IMPORTAÇÕES DE CLASSES - PARAMETRIZADOS

from src.controller.manager_cycles.cycles_parametrizados.faceamentop_manager import FaceamentoP_Manager
from src.controller.manager_cycles.cycles_parametrizados.desbastep_manager import DesbasteP_Manager
from src.controller.manager_cycles.cycles_parametrizados.furacaop_manager import FuracaoP_Manager
from src.controller.manager_cycles.cycles_parametrizados.canaisp_manager import CanaisP_Manager

# SEÇÃO DE IMPORTAÇÕES DE CLASSES - FUNCIONAIS

from src.controller.manager_cycles.cycles_funcionais.faceamentof_manager import FaceamentoF_Manager
from src.controller.manager_cycles.cycles_funcionais.desbastef_manager import DesbasteF_Manager
from src.controller.manager_cycles.cycles_funcionais.furacaof_manager import FuracaoF_Manager
from src.controller.manager_cycles.cycles_funcionais.canaisf_manager import CanaisF_Manager

class ButtonHandler:

    def __init__(self, master):

        self.master = master
        self.assents = Assents(self.master)
        self.utils_cmds = Utils(self.master)
        
        self.comandos = {
            "! compile -c: faceamento (p)": self.call_faceamentop,
            "! compile -c: desbaste (p)": self.call_desbastep,
            "! compile -c: furação (p)": self.call_furacaop,
            "! compile -c: canais (p)": self.call_canaisp,
            "! compile -c: faceamento (f)": self.call_faceamentof,
            "! compile -c: desbaste (f)": self.call_desbastef,
            "! compile -c: furação (f)": self.call_furacaof,
            "! compile -c: canais (f)": self.call_canaisf
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

    def call_faceamentop(self):

        self.utils_cmds.limpar_tela()
        self.__faceamentop = FaceamentoP_Manager(self.master)

    def call_desbastep(self):

        self.utils_cmds.limpar_tela()
        self.__desbastep = DesbasteP_Manager(self.master)

    def call_furacaop(self):

        self.utils_cmds.limpar_tela()
        self.__furacaop = FuracaoP_Manager(self.master)

    def call_canaisp(self):

        self.utils_cmds.limpar_tela()
        self.__canaisp = CanaisP_Manager(self.master)

    # SEÇÃO DE MÉTODOS DE CICLOS FUNCIONAIs

    def call_faceamentof(self):

        self.utils_cmds.limpar_tela()
        self.__faceamentof = FaceamentoF_Manager(self.master)

    def call_desbastef(self):

        self.utils_cmds.limpar_tela()
        self.__desbastef = DesbasteF_Manager(self.master)

    def call_furacaof(self):
        self.utils_cmds.limpar_tela()
        self.__furacaof = FuracaoF_Manager(self.master)

    def call_canaisf(self):

        self.utils_cmds.limpar_tela()
        self.__canaisf = CanaisF_Manager(self.master)

    # SEÇÃO DE MÉTODOS UTILs

    def list(self):
        
        self.utils_cmds.limpar_tela()
        self.utils_cmds.list_comands()

    def list_cycles(self):

        self.utils_cmds.limpar_tela()
        self.utils_cmds.list_cycles()