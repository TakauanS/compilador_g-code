from tkinter import messagebox

class MainScreenCmds:

    def __init__(self, master):
        
        self.__master = master

    # Método responsável por chamar a tela de ciclos
    def call_maincycles(self):
        try:
            from src.view.view_cycles.view_main_cycles import ViewMainCycles  

            self.clean_screen()
            self.main_cycles = ViewMainCycles(self.__master)

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Ocorreu um erro ao chamar a tela de ciclos de usinagem:\n\n{e}')
            print(f'Erro: {e}')

    # Método responsável por limpar a tela principal
    def clean_screen(self):
        try:
            self.__lista_widgets = self.__master.fra_main.winfo_children()

            for widget in self.__lista_widgets:
                widget.place_forget()
        
        except Exception as e:
            raise ValueError(f'Erro no momento de limpar a tela principal: {e}')