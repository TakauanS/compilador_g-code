from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(base_dir)

from src.model.cycles.cycle_faceamento import CicloFaceamento
from src.model.cycles.cycle_desbaste import CicloDesbaste
from src.model.cycles.cycle_canal import CicloCanal
from src.model.assents import Assents
from src.controller.menu import Menu

class ButtonHandler:

    # SEÇÃO DE EXPORTAÇÃO DE IMAGEs

    img_linha = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha.png'), size=(825, 20))
    img_code = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/code.png'), size=(24, 24))

    def __init__(self, master):

        self.master = master
        self.menu = Menu(root=self.master)
        self.assents = Assents(master=self.master)
        
        self.comandos = {
            "! compile -c: desbaste": self.desbaste,
            "! compile -c: canais": self.canais,
            "! compile -c: faceamento": self.faceamento
        }

    def executar_comando(self, comando):

        if comando not in self.comandos:
            messagebox.showerror(title='Compilador G-Code', message='O comando informado não existe no sistema. Por favor, verifique e tente novamente.')
        else:
            self.comandos[comando]()

    def desbaste(self):

        def gcode():

            # SEÇÃO DE CONVERSÃO DE ENTRADAs

            ferramenta = entry_ferramenta.get().upper()
            referencia = entry_ref.get().upper()

            # SEÇÃO DE VALIDAÇÃO DE G-CODE

            validacao_code = messagebox.askquestion(title='Compilador G-Code', message='Antes de prosseguir para gerar o G-code, você configurou os posicionamentos da ferramenta corretamente?')

            if validacao_code == 'yes':

                try:
                    diametro_inicial = float(entry_diametroi.get())
                    diametro_final = float(entry_diametrof.get())
                    espessura = float(entry_espessura.get())
                    rotacao = float(entry_rotacao.get())
                    avanco = float(entry_avanco.get())
                    passe = float(entry_passe.get())

                    ciclo_desbaste = CicloDesbaste(diametro_inicial=diametro_inicial, diametro_final=diametro_final, espessura=espessura)

                    ciclo_desbaste.referencia_trabalho(referencia=referencia)
                    ciclo_desbaste.ferramenta(tool=ferramenta)
                    ciclo_desbaste.avanco(advance=avanco)
                    ciclo_desbaste.rotacao(rpm=rotacao)
                    ciclo_desbaste.passe(pf=passe)

                    ciclo_desbaste.pos_segurancaX(self.menu.get_posx)
                    ciclo_desbaste.pos_segurancaZ(self.menu.get_posz)

                except Exception as e:
                    print(f'Erro! {e}')
                    messagebox.showerror(title='Compilador G-Code', message='Por favor, recompile o ciclo e tente novamente.')
                else:
                    ciclo_desbaste.gcode()
            else:
                pass

        # SEÇÃO DE LABELs

        label_diametroi = self.assents.criar_label(text='DIÂMETRO INICIAL', x=15, y=10)
        label_diametrof = self.assents.criar_label(text='DIÂMETRO FINAL', x=15, y=50)

        label_ferramenta = self.assents.criar_label(text='FERRAMENTA', x=15, y=170)
        label_ref = self.assents.criar_label(text='REF. DE TRABALHO', x=15, y=130)

        label_espessura = self.assents.criar_label(text='ESPESSURA', x=500, y=10)
        label_rotacao = self.assents.criar_label(text='ROTAÇÃO', x=500, y=130)

        label_avanco = self.assents.criar_label(text='AVANÇO', x=500, y=170)
        label_passe = self.assents.criar_label(text='PASSE', x=500, y=50)

        label_linha = ctk.CTkLabel(master=self.master, text='ㅤ', image=ButtonHandler.img_linha)
        label_linha.place(x=15, y=95)

        # SEÇÃO DE ENTRYs

        entry_ferramenta = self.assents.criar_entry(x=220, y=170)
        entry_espessura = self.assents.criar_entry(x=640, y=10)

        entry_diametroi = self.assents.criar_entry(x=220, y=10)
        entry_diametrof = self.assents.criar_entry(x=220, y=50)

        entry_rotacao = self.assents.criar_entry(x=640, y=130)
        entry_avanco = self.assents.criar_entry(x=640, y=170)

        entry_passe = self.assents.criar_entry(x=640, y=50)
        entry_ref = self.assents.criar_entry(x=220, y=130)

        # SEÇÃO DE BUTTONs

        button_code = self.assents.criar_button(text='G-CODE', command=gcode, image=ButtonHandler.img_code, x=705, y=355)

    def canais(self):

        def gcode():

            # SEÇÃO DE CONVERSÃO DE ENTRADAs

            ferramenta = entry_ferramenta.get().upper()
            referencia = entry_ref.get().upper()

            # SEÇÃO DE VALIDAÇÃO DE G-CODE

            valida_code = messagebox.askquestion(title='Compilador G-Code', message='Antes de prosseguir para gerar o G-code, você configurou os posicionamentos da ferramenta corretamente?')

            if valida_code == 'yes':

                try:
                    diametro_inicial = float(entry_diametroi.get())
                    diametro_final = float(entry_diametrof.get())
                    espessura = float(entry_espessura.get())
                    rotacao = float(entry_rotacao.get())
                    avanco = float(entry_avanco.get())
                    ncanais = int(entry_ncanais.get())
                    passe = float(entry_passe.get())

                    pos_canais = entry_poscanais.get()

                    ciclo_canal = CicloCanal(diametro_inicial=diametro_inicial, diametro_final=diametro_final, n_canais=ncanais, espessura=espessura, pos_canais=pos_canais)

                    ciclo_canal.passe(pf=passe)
                    ciclo_canal.rotacao(rpm=rotacao)
                    ciclo_canal.avanco(advance=avanco)
                    ciclo_canal.ferramenta(tool=ferramenta)
                    ciclo_canal.referencia_trabalho(referencia=referencia)

                    ciclo_canal.pos_segurancaX(posx=self.menu.get_posx)
                    ciclo_canal.pos_segurancaZ(posz=self.menu.get_posz)

                except Exception as e:
                    print(f'Erro! {e}')
                    messagebox.showerror(title='Compilador G-Code', message='Por favor, recompile o ciclo e tente novamente.')
                else:
                    ciclo_canal.gcode()
            else:
                pass
                
        # SEÇÃO DE LABELs

        label_diametroi = self.assents.criar_label(text='DIÂMETRO INICIAL', x=15, y=10)
        label_diametrof = self.assents.criar_label(text='DIÂMETRO FINAL', x=15, y=50)

        label_ferramenta = self.assents.criar_label(text='FERRAMENTA', x=15, y=170)
        label_ref = self.assents.criar_label(text='REF. DE TRABALHO', x=15, y=130)

        label_poscanais = self.assents.criar_label(text='POS CANAIS', x=500, y=10)
        label_rotacao = self.assents.criar_label(text='ROTAÇÃO', x=500, y=130)

        label_ncanais = self.assents.criar_label(text='N.CANAIS', x=500, y=50)
        label_avanco = self.assents.criar_label(text='AVANÇO', x=500, y=170)

        label_espessura = self.assents.criar_label(text='ESPESSURA', x=15, y=210)
        label_passe = self.assents.criar_label(text='PASSE', x=500, y=210)

        label_linha = ctk.CTkLabel(master=self.master, text='ㅤ', image=ButtonHandler.img_linha)
        label_linha.place(x=15, y=95)

        # SEÇÃO DE ENTRYs

        entry_ferramenta = self.assents.criar_entry(x=220, y=170)
        entry_poscanais = self.assents.criar_entry(x=640, y=10)

        entry_diametroi = self.assents.criar_entry(x=220, y=10)
        entry_diametrof = self.assents.criar_entry(x=220, y=50)

        entry_rotacao = self.assents.criar_entry(x=640, y=130)
        entry_ncanais = self.assents.criar_entry(x=640, y=50)

        entry_avanco = self.assents.criar_entry(x=640, y=170)
        entry_ref = self.assents.criar_entry(x=220, y=130)

        entry_espessura = self.assents.criar_entry(x=220, y=210)
        entry_passe = self.assents.criar_entry(x=640, y=210)

        # SEÇÃO DE BUTTONs

        button_code = self.assents.criar_button(text='G-CODE', command=gcode, image=ButtonHandler.img_code, x=705, y=355)

    def faceamento(self):

        def gcode():

            # SEÇÃO DE CONVERSÃO DE ENTRADAs

            ferramenta = entry_ferramenta.get().upper()
            referencia = entry_ref.get().upper()

            # SEÇÃO DE VALIDAÇÃO DE G-CODE

            valida_code = messagebox.askquestion(title='Compilador G-Code', message='Antes de prosseguir para gerar o G-code, você configurou os posicionamentos da ferramenta corretamente?')

            if valida_code == 'yes':

                try:
                    diametro_inicial = float(entry_diametroi.get())
                    diametro_final = float(entry_diametrof.get())
                    espessura = float(entry_espessura.get())

                    rotacao = float(entry_rotacao.get())
                    avanco = float(entry_avanco.get())
                    passe = float(entry_passe.get())

                    ciclo_faceamento = CicloFaceamento(diametro_inicial=diametro_inicial, diametro_final=diametro_final, espessura=espessura)

                    ciclo_faceamento.referencia_trabalho(referencia=referencia)
                    ciclo_faceamento.ferramenta(tool=ferramenta)
                    ciclo_faceamento.avanco(advance=avanco)
                    ciclo_faceamento.rotacao(rpm=rotacao)
                    ciclo_faceamento.passe(pf=passe)

                    ciclo_faceamento.pos_segurancaX(posx=self.menu.get_posx)
                    ciclo_faceamento.pos_segurancaZ(posz=self.menu.get_posz)
                
                except Exception as e:
                    print(f'Erro! {e}')
                    messagebox.showerror(title='Compilador G-Code', message='Por favor, recompile o ciclo e tente novamente.')
                else:
                    ciclo_faceamento.gcode()
            else:
                pass

        # SEÇÃO DE LABELs

        label_diametroi = self.assents.criar_label(text='DIÂMETRO INICIAL', x=15, y=10)
        label_diametrof = self.assents.criar_label(text='DIÂMETRO FINAL', x=15, y=50)

        label_ferramenta = self.assents.criar_label(text='FERRAMENTA', x=15, y=170)
        label_ref = self.assents.criar_label(text='REF. DE TRABALHO', x=15, y=130)

        label_espessura = self.assents.criar_label(text='ESPESSURA', x=500, y=10)
        label_rotacao = self.assents.criar_label(text='ROTAÇÃO', x=500, y=130)

        label_passe = self.assents.criar_label(text='PASSE', x=500, y=50)
        label_avanco = self.assents.criar_label(text='AVANÇO', x=500, y=170)

        label_linha = ctk.CTkLabel(master=self.master, text='ㅤ', image=ButtonHandler.img_linha)
        label_linha.place(x=15, y=95)

        # SEÇÃO DE ENTRYs

        entry_ferramenta = self.assents.criar_entry(x=220, y=170)
        entry_espessura = self.assents.criar_entry(x=640, y=10)

        entry_diametroi = self.assents.criar_entry(x=220, y=10)
        entry_diametrof = self.assents.criar_entry(x=220, y=50)

        entry_rotacao = self.assents.criar_entry(x=640, y=130)
        entry_passe = self.assents.criar_entry(x=640, y=50)

        entry_avanco = self.assents.criar_entry(x=640, y=170)
        entry_ref = self.assents.criar_entry(x=220, y=130)

        # SEÇÃO DE BUTTONs

        button_code = self.assents.criar_button(text='G-CODE', command=gcode, image=ButtonHandler.img_code, x=705, y=355)