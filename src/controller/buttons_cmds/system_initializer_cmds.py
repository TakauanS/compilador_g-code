from tkinter import messagebox

class SystemInitializerCmds:

    def __init__(self, master):
        self.__master = master

    # Método responsável por chamar a tela de setup manager
    def call_setup(self):
        try:
            from src.view.view_setup_manager import SetupManager

            self.__master.destroy()
            self.setup = SetupManager()
            self.setup.mainloop()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na chamada da tela de setup de configurações do usuário:\n\n{e}')
            raise ValueError(f'Erro na chamada da tela de setup de configurações do usuário: {e}')
        
    # Método responsável por fechar a tela system initializer
    def quit_system(self):
        try:
            self.__master.destroy()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de fechar a tela de inicialização:\n\n{e}')
            raise ValueError(f'Erro no momento de fechar a tela de inicialização: {e}')