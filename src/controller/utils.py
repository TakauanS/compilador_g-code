from src.model.assents import Assents

class Utils:

    def __init__(self, master):
        
        self.master = master
        self.assents = Assents(master=self.master)

    def limpar_tela(self):

        lista_widgets = self.master.winfo_children()

        for widget in lista_widgets:
            widget.place_forget()

    def list_comands(self):

        self.assents.criar_texbox(width=840, height=380, x=10, y=10)