from PIL import Image
import customtkinter as ctk
from tkinter import messagebox

from src.model.assents import Assents
from src.controller.buttons_cmds.parameters_cmds import ParametersCmds

class Parameters(ctk.CTkToplevel):

    cor1 = '#FCF6F2' # Cor branca para FG-COLOR
    cor2 = '#1A8AE5' # Cor azul para butões FG-COLOR
    cor3 = '#3757A0' # Cor azul para botões HOUVER-COLOR
    cor4 = 'black'   # Cor preta para TEXT-COLOR

    img_up = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/upload.png'), size=(24, 24))
    img_ln = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(675, 24))

    def __init__(self):
        try:
            super().__init__()

            self.__assents = Assents(self)
            self.__cmds = ParametersCmds(self)

            self.title('Compilador G-Code | Parâmetros de Corte')
            self.geometry('720x300')
            self.resizable(False, False)
            self.config(bg=Parameters.cor1)

            # SEÇÃO DE LABELFRAMEs
            self.fra_m = self.__assents.criar_labelframe(10, 5, 700, 285, 'Parâmetros de Corte:', frame=self)

            # SEÇÃO DE LABELs
            self.label_se = self.__assents.criar_label('SENT. ROT. SPDL:', 10, 110, text_color=Parameters.cor4, frame=self.fra_m)

            self.label_md = self.__assents.criar_label('MODO VEL. SPDL:', 10, 10, text_color=Parameters.cor4, frame=self.fra_m)
            self.label_fr = self.__assents.criar_label('FERRAMENTA:', 10, 45, text_color=Parameters.cor4, frame=self.fra_m)

            self.label_av = self.__assents.criar_label('AVANÇO:', 405, 10, text_color=Parameters.cor4, frame=self.fra_m)
            self.label_ps = self.__assents.criar_label('PASSE:', 405, 45, text_color=Parameters.cor4, frame=self.fra_m)

            # SEÇÃO DE ENTRYs
            self.entry_av = self.__assents.criar_entry(500, 10, 185, border_width=1 ,frame=self.fra_m)
            self.entry_ps = self.__assents.criar_entry(500, 45, 185, border_width=1 ,frame=self.fra_m)

            # SEÇÃO DE COMBOBOXs
            self.combo_se = self.__assents.criar_combobox(175, 110, self.fra_m, 190, values=('SENTIDO - HR', 'SENTIDO - AHR'))
            self.combo_md = self.__assents.criar_combobox(175, 10, self.fra_m, 190, values=('G96 - VCC', 'G97 - RPM FIXO'))
            self.combo_fr = self.__assents.criar_combobox(175, 45, self.fra_m, 190, values=('T10D1', 'T11D1'))

            # SEÇÃO DE LINHAs
            self.linha1 = ctk.CTkLabel(self.fra_m, text='', image=Parameters.img_ln)
            self.linha1.place(x=10, y=80)

            self.but_savec = ctk.CTkButton(self.fra_m,
                                           width=110,
                                           height=20, 
                                           text='SAVE',
                                           compound='right',
                                           corner_radius=13,
                                           image=Parameters.img_up,
                                           fg_color=Parameters.cor2,
                                           bg_color=Parameters.cor1,
                                           font=('Arial', 15, 'bold'), 
                                           hover_color=Parameters.cor3,
                                           command=self.__cmds.save_parameters).place(x=580, y=220)

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na geração da tela de parâmetros de corte:\n\n{e}')
            print(f'Erro: {e}')