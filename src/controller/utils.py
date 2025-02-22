import textwrap
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

        self.text_list = textwrap.dedent('''• CICLOS DE USINAGEM:
                                
- ! compile -c: faceamento > Ciclo de faceamento parametrizado.
- ! compile -c: desbaste > Ciclo de desbaste parametrizado.
- ! compile -c: canais > Ciclo de canais parametrizado.
                                
- ! compile -c: faceamento (f) > Ciclo de faceamento funcional.
- ! compile -c: desbaste (f) > Ciclo de desbaste funcional.
- ! compile -c: canais (f) > Ciclo de canais funcional.
                                
• VISUALIZAÇÃO DE COMANDOS
                                
- ! compile -list > Lista todos os comandos disponiveis no sistema.
- ! compile -list: cycles > Lista apenas os comandos de ciclo de usinagem.
- ! compile -list: pos > Lista apenas os valores de posicionamentos de segurança.''')

        self.assents.criar_textbox(text=self.text_list)

    def list_cycles(self):

        self.text_list_cycles = textwrap.dedent('''• CICLOS DE USINAGEM:
                                
- ! compile -c: faceamento > Ciclo de faceamento parametrizado.
- ! compile -c: desbaste > Ciclo de desbaste parametrizado.
- ! compile -c: canais > Ciclo de canais parametrizado.
                                
- ! compile -c: faceamento (f) > Ciclo de faceamento funcional.
- ! compile -c: desbaste (f) > Ciclo de desbaste funcional.
- ! compile -c: canais (f) > Ciclo de canais funcional.''')

        self.assents.criar_textbox(text=self.text_list_cycles)