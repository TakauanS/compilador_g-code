from tkinter import messagebox

class MainScreenCmds:

    def __init__(self, master):
        
        self.__master = master

    # Método responsável por chamar a tela de ciclos
    def call_maincycles(self):
        try:
            from src.view.view_cycles.main_cycles import MainCycles  
               
            self.main_cycles = MainCycles(self.__master)
            self.main_cycles.mainloop()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Ocorreu um erro ao chamar a tela de ciclos de usinagem:\n\n{e}')
            print(f'Erro: {e}')