from PIL import Image
import customtkinter as ctk
from tkinter import messagebox

from src.model.assents import Assents
from src.controller.buttons_cmds.pos_cmds.posp_cmds import PospCmds

class ViewPosp(ctk.CTkToplevel):

    cor1 = '#FCF6F2' # Cor branca para FG-COLOR
    cor2 = '#1A8AE5' # Cor azul para butões FG-COLOR
    cor3 = '#3757A0' # Cor azul para botões HOUVER-COLOR
    cor4 = 'black'   # Cor preta para TEXT-COLOR

    img_up = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/upload.png'), size=(24, 24))
    img_lh = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(365, 24))
    img_lv1 = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_v.png'), size=(20, 33))
    img_lv2 = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_v.png'), size=(20, 200))
    
    sub = 'Insira os valores de aproximação da ferramenta antes do início do ciclo de desbaste parametrizado.'

    def __init__(self):
        try:
            super().__init__()

            self.__cmds = PospCmds(self)
            self.__assents = Assents(self)

            self.geometry('880x320')
            self.title('Compilador G-Code | Ciclo de Desbaste Parametrizado - Posicionamentos')
            self.config(bg=ViewPosp.cor1)
            self.resizable(False, False)
            self.grab_set() # Dar foco máximo a tela de posicionamentos 

            # SEÇÃO DE FRAMEs
            self.fra_p = self.__assents.criar_frame(10, 10, 300, 860, 10, 1, ViewPosp.cor1, ViewPosp.cor1, self)

            # SEÇÃO DE LINHAs
            self.linha1 = ctk.CTkLabel(self.fra_p, 0, 0, text='', image=ViewPosp.img_lh)
            self.linha1.place(x=10, y=150)

            self.linha2 = ctk.CTkLabel(self.fra_p, 0, 0, text='', image=ViewPosp.img_lv2)
            self.linha2.place(x=380, y=60)

            # SEÇÃO DE LABELs
            self.label_title = self.__assents.criar_label('Posicionamentos de Segurança', 10, 5, text_color=ViewPosp.cor2, font=('Corbel', 22, 'bold'), frame=self.fra_p)
            self.label_sub = self.__assents.criar_label(ViewPosp.sub, 10, 35, text_color=ViewPosp.cor4, font=('Corbel', 18, 'normal'), frame=self.fra_p)

            self.label_posx = self.__assents.criar_label('POS. TROCA (X):', 10, 75, 0, 'POSICIONAMENTO DE TROCA DE FERRAMENTA EM X', text_color=ViewPosp.cor4, frame=self.fra_p)
            self.label_posz = self.__assents.criar_label('POS. TROCA (Z):', 10, 111, 0, 'POSICIONAMENTO DE TROCA DE FERRAMENTA EM Z', text_color=ViewPosp.cor4, frame=self.fra_p)
            self.label_aprx = self.__assents.criar_label('APROXIMA. (X):', 10, 180, 0, ' APROXIMAÇÃO DA FERRAMENTA EM X', text_color=ViewPosp.cor4, frame=self.fra_p)
            self.label_aprz = self.__assents.criar_label('APROXIMA. (Z):', 10, 216, 0, ' APROXIMAÇÃO DA FERRAMENTA EM Z', text_color=ViewPosp.cor4, frame=self.fra_p)

            # SEÇÃO DE ENTRYs
            self.entry_posx = self.__assents.criar_entry(170, 75, 205, 1, frame=self.fra_p)
            self.entry_posz = self.__assents.criar_entry(170, 111, 205, 1, frame=self.fra_p)
            self.entry_aprx = self.__assents.criar_entry(170, 180, 205, 1, frame=self.fra_p)
            self.entry_aprz = self.__assents.criar_entry(170, 216, 205, 1, frame=self.fra_p)

            # SEÇÃO DE BUTTONs
            self.but_save = self.__assents.criar_button(740, 260, 20, 110, 'SAVE', self.__cmds.save_positioning,
                                                        ViewPosp.img_up,
                                                        ViewPosp.cor3,
                                                        ViewPosp.cor2,
                                                        ViewPosp.cor1,
                                                        ti='SALVAR POSICIONAMENTOS', fr=self.fra_p)
            
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Aconteceu um erro inesperado na tela de posicionamentos dos parametrizados:\n\n{e}')
            raise ValueError(f'Aconteceu um erro inesperado na tela de posicionamentos dos parametrizados: {e}')