from PIL import Image
import customtkinter as ctk

from src.model.assents import Assents
from src.model.json_handler import JsonHandler
from src.controller.buttons_cmds.events_cmds import EventsCmds
from src.controller.buttons_cmds.main_screen_cmds import MainScreenCmds

class ViewMainScreen(ctk.CTk):

    cor1 = '#FCF6F2' # Cor branca de FG-COLOR
    cor2 = '#EBE8E8' # Cor branca de FG-COLOR (mais puxado para o cinza)
    cor3 = '#242322' # Cor preta de TEXT-COLOR
    cor4 = '#1A8AE5' # Cor azul de FG-COLOR

    img_up = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/upload.png'))

    def __init__(self):
        super().__init__()

        self.__assents = Assents(self)
        self.__even = EventsCmds(self)

        self.__cmds = MainScreenCmds(self)

        self.__json_handler = JsonHandler()
        self.__json_handler.convert_files()

        self.geometry('900x500')
        self.title('Compilador G-Code')
        self.config(bg=ViewMainScreen.cor1)
        self.resizable(False, False)
        self.iconbitmap('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/favicon.ico')

        # SEÇÃO DE FRAMEs
        self.fra_menu = self.__assents.criar_frame(0, 0, 60, 900, 0, 1, ViewMainScreen.cor1, self)
        self.fra_rodp = self.__assents.criar_frame(-1, 477, 25, 902, 0, 1, ViewMainScreen.cor1, self)
        self.fra_main = self.__assents.criar_frame(5, 98, 375, 890, 8, 1, ViewMainScreen.cor1, self)

        # SEÇÃO DE BUTTONs
        self._but_cmd = self.__assents.criar_button(850, 65, 28, 45, '', self.__even.call_cycles,
                                                    ViewMainScreen.img_up,
                                                    ViewMainScreen.cor4,
                                                    ViewMainScreen.cor4,
                                                    ViewMainScreen.cor1,
                                                    10, ti='BUSCAR COMANDO...', fr=self)

        self.but_con = self.__assents.criar_button(15, 3, 34, 34, '', self.__cmds.call_maincycles, 
                                                       self.__assents.img_conf, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1,
                                                       8, 'CONFIGURAÇÕES', 'top', fr=self.fra_menu)
        
        self.but_fer = self.__assents.criar_button(92, 5, 34, 34, '', self.__cmds.call_maincycles, 
                                                       self.__assents.img_ferr, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1,
                                                       8, 'FERRAMENTAS', 'top', fr=self.fra_menu)
        
        self.but_ava = self.__assents.criar_button(168, 3, 34, 34, '', self.__cmds.call_maincycles, 
                                                       self.__assents.img_adva, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1,
                                                       8, 'AVANÇOS', 'top', fr=self.fra_menu)
        
        self.but_cyc = self.__assents.criar_button(243, 3, 34, 34, '', self.__cmds.call_maincycles, 
                                                       self.__assents.img_cycl, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1,
                                                       8, 'CICLOS DE USINAGEM', 'top', fr=self.fra_menu)
        
        self.but_hel = self.__assents.criar_button(307, 5, 34, 34, '', self.__cmds.call_maincycles, 
                                                       self.__assents.img_help, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1, 
                                                       ViewMainScreen.cor1,
                                                       8, 'AJUDA', 'top', fr=self.fra_menu)

        # SEÇÃO DE ENTRYs
        self.entry_cmd = self.__assents.criar_entry(5, 65, 840, 1, 'left', self,)

        # SEÇÃO DE LABELs
        self.label_conf = self.__assents.criar_label('CONFIGS', 12, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)
        self.label_tool = self.__assents.criar_label('TOOLS', 90, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)

        self.label_adva = self.__assents.criar_label('ADVANCES', 160, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)
        self.label_cycl = self.__assents.criar_label('CYCLES', 245, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)

        self.label_help = self.__assents.criar_label('HELP', 316, 40, text_color=self.__assents.cor4, font=('Corbel', 13, 'bold'), frame=self.fra_menu)

        self.label_mode = self.__assents.criar_label(f"model: {self.__json_handler.get_data(self.__json_handler.data_user, 'modelo')}", 5, 4,     
                                                    frame=self.fra_rodp,
                                                    font=('Arial', 13, 'normal'),
                                                    text_color=ViewMainScreen.cor3) 
        # SEÇÃO DE LINHAs
        self.linha1 = self.__assents.criar_linha(66, 7, self.fra_menu)
        self.linha2 = self.__assents.criar_linha(135, 7, self.fra_menu)

        self.linha3 = self.__assents.criar_linha(220, 7, self.fra_menu)
        self.linha4 = self.__assents.criar_linha(290, 7, self.fra_menu)

        self.linha5 = self.__assents.criar_linha(346, 7, self.fra_menu)