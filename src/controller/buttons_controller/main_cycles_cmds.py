from PIL import Image
import customtkinter as ctk
from tkinter import messagebox

from src.model.json_handler import JsonHandler

class MainCyclesCmds:

    cor1 = '#F2F1F0'
    cor2 = '#1A8AE5'

    sub = 'Insira as informações em todos os campos abaixo para compilar o ciclo de desbaste parametrizado.'
    pre = 'Veja o preview do seu G-code para conferir se os parâmetros estão corretos antes de enviar para a máquina.'

    img_par = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/parametros.png'), size=(25, 25))
    img_pen = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/pendrive.png'), size=(25, 25))
    img_lhm = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(810, 25))
    img_lih = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha_h.png'), size=(25, 25))
    img_rea = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/readme.png'), size=(25, 25))

    def __init__(self, master, toplevel):
        self.__master = master
        self.__top = toplevel
        
        self.__file_json = JsonHandler()
        self.__file_json.convert_files()

    # Método responsável por chamar o ciclo de desbaste parametrizado
    def call_cycle_desbastep(self):
        try:
            # SEÇÃO DE FRAMEs
            self.__master.fra_code = ctk.CTkFrame(self.__master.fra_main, width=880, height=330, corner_radius=8, border_width=1, fg_color=MainCyclesCmds.cor1)
            self.__master.fra_code.place(x=5, y=70)

            self.__master.fra_menu = ctk.CTkFrame(self.__master.fra_code, width=40, height=155, corner_radius=8, border_width=1, fg_color=MainCyclesCmds.cor1)
            self.__master.fra_menu.place(x=835, y=5)

            # SEÇÃO DE LABELs   
            self.__master.label_title = ctk.CTkLabel(self.__master.fra_main, text='Ciclo de Desbaste | Parametrizado', text_color=MainCyclesCmds.cor2, font=('Corbel', 22, 'bold'))
            self.__master.label_title.place(x=10, y=5)

            self.__master.label_sub = ctk.CTkLabel(self.__master.fra_main, text=MainCyclesCmds.sub, font=('Corbel', 18, 'normal'))
            self.__master.label_sub.place(x=10, y=30)

            self.__master.label_dii = ctk.CTkLabel(self.__master.fra_code, text='Ø DIÂMETRO INICIAL:', font=('Corbel', 20, 'normal'))
            self.__master.label_dii.place(x=10, y=10)

            self.__master.label_dif = ctk.CTkLabel(self.__master.fra_code, text='Ø DIÂMETRO FINAL:', font=('Corbel', 20, 'normal'))
            self.__master.label_dif.place(x=10, y=46)

            self.__master.label_esp = ctk.CTkLabel(self.__master.fra_code, text='ESPESSURA:', font=('Corbel', 20, 'normal'))
            self.__master.label_esp.place(x=480, y=10)

            self.__master.label_pas = ctk.CTkLabel(self.__master.fra_code, text='PASSE:', font=('Corbel', 20, 'normal'))
            self.__master.label_pas.place(x=480, y=46)

            self.__master.label_pre = ctk.CTkLabel(self.__master.fra_code, text='PREVIEW - CODE', text_color=MainCyclesCmds.cor2, font=('Corbel', 23, 'bold'))
            self.__master.label_pre.place(x=10, y=110)

            self.__master.label_pre = ctk.CTkLabel(self.__master.fra_main, text=MainCyclesCmds.pre, font=('Corbel', 18, 'normal'))
            self.__master.label_pre.place(x=15, y=210)

            self.__master.label_man = ctk.CTkLabel(self.__master.fra_main,
                                                   font=('Corbel', 18, 'normal'),
                                                   text_color=MainCyclesCmds.cor2,  
                                                   text=f'CMP_MAIN{self.__file_json.get_data(self.__file_json.data_file, 'extensão')}')
            self.__master.label_man.place(x=15, y=240)

            self.__master.label_con = ctk.CTkLabel(self.__master.fra_main,
                                                   font=('Corbel', 18, 'normal'),
                                                   text_color=MainCyclesCmds.cor2, 
                                                   text=f'CMP_CONTROLS{self.__file_json.get_data(self.__file_json.data_file, 'extensão')}')
            self.__master.label_con.place(x=455, y=240)

            # SEÇÃO DE LINHAs
            self.__master.linha1 = ctk.CTkLabel(self.__master.fra_menu, image=MainCyclesCmds.img_lih, text='')
            self.__master.linha1.place(x=7, y=35)

            self.__master.linha2 = ctk.CTkLabel(self.__master.fra_menu, image=MainCyclesCmds.img_lih, text='')
            self.__master.linha2.place(x=7, y=90)

            self.__master.linha3 = ctk.CTkLabel(self.__master.fra_code, image=MainCyclesCmds.img_lhm, text='')
            self.__master.linha3.place(x=10, y=85)

            # SEÇÃO DE ENTRYs
            self.__master.entry_dii = ctk.CTkEntry(self.__master.fra_code, width=220, border_width=1, corner_radius=10, justify='center', font=('Arial', 16))
            self.__master.entry_dii.place(x=210, y=11)

            self.__master.entry_dif = ctk.CTkEntry(self.__master.fra_code, width=220, border_width=1, corner_radius=10, justify='center', font=('Arial', 16))
            self.__master.entry_dif.place(x=210, y=47)

            self.__master.entry_esp = ctk.CTkEntry(self.__master.fra_code, width=220, border_width=1, corner_radius=10, justify='center', font=('Arial', 16))
            self.__master.entry_esp.place(x=600, y=11)

            self.__master.entry_pas = ctk.CTkEntry(self.__master.fra_code, width=220, border_width=1, corner_radius=10, justify='center', font=('Arial', 16))
            self.__master.entry_pas.place(x=600, y=47)

            # SEÇÃO DE BUTTONs
            self.__master.but_par = ctk.CTkButton(self.__master.fra_menu, width=15, height=15, text='', corner_radius=0, image=MainCyclesCmds.img_par, fg_color=MainCyclesCmds.cor1, hover_color=MainCyclesCmds.cor1)
            self.__master.but_par.place(x=4, y=5)

            self.__master.but_pen = ctk.CTkButton(self.__master.fra_menu, width=15, height=15, text='', corner_radius=0, image=MainCyclesCmds.img_pen, fg_color=MainCyclesCmds.cor1, hover_color=MainCyclesCmds.cor1)
            self.__master.but_pen.place(x=4, y=60)

            self.__master.but_sav = ctk.CTkButton(self.__master.fra_menu, width=15, height=15, text='', corner_radius=0, image=MainCyclesCmds.img_rea, fg_color=MainCyclesCmds.cor1, hover_color=MainCyclesCmds.cor1)
            self.__master.but_sav.place(x=4, y=115)

            self.__master.preview_code1 = ctk.CTkTextbox(self.__master.fra_main, width=430, height=120, corner_radius=8, border_width=1).place(x=15, y=270)
            self.__master.preview_code2 = ctk.CTkTextbox(self.__master.fra_main, width=420, height=120, corner_radius=8, border_width=1).place(x=455, y=270)

            self.__top.destroy()
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code | Cycles', f'Ocorreu um erro ao chamar o ciclo de desbaste parametrizado:\n\n{e}')
            print(f'Erro! {e}')
