from PIL import Image
import customtkinter as ctk
from src.controller.events import ButtonHandler

class Interface(ctk.CTk):

    # SEÇÃO DE CORES

    cor1 = '#1C1A1B' # Cor preta para bg_color - Mais Forte
    cor2 = '#333031' # Cor preta para fg_color - Mais fraca
    cor3 = '#737277' # Cor cinza para placeholder
    cor4 = '#2E53F2' # Cor azul para butões
    cor5 = '#3757A0' # Cor azul para botões - hover color
    cor6 = 'white'   # Cor branca para textos

    # SEÇÃO DE EXPORTAÇÃO DE IMAGEs

    img_cima = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/seta_cima.png'), size=(20, 20))

    def __init__(self):
        super().__init__()

        self.geometry('900x500')
        self.title('Compilador G-Code')
        self.config(bg=Interface.cor1)
        self.resizable(width=False, height=False)

        # SEÇÃO DE DEFs

        def on_button():

            comando = entry_command.get()
            button_action.executar_comando(comando=comando)

        # SEÇÃO DE FRAMES

        frame_p = ctk.CTkFrame(master=self, corner_radius=15, width=860, height=400, bg_color=Interface.cor1, fg_color=Interface.cor2)
        frame_p.place(x=20, y=80)

        button_action = ButtonHandler(master=frame_p)

        # SEÇÃO DE ENTRYs

        entry_command = ctk.CTkEntry(master=self, width=700, height=35, corner_radius=12, font=('Corbel', 18), bg_color=Interface.cor1, fg_color=Interface.cor2, text_color=Interface.cor6, border_color=Interface.cor1, placeholder_text_color=Interface.cor3, placeholder_text='Insira o comando que deseja...')
        entry_command.place(x=20, y=20)

        # SEÇÃO DE BUTTONs

        button_pesq = ctk.CTkButton(master=self, image=Interface.img_cima, text='UP', font=('Arial', 15, 'bold'), height=35, corner_radius=12, command=on_button, bg_color=Interface.cor1, fg_color=Interface.cor4, hover_color=Interface.cor5)
        button_pesq.place(x=735, y=20)

if __name__ == "__main__":
    app = Interface()
    app.mainloop