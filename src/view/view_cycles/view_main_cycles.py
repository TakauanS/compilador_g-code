from PIL import Image
from customtkinter import CTkImage

from src.model.assents import Assents
from src.controller.buttons_cmds.cycles_cmds.main_cycles_cmds import MainCyclesCmds

class ViewMainCycles:

    cor1 = '#1A8AE5'
    cor2 = '#FFFFFF'
    cor3 = '#000000'

    img_up = CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/up_cycle.png'))
    img_help = CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/ajuda.png'))

    sub = 'Abaixo estão listados todos os ciclos de usinagem disponíveis, prontos para parametrização e uso funcional:'

    def __init__(self, master):

        self.__master = master
        self.__asssents = Assents(self.__master)
        self.__cmds = MainCyclesCmds(self.__master)

        # SEÇÃO DE FRAMEs E LABELFRAMEs
        self.__master.fra_cycl = self.__asssents.criar_frame(5, 70, 295, 880, 8, 1, ViewMainCycles.cor2, ViewMainCycles.cor2, fr=self.__master.fra_main)
        
        self.__master.fra_desb = self.__asssents.criar_labelframe(10, 5, 340, 100, 'Cycles de Desbaste', ViewMainCycles.cor2, self.__master.fra_cycl)
        self.__master.fra_fura = self.__asssents.criar_labelframe(10, 120, 340, 100, 'Cycles de Furação', ViewMainCycles.cor2, self.__master.fra_cycl)
        self.__master.fra_face = self.__asssents.criar_labelframe(530, 5, 340, 100, 'Cycles de Faceamento', ViewMainCycles.cor2, self.__master.fra_cycl)
        self.__master.fra_cana = self.__asssents.criar_labelframe(530, 120, 340, 100, 'Cycles de Canal', ViewMainCycles.cor2, self.__master.fra_cycl)

        # SEÇÃO DE LABELs
        self.__master.label_title = self.__asssents.criar_label('Ciclos de Usinagem | Parametrizados - Funcionais', 10, 5, text_color=ViewMainCycles.cor1, font=('Corbel', 22, 'bold'), frame=self.__master.fra_main)
        self.__master.label_sub = self.__asssents.criar_label(ViewMainCycles.sub, 10, 35, text_color=ViewMainCycles.cor3, font=('Corbel', 18, 'normal'), frame=self.__master.fra_main)

        self.__master.label_desbp = self.__asssents.criar_label('Desbaste Parametrizado:', 10, 5, text_color=ViewMainCycles.cor3, frame=self.__master.fra_desb)
        self.__master.label_desbf = self.__asssents.criar_label('Desbaste Funcional:', 10, 40, text_color=ViewMainCycles.cor3, frame=self.__master.fra_desb)

        self.__master.label_furap = self.__asssents.criar_label('Furação Parametrizado:', 10, 5, text_color=ViewMainCycles.cor3, frame=self.__master.fra_fura)
        self.__master.label_furaf = self.__asssents.criar_label('Furação Funcional:', 10, 40, text_color=ViewMainCycles.cor3, frame=self.__master.fra_fura)

        self.__master.label_facep = self.__asssents.criar_label('Faceamento Parametrizado:', 10, 5, text_color=ViewMainCycles.cor3, frame=self.__master.fra_face)
        self.__master.label_facef = self.__asssents.criar_label('Faceamento Funcional:', 10, 40, text_color=ViewMainCycles.cor3, frame=self.__master.fra_face)

        self.__master.label_canap = self.__asssents.criar_label('Canal Parametrizado:', 10, 5, text_color=ViewMainCycles.cor3, frame=self.__master.fra_cana)
        self.__master.label_canaf = self.__asssents.criar_label('Canal Funcional:', 10, 40, text_color=ViewMainCycles.cor3, frame=self.__master.fra_cana)

        # SEÇÃO DE ENTRYs

        # SEÇÃO DE BUTTONs
        self.__master.but_help_desb = self.__asssents.criar_button(305, -8, 0, 0, '', 'teste', ViewMainCycles.img_help, ViewMainCycles.cor2, ViewMainCycles.cor2, ViewMainCycles.cor2, ti='HELP', fr=self.__master.fra_desb)
        self.__master.but_help_fura = self.__asssents.criar_button(305, -8, 0, 0, '', 'teste', ViewMainCycles.img_help, ViewMainCycles.cor2, ViewMainCycles.cor2, ViewMainCycles.cor2, ti='HELP', fr=self.__master.fra_fura)
        self.__master.but_help_face = self.__asssents.criar_button(305, -8, 0, 0, '', 'teste', ViewMainCycles.img_help, ViewMainCycles.cor2, ViewMainCycles.cor2, ViewMainCycles.cor2, ti='HELP', fr=self.__master.fra_face)
        self.__master.but_help_cana = self.__asssents.criar_button(305, -8, 0, 0, '', 'teste', ViewMainCycles.img_help, ViewMainCycles.cor2, ViewMainCycles.cor2, ViewMainCycles.cor2, ti='HELP', fr=self.__master.fra_cana)

        self.__master.but_desbp = self.__asssents.criar_button(225, 5, 0, 0, '', self.__cmds.call_desbastep, 
                                                               ViewMainCycles.img_up, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, ti='UP - DESBASTE PARAMETRIZADO', fr=self.__master.fra_desb)
        
        self.__master.but_desbf = self.__asssents.criar_button(185, 40, 0, 0, '', 'teste', 
                                                               ViewMainCycles.img_up, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, ti='UP - DESBASTE FUNCIONAL', fr=self.__master.fra_desb)
        
        self.__master.but_furap = self.__asssents.criar_button(215, 5, 0, 0, '', 'teste', 
                                                               ViewMainCycles.img_up, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, ti='UP - FURAÇÃO PARAMETRIZADO', fr=self.__master.fra_fura)
        
        self.__master.but_furaf = self.__asssents.criar_button(175, 40, 0, 0, '', 'teste', 
                                                               ViewMainCycles.img_up, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, ti='UP - FURAÇÃO FUNCIONAL', fr=self.__master.fra_fura)
        
        self.__master.but_facep = self.__asssents.criar_button(255, 5, 0, 0, '', 'teste', 
                                                               ViewMainCycles.img_up, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, ti='UP - FACEAMENTO PARAMETRIZADO', fr=self.__master.fra_face)
        
        self.__master.but_facef = self.__asssents.criar_button(210, 40, 0, 0, '', 'teste', 
                                                               ViewMainCycles.img_up, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, ti='UP - FACEAMENTO FUNCIONAL', fr=self.__master.fra_face)
        
        self.__master.but_canap = self.__asssents.criar_button(195, 5, 0, 0, '', 'teste', 
                                                               ViewMainCycles.img_up, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, ti='UP - CANAL PARAMETRIZADO', fr=self.__master.fra_cana)
        
        self.__master.but_canaf = self.__asssents.criar_button(155, 40, 0, 0, '', 'teste', 
                                                               ViewMainCycles.img_up, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, 
                                                               ViewMainCycles.cor2, ti='UP - CANAL FUNCIONAL', fr=self.__master.fra_cana)