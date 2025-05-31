from tkinter import messagebox

from src.controller.buttons_cmds.events_cmds import EventsCmds

class MainScreenCmds:

    def __init__(self, master):
        self.__master = master
        self.__events = EventsCmds(self.__master)

    # Método responsável por chamar a tela de ciclos
    def call_maincycles(self):
        try:
            from src.view.view_cycles.view_main_cycles import ViewMainCycles  

            self.__events.clean_screen()
            self.main_cycles = ViewMainCycles(self.__master)

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Ocorreu um erro ao chamar a tela de ciclos de usinagem:\n\n{e}')
            print(f'Erro: {e}')

    # Método responsável por chamar a tela de parâmetros de corte
    def call_parameters(self):
        try:
            from src.view.view_parameters import ViewParameters
            self.parameters = ViewParameters()
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de chamar a tela de parâmetros de corte:\n\n{e}')
            raise ValueError(f'Erro no momento de chamar a tela de parâmetros de corte: {e}')