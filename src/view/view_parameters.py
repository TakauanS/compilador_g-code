from PIL import Image
import customtkinter as ctk
from tkinter import messagebox

from src.model.assents import Assents
from src.controller.buttons_cmds.parameters_cmds import ParametersCmds

class ViewParameters(ctk.CTkToplevel):

    cor1 = '#FCF6F2' # Cor branca para FG-COLOR
    cor2 = '#1A8AE5' # Cor azul para butões FG-COLOR
    cor3 = '#3757A0' # Cor azul para botões HOUVER-COLOR
    cor4 = 'black'   # Cor preta para TEXT-COLOR
    
    img_pr = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/padrao.png'), size=(25, 25))
    img_up = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/upload.png'), size=(24, 24))
    img_lv = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_v.png'), size=(20, 33))
    img_lh = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(840, 24))

    sub = 'Insira os parâmetros de corte para gerar o código CNC do seu ciclo de usinagem.'

    def __init__(self):
        try:
            super().__init__()

            self.__assents = Assents(self)
            self.__cmds = ParametersCmds(self)

            self.geometry('880x320')
            self.title('Compilador G-Code | Parâmetros de Corte')
            self.resizable(False, False)
            self.config(bg=ViewParameters.cor1)

            # SEÇÃO DE FRAMES
            self.fra_p = self.__assents.criar_frame(10, 10, 300, 860, 10, 1, ViewParameters.cor1, ViewParameters.cor1, self)

            # SEÇÃO DE LABELs
            self.label_title = self.__assents.criar_label('Parâmetros de Corte', 10, 5, text_color=ViewParameters.cor2, font=('Corbel', 22, 'bold'), frame=self.fra_p)
            self.label_sub = self.__assents.criar_label(ViewParameters.sub, 10, 35, text_color=ViewParameters.cor4, font=('Corbel', 18, 'normal'), frame=self.fra_p)

            self.label_sent = self.__assents.criar_label('SENT ROT.SPDL:', 10, 75, 0, 'SENTIDO DE ROTAÇÃO DO SPINDLE', text_color=ViewParameters.cor4, frame=self.fra_p)
            self.label_ferr = self.__assents.criar_label('FERRAMENTA:', 10, 111, 0, '', text_color=ViewParameters.cor4, frame=self.fra_p)
            self.label_rpm = self.__assents.criar_label('ROTAÇÃO | RPM:', 10, 180, 0, '', text_color=ViewParameters.cor4, frame=self.fra_p)
            self.label_avan = self.__assents.criar_label('AVANÇO:', 550, 75, 0, '', text_color=ViewParameters.cor4, frame=self.fra_p)
            self.label_pass = self.__assents.criar_label('PASSE:', 550, 111, 0, '', text_color=ViewParameters.cor4, frame=self.fra_p)

            # SEÇÃO DE ENTRYs
            self.entry_avan = self.__assents.criar_entry(645, 75, 205, 1, frame=self.fra_p)
            self.entry_pass = self.__assents.criar_entry(645, 111, 205, 1, frame=self.fra_p)
            self.entry_rpm = self.__assents.criar_entry(170, 180, 200, 1, frame=self.fra_p)

            # SEÇÃO DE LINHAs
            self.linha1 = ctk.CTkLabel(self.fra_p, 0, 0, text='', image=ViewParameters.img_lh)
            self.linha1.place(x=10, y=150)

            self.linha2 = ctk.CTkLabel(self.fra_p, 0, 0, text='', image=ViewParameters.img_lv)
            self.linha2.place(x=720, y=260)

            # SEÇÃO DE COMBOBOXs
            self.com_sent = self.__assents.criar_combobox(170, 75, self.fra_p, 200, 10, ('HORÁRIO', 'ANTI-HORÁRIO'))
            self.com_ferr = self.__assents.criar_combobox(170, 111, self.fra_p, 200, 10, ('T10D1', 'T11D1'))

            # SEÇÃO DE BUTTONs
            self.but_save = self.__assents.criar_button(740, 260, 20, 110, 'SAVE', self.__cmds.save_parameters,
                                                        ViewParameters.img_up,
                                                        ViewParameters.cor3,
                                                        ViewParameters.cor2,
                                                        ViewParameters.cor1,
                                                        ti='SALVAR PARÂMETROS', fr=self.fra_p)
            
            self.but_padrao = self.__assents.criar_button(690, 260, 5, 5, '', self.__cmds.insert_parameters, 
                                                          ViewParameters.img_pr, 
                                                          ViewParameters.cor1, 
                                                          ViewParameters.cor1, 
                                                          ViewParameters.cor1, 
                                                          ti='PARÂMETROS DE CORTE PADRÃO', fr=self.fra_p)

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na geração da tela de parâmetros de corte:\n\n{e}')
            print(f'Erro: {e}')