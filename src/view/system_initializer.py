from PIL import Image
import customtkinter as ctk
from src.model.assents import Assents
from src.view.setup_manager import SetupManager

class System_Initializer(ctk.CTk):

    cor1 = '#FCF6F2' # Cor cinza de FG-COLOR

    img_ban = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/banner.png'), size=(320, 550)) # Imagem de banner lateral

    def __init__(self):
        super().__init__()

        self.assents = Assents(self)

        self.title('Compilador G-Code | Inicialização')
        self.geometry('900x500')
        self.resizable(False, False)
        self.config(bg=System_Initializer.cor1)
        self.iconbitmap('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/favicon.ico')

        # Método responsável por sair do software
        def quit_seup():
            self.destroy()

        # Método responsável por chamar a tela de setup manager
        def call_setup():

            self.destroy()
            self.setup = SetupManager()
            self.setup.mainloop()

        # SEÇÃO DE FRAMEs
        self.frame_later = ctk.CTkFrame(self, border_width=1, width=320, height=550, corner_radius=0)
        self.frame_later.place(x=0, y=0)

        self.frame_rodap = ctk.CTkFrame(self, fg_color=System_Initializer.cor1, border_width=1, width=900, height=40, corner_radius=0)
        self.frame_rodap.place(x=0, y=460)

        # SEÇÃO DE BUTTONs
        self.but_avancar = ctk.CTkButton(self.frame_rodap, text='AVANÇAR', command=call_setup, font=('Arial', 14, 'bold'), fg_color=self.assents.cor4, hover_color=self.assents.cor5, width=100, corner_radius=5)
        self.but_avancar.place(x=790, y=6)

        self.but_cancelar = ctk.CTkButton(self.frame_rodap, width=100, text='CANCELAR', command=quit_seup, font=('Arial', 14, 'bold'), fg_color=self.assents.cor4, hover_color=self.assents.cor5, corner_radius=5)
        self.but_cancelar.place(x=680, y=6)

        # SEÇÃO DE LABELs
        self.label_img = ctk.CTkLabel(self.frame_later, text='', image=System_Initializer.img_ban) # Label que exibe a imagem do banner na lateral
        self.label_img.place(x=0, y=0)

        self.label_title = self.assents.criar_label('Bem-Vindo ao Compilador G-Code', 340, 15, text_color='black', font=('Corbel', 26, 'bold'))
        self.label_title2 = self.assents.criar_label('Seja muito bem-vindo ao seu novo ambiente de programação CNC!', 340, 55, text_color='black', font=('Corbel', 18, 'normal')) 

        self.label_trecho1 = self.assents.criar_label('O Compilador G-code era de foi desenvolvido para tornar o seu trabalho', 340, 95, text_color='black', font=('Corbel', 18, 'normal'))

        self.label_trecho2 = self.assents.criar_label('mais rápido, preciso e eficiente.', 340, 120, text_color='black', font=('Corbel', 18))
        self.label_trecho3 = self.assents.criar_label('Aqui, você pode escrever, compilar e simular comandos G-code com total', 340, 155, text_color='black', font=('Corbel', 18))
        
        self.label_trecho4 = self.assents.criar_label('controle sobre seus projetos.', 340, 180, text_color='black', font=('Corbel', 18))    
        self.label_trecho5 = self.assents.criar_label('💡 Recursos principais:', 340, 220, text_color='black', font=('Corbel', 18))  
              
        self.label_trecho6 = self.assents.criar_label('• Interface intuitiva.', 340, 260, text_color='black', font=('Corbel', 18))        
        self.label_trecho7 = self.assents.criar_label('• Suporte a múltiplas máquinas CNC.', 340, 310, text_color='black', font=('Corbel', 18))        
         
        self.label_trecho8 = self.assents.criar_label('• Geração otimizada de trajetórias.', 340, 285, text_color='black', font=('Corbel', 18))        
        self.label_trecho9 = self.assents.criar_label('Vamos começar a programar?', 340, 360, text_color='black', font=('Corbel', 22, 'bold'))