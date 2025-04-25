import customtkinter as ctk
from src.model.assents import Assents
from src.controller.events.events_main import ButtonHandler

class MainScreen(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.__assents = Assents(self)

        self.geometry('900x500')
        self.title('Compilador G-Code')
        self.config(bg=self.__assents.cor1)
        self.resizable(False, False)
        self.iconbitmap('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/favicon.ico')

        # SEÇÃO DE DEFs

        def on_button():
            
            comando = entry_command.get()
            button_action.executar_comando(comando)

        # SEÇÃO DE FRAMES

        frame_p = ctk.CTkFrame(self, corner_radius=15, width=860, height=400, bg_color=self.__assents.cor1, fg_color=self.__assents.cor2)
        frame_p.place(x=20, y=80)

        # SEÇÃO DE ENTRYs

        entry_command = ctk.CTkEntry(self, width=700, height=35, corner_radius=12, font=('Corbel', 18), bg_color=self.__assents.cor1, fg_color=self.__assents.cor2, text_color=self.__assents.cor6, border_color=self.__assents.cor1, placeholder_text_color=self.__assents.cor3, placeholder_text='Insira o comando que deseja...')
        entry_command.place(x=20, y=20)

        # SEÇÃO DE BUTTONs

        button_action = ButtonHandler(frame_p)

        button_pesq = ctk.CTkButton(self, image=self.__assents.img_cima, text='UP', font=('Arial', 15, 'bold'), height=35, corner_radius=12, command=on_button, bg_color=self.__assents.cor1, fg_color=self.__assents.cor4, hover_color=self.__assents.cor5)
        button_pesq.place(x=735, y=20)