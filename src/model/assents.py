from PIL import Image
import customtkinter as ctk
import textwrap

class Assents:

    cor1 = '#1C1A1B' # Cor preta para bg_color - Mais Forte
    cor2 = '#333031' # Cor preta para fg_color - Mais fraca
    cor3 = '#737277' # Cor cinza para placeholder
    cor4 = '#2E53F2' # Cor azul para butões
    cor5 = '#3757A0' # Cor azul para botões - hover color
    cor6 = 'white'   # Cor branca para textos

    text_list = textwrap.dedent('''• CICLOS DE USINAGEM:
                                
- ! compile -c: faceamento > Ciclo de faceamento parametrizado.
- ! compile -c: desbaste > Ciclo de desbaste parametrizado.
- ! compile -c: canais > Ciclo de canais parametrizado.
                                
- ! compile -c: faceamento (f) > Ciclo de faceamento funcional.
- ! compile -c: desbaste (f) > Ciclo de desbaste funcional.
- ! compile -c: canais (f) > Ciclo de canais funcional.
                                
• VISUALIZAÇÃO DE COMANDOS
                                
- ! compile -list > Lista todos os comandos disponiveis no sistema.
- ! compile -list: cycles > Lista apenas os comandos de ciclo de usinagem.
- ! compile -list: pos > Lista apenas os valores de posicionamentos de segurança.
                                ''')

    def __init__(self, master):

        self.master = master

    def criar_label(self, text, x, y):

        self.label = ctk.CTkLabel(master=self.master, text=text, font=('Corbel', 23), text_color='white')
        self.label.place(x=x, y=y)

    def criar_entry(self, x, y):

        self.entry = ctk.CTkEntry(master=self.master, corner_radius=12, width=200, font=('Consola', 16))
        self.entry.place(x=x, y=y)

        return self.entry

    def criar_texbox(self, width, height, x, y):

        self.texbox = ctk.CTkTextbox(master=self.master, 
                                                width=width, 
                                                    height=height,
                                                        corner_radius=12,
                                                            font=('Consolas', 18),
                                                                text_color=Assents.cor6,  
                                                                    bg_color=Assents.cor2, 
                                                                        fg_color=Assents.cor2, 
                                                                            activate_scrollbars=True)
        
        self.texbox.place(x=x, y=y)

        self.texbox.insert(index='1.0', text=Assents.text_list)
        self.texbox.configure(state='disabled')

    def criar_button(self, text, command, image, x, y):

        self.button = ctk.CTkButton(master=self.master,
                                    height=35,
                                        text=text,
                                        image=image, 
                                            command=command, 
                                                corner_radius=12,   
                                                    bg_color=Assents.cor2, 
                                                        fg_color=Assents.cor4, 
                                                            hover_color=Assents.cor5,
                                                                font=('Arial', 15, 'bold'))
        self.button.place(x=x, y=y)
        return self.button