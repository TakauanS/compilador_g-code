from tkinter import messagebox

from src.controller.buttons_cmds.events_cmds import EventsCmds
from src.view.view_cycles.cy_parametrizados.view_cy_desbastep import ViewCyDesbasteP

class MainCyclesCmds:

    def __init__(self, master):
        self.__master = master
        self.__events = EventsCmds(self.__master)

    # Método responsável por fazer a chamada do ciclo de desbaste parametrizado
    def call_desbastep(self):
        try:
            self.__events.clean_screen()
            self.__desbastep = ViewCyDesbasteP(self.__master)
            self.__desbastep.mainloop()
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na abertura da tela de ciclo de desbaste parametrizado:\n\n{e}')
            print(f'Erro: {e}')