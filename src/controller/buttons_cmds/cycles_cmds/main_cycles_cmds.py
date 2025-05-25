from tkinter import messagebox

from src.view.view_cycles.cy_parametrizados.view_cy_desbastep import ViewCyDesbasteP

class MainCyclesCmds:

    def __init__(self, mtr):
        self.__mtr = mtr

    # Método responsável por fazer a chamada do ciclo de desbaste parametrizado
    def call_desbastep(self):
        try:
            self.__desbastep = ViewCyDesbasteP(self.__mtr)
            self.__desbastep.mainloop()
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na abertura da tela de ciclo de desbaste parametrizado:\n\n{e}')
            print(f'Erro: {e}')