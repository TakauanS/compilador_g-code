from PIL import Image
import customtkinter as ctk
from tkinter import messagebox

from src.model.assents import Assents
from src.model.json_manager.cy_parametrizados.json_desbastep import JsonDesbasteP
from src.controller.buttons_cmds.cycles_cmds.cy_parametrizados_cmds.cy_desbastep_cmd import DesbastePCmds

class ViewAvaDesbasp_Men(ctk.CTkToplevel):

    cor1 = '#FFFFFF'
    cor2 = '#1A8AE5'
    cor3 = '#3757A0'
    cor4 = '#000000'

    img_up = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/upload.png'), size=(24, 24))
    img_lh = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(362, 24))

    sub1 = 'Configure os avanços de trabalho considerando a capacidade da máquina, o tipo de ferramenta e'
    sub2 = 'a remoção de material esperada.'

    def __init__(self):
        try:
            super().__init__()

            self.json = JsonDesbasteP()
            self.assents = Assents(self)
            self.cmds = DesbastePCmds(self)

            self.geometry('850x320')
            self.title('Compilador G-Code | Configurações Avançadas - Avanços')
            self.config(bg=ViewAvaDesbasp_Men.cor1)
            self.resizable(False, False)
            self.grab_set()

            # SEÇÃO DE VARIÁVEIS JSONs
            vc_conf = self.json.get_data(self.json.data_rotations, 'modo_velo')
            av_conf = self.json.get_data(self.json.data_desbastep, 'avan')

            # SEÇÃO DE FRAMEs
            fra_p = self.assents.criar_frame(10, 5, 305, 830, 10, 1, ViewAvaDesbasp_Men.cor1, ViewAvaDesbasp_Men.cor1, self)

            # SEÇÃO DE LABELs
            label_title = self.assents.criar_label('Configurações - Avanços', 10, 5, text_color=ViewAvaDesbasp_Men.cor2, font=('Corbel', 22, 'bold'), frame=fra_p)
            label_sub1 = self.assents.criar_label(ViewAvaDesbasp_Men.sub1, 10, 35, text_color=ViewAvaDesbasp_Men.cor4, font=('Corbel', 18, 'normal'), frame=fra_p)
            label_sub2 = self.assents.criar_label(ViewAvaDesbasp_Men.sub2, 10, 55, text_color=ViewAvaDesbasp_Men.cor4, font=('Corbel', 18, 'normal'), frame=fra_p)

            label_tip = self.assents.criar_label('TIPO DE AVANÇO:', 10, 126, 0, 'TIPO DE AVANÇO DE CORTE', text_color=ViewAvaDesbasp_Men.cor4, frame=fra_p)
            label_mod = self.assents.criar_label('MODO DE AVANÇO:', 10, 90, 0, 'MODO DE AVANÇO DE CORTE', text_color=ViewAvaDesbasp_Men.cor4, frame=fra_p)

            label_deb = self.assents.criar_label('AVANÇO DESB:', 10, 226, 0, 'AVANÇO DE CORTE (DESBASTE)', text_color=ViewAvaDesbasp_Men.cor4, frame=fra_p)
            label_aca = self.assents.criar_label('AVANÇO ACAB:', 10, 190, 0, 'AVANÇO DE CORTE (ACABAMENTO)', text_color=ViewAvaDesbasp_Men.cor4, frame=fra_p)

            label_lim = self.assents.criar_label('LIMIT. AVANÇO:', 475, 90, 0, 'LIMITE DE AVANÇO DE CORTE', text_color=ViewAvaDesbasp_Men.cor4, frame=fra_p)
            label_vel = self.assents.criar_label(f'modo_velo: {vc_conf}', 10, 285, 0, 'MODO DE VELOCIDADE DE CORTE', 
                                                 text_color=ViewAvaDesbasp_Men.cor4, 
                                                 font=('Corbel', 14, 'normal'), 
                                                 frame=fra_p)
            # SEÇÃO DE LINHAs
            linha_h = ctk.CTkLabel(fra_p, 0, 0, text='', image=ViewAvaDesbasp_Men.img_lh)
            linha_h.place(x=10, y=160)
            
            # SEÇÃO DE ENTRYs
            self.entry_deb = self.assents.criar_entry(155, 226, 150, 1, frame=fra_p)
            self.entry_deb.insert(0, av_conf)
            self.entry_deb.configure(state='disabled')

            self.entry_aca = self.assents.criar_entry(155, 190, 150, 1, frame=fra_p)
            self.entry_aca.insert(0, av_conf)
            self.entry_aca.configure(state='disabled')

            self.entry_lim = self.assents.criar_entry(625, 90, 150, 1, frame=fra_p)

            # SEÇÃO DE COMBOBOXs
            self.combo_tip = self.assents.criar_combobox(190, 126, fra_p, 180, 10, ('mm/min', 'mm/rot'), state='disabled')
            self.combo_mod = self.assents.criar_combobox(190, 90, fra_p, 180, 10, ('FNORM', 'FLIN'), state='disabled')

            # SEÇÃO DE CHECKBOXs
            self.check_deb = self.assents.criar_checkbox(315, 229, self.cmds.unlock_advance_desb, fra_p)
            self.check_aca = self.assents.criar_checkbox(315, 193, self.cmds.unlock_advance_acab, fra_p)

            self.check_tip = self.assents.criar_checkbox(382, 129, self.cmds.unlock_tip_advance, fra_p)
            self.check_mod = self.assents.criar_checkbox(382, 93, self.cmds.unlock_mod_advance, fra_p)

            # SEÇÃO DE BUTTONs
            self.but_save = self.assents.criar_button(713, 265, 20, 110, 'SAVE', self.cmds.save_advance,
                                                        ViewAvaDesbasp_Men.img_up,
                                                        ViewAvaDesbasp_Men.cor3,
                                                        ViewAvaDesbasp_Men.cor2,
                                                        ViewAvaDesbasp_Men.cor1,
                                                        ti='SALVAR CONFIGURAÇÕES', fr=fra_p)
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de gerenciar os widgets da tela de configuração de avanços do ciclo:\n\n{e}')
            raise Exception(f'Erro no momento de gerenciar os widgets da tela de configuração de avanços do ciclo: {e}')