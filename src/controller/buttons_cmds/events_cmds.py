from tkinter import messagebox

from src.view.view_cycles.cy_parametrizados.view_cy_desbastep import ViewCyDesbasteP

class EventsCmds:

    def __init__(self, master):
        self.__master = master

        self.__dic_cycles = {
            '! compile -c: desbaste (p)': self.call_desbastep
        }

        self.__dic_utils = {
            '! compile -parameters': self.call_parameters
        }

    # Método responsável por chamar os comandos dentro do entry
    def call_commands(self):
        try:
            self.__command_atual = self.__master.entry_cmd.get() # Retorna o comando atual no entry de comandos
        
            if self.__command_atual in self.__dic_cycles:
                self.__dic_cycles[self.__command_atual]()

            elif self.__command_atual in self.__dic_utils:
                self.__dic_utils[self.__command_atual]()
            else:
                messagebox.showerror('Compilador G-Code', f'O comando que você inseriu não existe ou está incorreto: {self.__command_atual}')
                return
        except Exception as e:
            raise ValueError(f'Erro no momento de chamar o comando: {e}')
        
    # Método responsável por limpar as telas
    def clean_screen(self):
        try:
            self.__lista_widgets = self.__master.fra_main.winfo_children()

            for widget in self.__lista_widgets:
                widget.place_forget()
        
        except Exception as e:
            raise ValueError(f'Erro no momento de limpar a tela: {e}')

    # Método responsável por chamar a tela de parâmetros de corte
    def call_parameters(self):
        try:
            from src.view.view_parameters import ViewParameters
            self.parameters = ViewParameters()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de chamar a tela de parâmetros de corte:\n\n{e}')
            raise ValueError(f'Erro no momento de chamar a tela de parâmetros de corte: {e}')

    # Método responsável por chamar o ciclo de desbaste parametrizado
    def call_desbastep(self):
        try:
            self.clean_screen()
            self._desbast = ViewCyDesbasteP(self.__master)
            self._desbast.mainloop()
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de chamar a tela de ciclo de desbaste parametrizado:\n\n{e}')
            raise ValueError(f'Erro no momento de chamar a tela de ciclo de desbaste parametrizado: {e}')