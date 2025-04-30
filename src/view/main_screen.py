import customtkinter as ctk
from src.model.assents import Assents

class MainScreen(ctk.CTk):

    cor1 = '#F2F1F0' # Cor branca de FG-COLOR
    cor2 = '#EBE8E8' # Cor branca de FG-COLOR (mais puxado para o cinza)

    def __init__(self):
        super().__init__()

        self.__assents = Assents(self)

        self.geometry('900x500')
        self.title('Compilador G-Code')
        self.config(bg=MainScreen.cor1)
        self.resizable(False, False)
        self.iconbitmap('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/favicon.ico')

        # SEÇÃO DE FRAMEs

        self.fra_menu = ctk.CTkFrame(self, border_width=1, width=900, height=60, corner_radius=0, fg_color=MainScreen.cor1)
        self.fra_menu.place(x=0, y=0)
        
        self.fra_rodp = ctk.CTkFrame(self, border_width=1, width=902, height=25, corner_radius=0, fg_color=MainScreen.cor1)
        self.fra_rodp.place(x=-1, y=477)

        self.fra_main = ctk.CTkFrame(self, border_width=1, width=890, height=407, corner_radius=0, fg_color=MainScreen.cor1)
        self.fra_main.place(x=5, y=65)

        # SEÇÃO DE BUTTONs

        self.button_configs = ctk.CTkButton(self.fra_menu,
                                   text='', 
                                   width=34, 
                                   height=34,
                                   compound='top', 
                                   corner_radius=8, 
                                   fg_color=MainScreen.cor1,
                                   hover_color=MainScreen.cor1,
                                   image=self.__assents.img_conf)
        self.button_configs.place(x=15, y=3)

        self.button_ferrame = ctk.CTkButton(self.fra_menu,
                                   text='', 
                                   width=34, 
                                   height=34,
                                   compound='top', 
                                   corner_radius=8, 
                                   fg_color=MainScreen.cor1,
                                   hover_color=MainScreen.cor1,
                                   image=self.__assents.img_ferr)
        self.button_ferrame.place(x=92, y=5)

        self.button_advances = ctk.CTkButton(self.fra_menu,
                                   text='', 
                                   width=34, 
                                   height=34,
                                   compound='top', 
                                   corner_radius=8, 
                                   fg_color=MainScreen.cor1,
                                   hover_color=MainScreen.cor1,
                                   image=self.__assents.img_adva)
        self.button_advances.place(x=168, y=3)

        self.button_cycles = ctk.CTkButton(self.fra_menu,
                                   text='', 
                                   width=34, 
                                   height=34,
                                   compound='top', 
                                   corner_radius=8, 
                                   fg_color=MainScreen.cor1,
                                   hover_color=MainScreen.cor1,
                                   image=self.__assents.img_cycl)
        self.button_cycles.place(x=243, y=3)

        self.button_help = ctk.CTkButton(self.fra_menu,
                                   text='', 
                                   width=34, 
                                   height=34,
                                   compound='top', 
                                   corner_radius=8, 
                                   fg_color=MainScreen.cor1,
                                   hover_color=MainScreen.cor1,
                                   image=self.__assents.img_help)
        self.button_help.place(x=307, y=5)

        # SEÇÃO DE LABELs

        self.label_conf = self.__assents.criar_label('CONFIGS', 12, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)
        self.label_tool = self.__assents.criar_label('TOOLS', 90, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)

        self.label_adva = self.__assents.criar_label('ADVANCES', 160, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)
        self.label_cycl = self.__assents.criar_label('CYCLES', 245, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)

        self.label_help = self.__assents.criar_label('HELP', 316, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)

        # SEÇÃO DE LINHAs

        self.linha1 = self.__assents.criar_linha(66, 7, self.fra_menu)
        self.linha2 = self.__assents.criar_linha(135, 7, self.fra_menu)

        self.linha3 = self.__assents.criar_linha(220, 7, self.fra_menu)
        self.linha4 = self.__assents.criar_linha(290, 7, self.fra_menu)

        self.linha5 = self.__assents.criar_linha(346, 7, self.fra_menu)