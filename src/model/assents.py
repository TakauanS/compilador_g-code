from PIL import Image
import customtkinter as ctk
from tkinter import LabelFrame

class Assents:

    cor1 = '#1C1A1B' # Cor preta para bg_color - Mais Forte
    cor2 = '#333031' # Cor preta para fg_color - Mais fraca
    cor3 = '#737277' # Cor cinza para placeholder
    cor4 = '#1A8AE5' # Cor azul para butões - fg color     
    cor5 = '#3757A0' # Cor azul para botões - hover color
    cor6 = 'white'   # Cor branca para textos
    cor7 = '#FAEFEB' # Cor branca para input dialog

    img_up = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/upload.png'), size=(24, 24))
    img_help = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/ajuda.png'), size=(28, 28))
    img_pasta = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/pasta.png'), size=(24, 24))
    img_cycl = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/cycles.png'), size=(34, 32))
    img_conf = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/configs.png'), size=(30, 30))
    img_linv = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_v.png'), size=(25, 46))
    img_adva = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/advance.png'), size=(36, 36))
    img_bann = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/banner.png'), size=(320, 550))
    img_ferr = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/ferramentas.png'), size=(30, 30))    

    def __init__(self, master):

        self.master = master

    def criar_label(self, text, x, y, height=0, bg_color='#FCF6F2', fg_color='#FCF6F2', text_color='white', font=('Corbel', 20, 'normal'), frame=None):

        if frame is None:
            frame = self.master
        
        self.label = ctk.CTkLabel(master=frame, height=height, text=text, font=font, fg_color=fg_color, text_color=text_color, bg_color=bg_color)
        self.label.place(x=x, y=y)

    def criar_labelframe(self, x, y, width, height, text, bg='#FCF6F2', frame=None):

        if frame is None: 
            frame = self.master

        self.labelframe = LabelFrame(master=frame, width=width, height=height, text=text, font=('Corbel', 13), bg=bg)
        self.labelframe.place(x=x, y=y)

        return self.labelframe

    def criar_entry(self, x, y, width=200, border_width=2, frame=None):

        if frame is None:
            frame = self.master

        self.entry = ctk.CTkEntry(master=frame, corner_radius=10, width=width, border_width=border_width, justify='center', bg_color='#fcf6f2', font=('Consola', 16))
        self.entry.place(x=x, y=y)    

        return self.entry

    def criar_linha(self, x, y, frame=None):

        if frame is None:
            frame = self.master

        self.linha = ctk.CTkLabel(master=frame, width=10, text='', image=Assents.img_linv)
        self.linha.place(x=x, y=y)

    def criar_textbox(self, text):

        self.textbox = ctk.CTkTextbox(self.master, 
                                                width=840, 
                                                height=380,
                                                corner_radius=12,
                                                bg_color=Assents.cor2,
                                                fg_color=Assents.cor2, 
                                                font=('Consolas', 18),
                                                text_color=Assents.cor6,                                                 
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
    
    def criar_combobox(self, x, y, frame=None, width=200, corner_radius=10, values=(), justify='center'):

        if frame is None:
            frame = self.master

        self.combobox = ctk.CTkComboBox(frame, 
                                width=width,
                                values=values, 
                                border_width=1,
                                justify=justify,
                                state='readonly',
                                bg_color='#fcf6f2',
                                font=('Arial', 14),
                                button_color=Assents.cor4,
                                corner_radius=corner_radius,
                                button_hover_color=Assents.cor5)
        self.combobox.place(x=x, y=y)
        return self.combobox

    def criar_radionbutton(self, x, y, text, value, variable, width=100, frame=None):

        if frame is None:
            frame = self.master

        self.radiobutton = ctk.CTkRadioButton(frame,
                                             width=width, 
                                             text=text,
                                             value=value,  
                                             variable=variable,
                                             bg_color='#fcf6f2', 
                                             border_width_unchecked=1)                                     
        self.radiobutton.place(x=x, y=y)