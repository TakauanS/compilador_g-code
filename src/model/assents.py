from PIL import Image
import customtkinter as ctk

class Assents:

    cor1 = '#1C1A1B' # Cor preta para bg_color - Mais Forte
    cor2 = '#333031' # Cor preta para fg_color - Mais fraca
    cor3 = '#737277' # Cor cinza para placeholder
    cor4 = '#2E53F2' # Cor azul para butões
    cor5 = '#3757A0' # Cor azul para botões - hover color
    cor6 = 'white'   # Cor branca para textos

    def __init__(self, master):

        self.master = master

    def criar_label(self, text, x, y):

        self.label = ctk.CTkLabel(master=self.master, text=text, font=('Corbel', 23), text_color='white')
        self.label.place(x=x, y=y)

    def criar_entry(self, x, y):

        self.entry = ctk.CTkEntry(master=self.master, corner_radius=12, width=200, font=('Consola', 16))
        self.entry.place(x=x, y=y)

        return self.entry
    
    def criar_button(self, text, command, x, y):

        self.button = ctk.CTkButton(master=self.master,
                                    height=35,
                                        text=text, 
                                            command=command, 
                                                corner_radius=12,   
                                                    bg_color=Assents.cor2, 
                                                        fg_color=Assents.cor4, 
                                                            hover_color=Assents.cor5,
                                                                font=('Arial', 15, 'bold'))
        self.button.place(x=x, y=y)
        return self.button