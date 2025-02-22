from PIL import Image
import customtkinter as ctk

class Assents:

    cor1 = '#1C1A1B' # Cor preta para bg_color - Mais Forte
    cor2 = '#333031' # Cor preta para fg_color - Mais fraca
    cor3 = '#737277' # Cor cinza para placeholder
    cor4 = '#2E53F2' # Cor azul para butões - fg color
    cor5 = '#3757A0' # Cor azul para botões - hover color
    cor6 = 'white'   # Cor branca para textos
    cor7 = '#FAEFEB' # Cor branca para input dialog

    img_cima = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/seta_cima.png'), size=(20, 20))
    img_linha = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha.png'), size=(825, 20))
    img_code = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/code.png'), size=(24, 24))

    def __init__(self, master):

        self.master = master

    def criar_label(self, text, x, y):

        self.label = ctk.CTkLabel(master=self.master, text=text, font=('Corbel', 23), text_color='white')
        self.label.place(x=x, y=y)

    def criar_entry(self, x, y):

        self.entry = ctk.CTkEntry(master=self.master, corner_radius=12, width=200, font=('Consola', 16))
        self.entry.place(x=x, y=y)

        return self.entry

    def criar_linha(self, x, y):

        self.linha = ctk.CTkLabel(master=self.master, text='ㅤ', image=Assents.img_linha)
        self.linha.place(x=x, y=y)

    def criar_textbox(self, text):

        self.textbox = ctk.CTkTextbox(master=self.master, 
                                                width=840, 
                                                    height=380,
                                                        corner_radius=12,
                                                            font=('Consolas', 18),
                                                                text_color=Assents.cor6,  
                                                                    bg_color=Assents.cor2, 
                                                                        fg_color=Assents.cor2, 
                                                                            activate_scrollbars=True)
        
        self.textbox.place(x=10, y=10)

        self.textbox.insert(index='1.0', text=text)
        self.textbox.configure(state='disabled')

    def criar_inputdialog(self, title, text):

        self.input_dialog = ctk.CTkInputDialog(text=text,
                                                    title=title,
                                                        fg_color=Assents.cor7,
                                                            button_fg_color=Assents.cor4,
                                                                button_hover_color=Assents.cor5)
        return self.input_dialog

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