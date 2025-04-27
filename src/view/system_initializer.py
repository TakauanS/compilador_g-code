import customtkinter as ctk
from src.model.assents import Assents
from src.view.setup_manager import SetupManager

class System_Initializer(ctk.CTk):

    teste_color = '#f2f1f0'
    teste = '#E5E5E5'

    def __init__(self):
        super().__init__()

        self.assents = Assents(self)

        self.title('Instalação do Compilador G-Code 1.0')
        self.geometry('900x500')
        self.resizable(False, False)
        self.config(bg=System_Initializer.teste_color)

        # SEÇÃO DE COMMANDs DOS BUTTONs

        def quit():
            self.quit()

        def call_setup():

            quit()
            self.setup = SetupManager()
            self.setup.mainloop()

        # SEÇÃO DE FRAMEs

        self.frame_later = ctk.CTkFrame(self, border_width=1, width=320, height=550, corner_radius=0)
        self.frame_later.place(x=0, y=0)

        self.frame_rodap = ctk.CTkFrame(self, fg_color=System_Initializer.teste, border_width=1, width=900, height=40, corner_radius=0)
        self.frame_rodap.place(x=0, y=460)

        # SEÇÃO DE BUTTONs

        self.but_avancar = ctk.CTkButton(self.frame_rodap, command=call_setup, fg_color='#3294E3', width=100, corner_radius=5, text='AVANÇAR', font=('Arial', 14, 'bold'))
        self.but_avancar.place(x=790, y=6)

        self.but_cancelar = ctk.CTkButton(self.frame_rodap, command=quit, fg_color='#3294E3', width=100, corner_radius=5, text='CANCELAR', font=('Arial', 14, 'bold'))
        self.but_cancelar.place(x=680, y=6)

        # SEÇÃO DE LABELs

        self.label_img = ctk.CTkLabel(self.frame_later, text='', image=self.assents.img_ban)
        self.label_img.place(x=0, y=0)

        self.label_title = ctk.CTkLabel(self, 
                                        fg_color=System_Initializer.teste_color, 
                                        text='Bem-Vindo ao Compilador G-Code', 
                                        font=('Corbel', 26, 'bold')).place(x=340, y=15)
        
        self.label_title2 = ctk.CTkLabel(self, fg_color=System_Initializer.teste_color, 
                                         text='Seja muito bem-vindo ao seu novo ambiente de programação CNC!', 
                                         font=('Corbel', 18)).place(x=340, y=55)

        self.label_trecho1 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text=f'O Compilador G-code era de foi desenvolvido para tornar o seu trabalho', 
                                          font=('Corbel', 18)).place(x=340, y=95)
        
        self.label_trecho2 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='mais rápido, preciso e eficiente.', 
                                          font=('Corbel', 18)).place(x=340, y=120)
        
        self.label_trecho3 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='Aqui, você pode escrever, compilar e simular comandos G-code com total', 
                                          font=('Corbel', 18)).place(x=340, y=155)
        
        self.label_trecho4 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='controle sobre seus projetos.', 
                                          font=('Corbel', 18)).place(x=340, y=180)
        
        self.label_trecho5 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='💡 Recursos principais:', 
                                          font=('Corbel', 18)).place(x=340, y=220)
        
        self.label_trecho6 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='• Interface intuitiva.', 
                                          font=('Corbel', 18)).place(x=340, y=260)
        
        self.label_trecho7 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='• Suporte a múltiplas máquinas CNC.', 
                                          font=('Corbel', 18)).place(x=340, y=285)
    
        self.label_trecho8 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='• Geração otimizada de trajetórias.', 
                                          font=('Corbel', 18)).place(x=340, y=310)
        self.label_trecho9 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='• Geração otimizada de trajetórias.', 
                                          font=('Corbel', 18)).place(x=340, y=310)
        
        self.label_trecho10 = ctk.CTkLabel(self, 
                                          fg_color=System_Initializer.teste_color, 
                                          text='Vamos começar a programar?', 
                                          font=('Corbel', 22, 'bold')).place(x=340, y=360)