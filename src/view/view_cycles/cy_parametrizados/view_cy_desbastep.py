from PIL import Image
import customtkinter as ctk
from tkinter import messagebox
from src.model.assents import Assents

from src.model.json_handler import JsonHandler
from src.controller.buttons_cmds.cycles_cmds.cy_parametrizados_cmds.cy_desbastep_cmd import DesbastePCmds

class ViewCyDesbasteP(ctk.CTkFrame):

    cor1 = '#FCF6F2' # Cor branca para FG-COLOR
    cor2 = '#1A8AE5' # Cor Azul para FG-COLOR
    cor3 = 'black'   # Cor preta para TEXT-COLOR

    sub = 'Insira as informações em todos os campos abaixo para compilar o ciclo de desbaste parametrizado.'
    pre = 'Veja o preview do seu G-code para conferir se os parâmetros estão corretos antes de enviar para a máquina.'

    img_par = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/parametros.png'), size=(25, 25))
    img_pen = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/pendrive.png'), size=(25, 25))
    img_lhm = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(810, 25))
    img_lih = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(25, 25))
    img_rea = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/readme.png'), size=(25, 25))

    def __init__(self, master, toplevel):
        try:
            super().__init__(master)

            self.__master = master
            self.__toplevel = toplevel
    
            self.__json = JsonHandler()
            self.__json.convert_files()

            self.__assents = Assents(self.__master)
            self.__cmds = DesbastePCmds(self.__master)

            # SEÇÃO DE FRAMEs
            self.__master.fra_code = ctk.CTkFrame(self.__master.fra_main, width=880, height=295, corner_radius=8, border_width=1, fg_color=ViewCyDesbasteP.cor1)
            self.__master.fra_code.place(x=5, y=70)

            self.__master.fra_menu = ctk.CTkFrame(self.__master.fra_code, width=40, height=155, corner_radius=8, border_width=1, fg_color=ViewCyDesbasteP.cor1)
            self.__master.fra_menu.place(x=835, y=5)

            # SEÇÃO DE LABELs
            self.__master.label_title = self.__assents.criar_label('Ciclo de Desbaste | Parametrizado', 10, 5, text_color=ViewCyDesbasteP.cor2, font=('Corbel', 22, 'bold'), frame=self.__master.fra_main)
            self.__master.label_sub = self.__assents.criar_label(ViewCyDesbasteP.sub, 10, 35, text_color=ViewCyDesbasteP.cor3, font=('Corbel', 18, 'normal'), frame=self.__master.fra_main)

            self.__master.label_dii = self.__assents.criar_label('Ø DIÂMETRO INICIAL:', 10, 10, text_color=ViewCyDesbasteP.cor3, frame=self.__master.fra_code)
            self.__master.label_dif = self.__assents.criar_label('Ø DIÂMETRO FINAL:', 10, 46, text_color=ViewCyDesbasteP.cor3, frame=self.__master.fra_code)
            self.__master.label_esp = self.__assents.criar_label('ESPESSURA:', 480, 10, text_color=ViewCyDesbasteP.cor3, frame=self.__master.fra_code)

            self.__master.label_prp = self.__assents.criar_label('PREVIEW - CODE', 10, 110, text_color=ViewCyDesbasteP.cor2, font=('Corbel', 23, 'bold'), frame=self.__master.fra_code)
            self.__master.label_prt = self.__assents.criar_label(ViewCyDesbasteP.pre, 10, 140, text_color=ViewCyDesbasteP.cor3, font=('Corbel', 18, 'normal'), frame=self.__master.fra_code)

            # SEÇÃO DE LINHAs
            self.__master.linha1 = ctk.CTkLabel(self.__master.fra_menu, image=ViewCyDesbasteP.img_lih, text='')
            self.__master.linha1.place(x=7, y=35)

            self.__master.linha2 = ctk.CTkLabel(self.__master.fra_menu, image=ViewCyDesbasteP.img_lih, text='')
            self.__master.linha2.place(x=7, y=90)

            self.__master.linha3 = ctk.CTkLabel(self.__master.fra_code, image=ViewCyDesbasteP.img_lhm, text='')
            self.__master.linha3.place(x=10, y=85)

            # SEÇÃO DE ENTRYs
            self.__master.entry_dii = self.__assents.criar_entry(210, 11, 220, 1, self.__master.fra_code)
            self.__master.entry_dif = self.__assents.criar_entry(210, 47, 220, 1, self.__master.fra_code)
            self.__master.entry_esp = self.__assents.criar_entry(600, 11, 220, 1, self.__master.fra_code)
        
            # SEÇÃO DE BUTTONs
            self.__master.but_par = ctk.CTkButton(self.__master.fra_menu, command=self.__cmds.call_parameters, width=15, height=15, text='', corner_radius=0, image=ViewCyDesbasteP.img_par, fg_color=ViewCyDesbasteP.cor1, hover_color=ViewCyDesbasteP.cor1)
            self.__master.but_par.place(x=4, y=5)

            self.__master.but_pen = ctk.CTkButton(self.__master.fra_menu, width=15, height=15, text='', corner_radius=0, image=ViewCyDesbasteP.img_pen, fg_color=ViewCyDesbasteP.cor1, hover_color=ViewCyDesbasteP.cor1)
            self.__master.but_pen.place(x=4, y=60)

            self.__master.but_sav = ctk.CTkButton(self.__master.fra_menu, command=self.__cmds.up_gcode, width=15, height=15, text='', corner_radius=0, image=ViewCyDesbasteP.img_rea, fg_color=ViewCyDesbasteP.cor1, hover_color=ViewCyDesbasteP.cor1)
            self.__master.but_sav.place(x=4, y=115)

            self.__toplevel.destroy()

        except Exception as e:
            messagebox.showerror('Compilador G-Code | Cycles', f'Ocorreu um erro ao chamar o ciclo de desbaste parametrizado:\n\n{e}')
            print(f'Erro! {e}')