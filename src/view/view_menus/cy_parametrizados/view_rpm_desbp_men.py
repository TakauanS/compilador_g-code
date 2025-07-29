from PIL import Image
import customtkinter as ctk
from tkinter import messagebox

from src.model.assents import Assents
from src.controller.buttons_cmds.cycles_cmds.cy_parametrizados_cmds.cy_desbastep_cmd import DesbastePCmds

class ViewRpmDesbasp_Men(ctk.CTkToplevel):

    cor1 = '#FFFFFF'
    cor2 = '#1A8AE5'
    cor3 = '#3757A0'
    cor4 = '#000000'

    img_up = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/upload.png'), size=(24, 24))
    img_lh = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(408, 24))

    sub = 'Abaixo estão listadas todas as opções de configurações possíveis para as rotações do fuso'

    def __init__(self):
        try:
            super().__init__()

            self.__assents = Assents(self)
            self.__cmds = DesbastePCmds(self)

            self.geometry('850x320')
            self.title('Compilador G-Code | Configurações Avançadas - Rotações do Fuso')
            self.config(bg=ViewRpmDesbasp_Men.cor1)
            self.resizable(False, False)
            self.grab_set() 

            # SEÇÃO DE FRAMEs
            fra_p = self.__assents.criar_frame(10, 5, 305, 830, 10, 1, ViewRpmDesbasp_Men.cor1, ViewRpmDesbasp_Men.cor1, self)

            # SEÇÃO DE LABELs
            label_title = self.__assents.criar_label('Configurações - Rotações do Fuso', 10, 5, text_color=ViewRpmDesbasp_Men.cor2, font=('Corbel', 22, 'bold'), frame=fra_p)
            label_sub = self.__assents.criar_label(ViewRpmDesbasp_Men.sub, 10, 35, text_color=ViewRpmDesbasp_Men.cor4, font=('Corbel', 18, 'normal'), frame=fra_p)

            label_mod = self.__assents.criar_label('MODO DE VELO:', 10, 75, 0, 'MODO DE VELOCIDADE DO SPINDLE', text_color=ViewRpmDesbasp_Men.cor4, frame=fra_p)
            label_sen = self.__assents.criar_label('SENTI. DE GIRO :', 10, 111, 0, 'SENTIDO DE GIRO DO SPINDLE', text_color=ViewRpmDesbasp_Men.cor4, frame=fra_p)

            label_fus = self.__assents.criar_label('FUSO :', 520, 75, 0, 'ESCOLHA O FUSO (OPCIONAL)', text_color=ViewRpmDesbasp_Men.cor4, frame=fra_p)
            label_lim = self.__assents.criar_label('Limites - Superiores e Inferiores', 10, 160, text_color=ViewRpmDesbasp_Men.cor2, font=('Corbel', 22, 'bold'), frame=fra_p)

            label_sup = self.__assents.criar_label('SUPERIOR :', 10, 200, 0, 'LIMITE DE ROTAÇÃO SUPERIOR', text_color=ViewRpmDesbasp_Men.cor4, frame=fra_p)
            label_inf = self.__assents.criar_label('INFERIOR  :', 10, 235, 0, 'LIMITE DE ROTAÇÃO SUPERIOR', text_color=ViewRpmDesbasp_Men.cor4, frame=fra_p)

            # SEÇÃO DE LINHAs
            linha_h = ctk.CTkLabel(fra_p, 0, 0, text='', image=ViewRpmDesbasp_Men.img_lh)
            linha_h.place(x=10, y=140)

            # SEÇÃO DE ENTRYs
            self.entry_fus = self.__assents.criar_entry(585, 75, 135, 1, frame=fra_p)

            self.entry_sup = self.__assents.criar_entry(120, 200, 170, 1, frame=fra_p)
            self.entry_inf = self.__assents.criar_entry(120, 235, 170, 1, frame=fra_p)

            # SEÇÃO DE COMBOBOXs
            self.combo_mod = self.__assents.criar_combobox(160, 75, fra_p, 220, 10, ('CONSTANTE', 'FIXA'), state='disabled')
            self.combo_sen = self.__assents.criar_combobox(160, 111, fra_p, 220, 10, ('HORÁRIO', 'ANTI-HORÁRIO'), state='disabled')

            # SEÇÃO DE CHECKBOXs
            self.check_mod = self.__assents.criar_checkbox(395, 77, self.__cmds.unlock_mode, fra_p)
            self.check_sen = self.__assents.criar_checkbox(395, 113, self.__cmds.unlock_sense, fra_p)

            # SEÇÃO DE BUTTONs
            self.but_save = self.__assents.criar_button(713, 265, 20, 110, 'SAVE', self.__cmds.save_rotations,
                                                        ViewRpmDesbasp_Men.img_up,
                                                        ViewRpmDesbasp_Men.cor3,
                                                        ViewRpmDesbasp_Men.cor2,
                                                        ViewRpmDesbasp_Men.cor1,
                                                        ti='SALVAR CONFIGURAÇÕES', fr=fra_p)
        except Exception as e:
            messagebox.showerror('Compilador G-Code', 'Erro no momento de carregar os widgets da tela de configurações avançadas das rotações do fuso!')
            raise ValueError(f'Erro no momento de carregar os widgets da tela de configurações avançadas das rotações do fuso: {e}')