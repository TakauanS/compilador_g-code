from tkinter import messagebox

from src.view.view_cycles.cy_parametrizados.view_cy_desbastep import ViewCyDesbasteP

class EventsCmds:

    def __init__(self, master):
        self.__master = master

        self.__dic_cycles = {
            '! compile -c: desbaste (p)': self.call_desbastep
        }

    # Método responsável por limpar as telas
    def clean_screen(self):
        try:
            self.__lista_widgets = self.__master.fra_main.winfo_children()

            for widget in self.__lista_widgets:
                widget.place_forget()
        
        except Exception as e:
            raise ValueError(f'Erro no momento de limpar a tela: {e}')

    # Método responsável por chamar os ciclos de usinagem
    def call_cycles(self):
        try:
            self.__cycle_atual = self.__master.entry_cmd.get() # Retorna o comando atual no entry de comandos
        
            if self.__cycle_atual not in self.__dic_cycles.keys():
                messagebox.showerror('Compilador G-Code', f'O comando que você inseriu não existe ou está incorreto: {self.__cycle_atual}')
                return
            else:
                self.__dic_cycles[self.__cycle_atual]()

        except Exception as e:
            raise ValueError(f'Erro no momento de chamar o comando: {e}')
        
    # Método responsável por chamar o ciclo de desbaste parametrizado
    def call_desbastep(self):
        
        self.clean_screen()
        self._desbast = ViewCyDesbasteP(self.__master)
        self._desbast.mainloop()