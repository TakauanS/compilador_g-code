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

    img_pr = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/padrao.png'), size=(25, 25))
    img_up = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/upload.png'), size=(24, 24))
    img_lh = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(675, 24))
    img_lv = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_v.png'), size=(20, 33))

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
            self.label_se = self.__assents.criar_label('SENTIDO ROT:', 10, 110, tooltip='SENTIDO DE ROTAÇÃO', text_color=Parameters.cor4, frame=self.fra_m)

            self.label_fr = self.__assents.criar_label('FERRAMENTA:', 10, 10, text_color=Parameters.cor4, frame=self.fra_m)
            self.label_rp = self.__assents.criar_label('ROTAÇÃO:', 10, 45, text_color=Parameters.cor4, frame=self.fra_m)

            self.label_av = self.__assents.criar_label('AVANÇO:', 405, 10, text_color=Parameters.cor4, frame=self.fra_m)
            self.label_ps = self.__assents.criar_label('PASSE:', 405, 45, text_color=Parameters.cor4, frame=self.fra_m)

            # SEÇÃO DE ENTRYs
            self.entry_rp = self.__assents.criar_entry(150, 45, 190, border_width=1 ,frame=self.fra_m)
            self.entry_av = self.__assents.criar_entry(500, 10, 185, border_width=1 ,frame=self.fra_m)
            self.entry_ps = self.__assents.criar_entry(500, 45, 185, border_width=1 ,frame=self.fra_m)

            # SEÇÃO DE COMBOBOXs
            self.combo_se = self.__assents.criar_combobox(150, 110, self.fra_m, 190, values=('SENTIDO - HR', 'SENTIDO - AHR'))
            self.combo_fr = self.__assents.criar_combobox(150, 10, self.fra_m, 190, values=('T10D1', 'T11D1'))

            # SEÇÃO DE LINHAs
            self.linha1 = ctk.CTkLabel(self.fra_m, text='', image=Parameters.img_lh)
            self.linha1.place(x=10, y=80)

            self.linha2 = ctk.CTkLabel(self.fra_m, text='', image=Parameters.img_lv)
            self.linha2.place(x=560, y=220)

            self.but_save = self.__assents.criar_button(580, 220, 20, 110, 'SAVE', self.__cmds.save_parameters,
                                                        Parameters.img_up,
                                                        Parameters.cor3,
                                                        Parameters.cor2,
                                                        Parameters.cor1,
                                                        ti='salvar parâmetros', fr=self.fra_m)
  
            self.but_padrao = self.__assents.criar_button(530, 220, 5, 5, '', self.__cmds.save_parameters, 
                                                          Parameters.img_pr, 
                                                          Parameters.cor1, 
                                                          Parameters.cor1, 
                                                          Parameters.cor1, 
                                                          ti='parâmetros de corte padrão', fr=self.fra_m)

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na geração da tela de parâmetros de corte:\n\n{e}')
            print(f'Erro: {e}')