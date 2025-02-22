from PIL import Image
import customtkinter as ctk
from src.model.assents import Assents
from src.controller.events import ButtonHandler

class Interface(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.assents = Assents(master=self)

        self.geometry('900x500')
        self.title('Compilador G-Code')
        self.config(bg=self.assents.cor1)
        self.resizable(width=False, height=False)
        self.iconbitmap('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/favicon.ico')

        # SEÇÃO DE DEFs

        def on_button():
            
            comando = entry_command.get()
            button_action.executar_comando(comando=comando)

        # SEÇÃO DE FRAMES

        frame_p = ctk.CTkFrame(master=self, corner_radius=15, width=860, height=400, bg_color=self.assents.cor1, fg_color=self.assents.cor2)
        frame_p.place(x=20, y=80)

        # SEÇÃO DE ENTRYs

        entry_command = ctk.CTkEntry(master=self, width=700, height=35, corner_radius=12, font=('Corbel', 18), bg_color=self.assents.cor1, fg_color=self.assents.cor2, text_color=self.assents.cor6, border_color=self.assents.cor1, placeholder_text_color=self.assents.cor3, placeholder_text='Insira o comando que deseja...')
        entry_command.place(x=20, y=20)

        # SEÇÃO DE BUTTONs

        button_action = ButtonHandler(master=frame_p)

        button_pesq = ctk.CTkButton(master=self, image=self.assents.img_cima, text='UP', font=('Arial', 15, 'bold'), height=35, corner_radius=12, command=on_button, bg_color=self.assents.cor1, fg_color=self.assents.cor4, hover_color=self.assents.cor5)
        button_pesq.place(x=735, y=20)