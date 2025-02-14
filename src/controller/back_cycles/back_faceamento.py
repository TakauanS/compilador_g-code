from src.model.cycles.cycle_faceamento import CicloFaceamento
from src.model.assents import Assents
from src.controller.menu import Menu
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image

class BackFaceamento:

    img_linha = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha.png'), size=(825, 20))
    img_code = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/code.png'), size=(24, 24))

    def __init__(self, master):

        self.master = master
        self.menu = Menu(root=self.master)
        self.__assents = Assents(master=self.master)

        # SEÇÃO DE LABELs

        label_diametroi = self.__assents.criar_label(text='DIÂMETRO INICIAL', x=15, y=10)
        label_diametrof = self.__assents.criar_label(text='DIÂMETRO FINAL', x=15, y=50)

        label_ferramenta = self.__assents.criar_label(text='FERRAMENTA', x=15, y=170)
        label_ref = self.__assents.criar_label(text='REF. DE TRABALHO', x=15, y=130)

        label_espessura = self.__assents.criar_label(text='ESPESSURA', x=500, y=10)
        label_rotacao = self.__assents.criar_label(text='ROTAÇÃO', x=500, y=130)

        label_passe = self.__assents.criar_label(text='PASSE', x=500, y=50)
        label_avanco = self.__assents.criar_label(text='AVANÇO', x=500, y=170)

        label_linha = ctk.CTkLabel(master=self.master, text='ㅤ', image=BackFaceamento.img_linha)
        label_linha.place(x=15, y=95)

        # SEÇÃO DE ENTRYs

        self.entry_ferramenta = self.__assents.criar_entry(x=220, y=170)
        self.entry_espessura = self.__assents.criar_entry(x=640, y=10)

        self.entry_diametroi = self.__assents.criar_entry(x=220, y=10)
        self.entry_diametrof = self.__assents.criar_entry(x=220, y=50)

        self.entry_rotacao = self.__assents.criar_entry(x=640, y=130)
        self.entry_passe = self.__assents.criar_entry(x=640, y=50)

        self.entry_avanco = self.__assents.criar_entry(x=640, y=170)
        self.entry_ref = self.__assents.criar_entry(x=220, y=130)

        # SEÇÃO DE BUTTONs

        self.button_code = self.__assents.criar_button(text='G-CODE', command=self.gcode_faceamento, image=BackFaceamento.img_code, x=705, y=355)

    def gcode_faceamento(self):

        validacao_code = messagebox.askquestion(title='Compilador G-Code', message='Antes de prosseguir para gerar o G-code, você configurou os posicionamentos da ferramenta corretamente?')

        if validacao_code == 'yes':

            try:
                diametro_inicial = float(self.entry_diametroi.get())
                diametro_final = float(self.entry_diametrof.get())
                espessura = float(self.entry_espessura.get())
                rotacao = float(self.entry_rotacao.get())
                avanco = float(self.entry_avanco.get())
                passe = float(self.entry_passe.get())

                ferramenta = self.entry_ferramenta.get().upper()
                referencia = self.entry_ref.get().upper()

                ciclo_faceamento = CicloFaceamento(diametro_inicial=diametro_inicial, diametro_final=diametro_final, espessura=espessura)

                ciclo_faceamento.referencia_trabalho(referencia=referencia)
                ciclo_faceamento.ferramenta(tool=ferramenta)
                ciclo_faceamento.avanco(advance=avanco)
                ciclo_faceamento.rotacao(rpm=rotacao)
                ciclo_faceamento.passe(pf=passe)

                ciclo_faceamento.pos_segurancaX(posx=self.menu.get_posx)
                ciclo_faceamento.pos_segurancaZ(posz=self.menu.get_posz)
            
            except Exception as e:
                messagebox.showerror(title='Compilador G-Code', message='')
                print(f'Erro! {e}')
            else:
                ciclo_faceamento.gcode()
        else:
            pass