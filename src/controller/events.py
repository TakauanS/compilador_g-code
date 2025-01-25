from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(base_dir)

from src.model.cycles import CicloDesbaste, CicloCanal
from src.model.menu import Menu

class ButtonHandler:

    # SEÇÃO DE EXPORTAÇÃO DE IMAGEs

    img_linha = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/linha.png'), size=(825, 20))
    img_code = ctk.CTkImage(Image.open('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/code.png'), size=(20, 20))

    # SEÇÃO DE COREs

    cor1 = '#1C1A1B' # Cor preta para bg_color - Mais Forte
    cor2 = '#333031' # Cor preta para fg_color - Mais fraca
    cor3 = '#737277' # Cor cinza para placeholder
    cor4 = '#2E53F2' # Cor azul para butões
    cor5 = '#3757A0' # Cor azul para botões - hover color
    cor6 = 'white'   # Cor branca para textos

    def __init__(self, master):

        self.master = master
        self.menu = Menu(self.master)
        
        self.comandos = {
            "! compile -c: desbaste": self.desbaste,
            "! compile -c: canais": self.canais
        }

    def executar_comando(self, comando):

        if comando not in self.comandos:
            msg = messagebox.showerror(title='Compilador G-Code', message='O comando informado não existe no sistema. Por favor, verifique e tente novamente.')

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

                    ciclo_desbaste = CicloDesbaste(diametro_inicial=diametro_inicial, diametro_final=diametro_final, espessura=espessura, passe=passe)

                    ciclo_desbaste.ferramenta(tool=ferramenta)
                    ciclo_desbaste.avanco(advance=avanco)
                    ciclo_desbaste.rotacao(rpm=rotacao)
                    ciclo_desbaste.referencia_trabalho(ref=referencia)

                    ciclo_desbaste.trocax_pos(trocax=self.menu.get_trocax)
                    ciclo_desbaste.trocaz_pos(trocaz=self.menu.get_trocaz)
                    ciclo_desbaste.afastx_pos(afastx=self.menu.get_afastx)
                    ciclo_desbaste.afastz_pos(afastz=self.menu.get_afastz)

                except Exception as e:
                    print(f'Erro! {e}')
                    msg = messagebox.showerror(title='Compilador G-Code', message='Por favor, recompile o ciclo e tente novamente.')
                else:
                    ciclo_desbaste.gcode()
                    msg = messagebox.showinfo(title='Compilador G-Code', message='O ciclo de desbaste foi concluído com sucesso e já está salvo em seus arquivos.')
            else:
                pass

        # SEÇÃO DE LABELs

        label_diametroi = ctk.CTkLabel(master=self.master, text='DIÂMETRO INICIAL', font=('Corbel', 23), text_color='white')
        label_diametroi.place(x=15, y=10)

        label_diametrof = ctk.CTkLabel(master=self.master, text='DIÂMETRO FINAL', font=('Corbel', 23), text_color='white')
        label_diametrof.place(x=15, y=50)

        label_espessura = ctk.CTkLabel(master=self.master, text='ESPESSURA', font=('Corbel', 23), text_color='white')
        label_espessura.place(x=500, y=10)

        label_passe = ctk.CTkLabel(master=self.master, text='PASSE', font=('Corbel', 23), text_color='white')
        label_passe.place(x=500, y=50)

        label_ref = ctk.CTkLabel(master=self.master, text='REF. DE TRABALHO', font=('Corbel', 23), text_color='white')
        label_ref.place(x=15, y=130)

        label_ferramenta = ctk.CTkLabel(master=self.master, text='FERRAMENTA', font=('Corbel', 23), text_color='white')
        label_ferramenta.place(x=15, y=170)

        label_rotacao = ctk.CTkLabel(master=self.master, text='ROTAÇÃO', font=('Corbel', 23), text_color='white')
        label_rotacao.place(x=500, y=130)

        label_avanco = ctk.CTkLabel(master=self.master, text='AVANÇO', font=('Corbel', 23), text_color='white')
        label_avanco.place(x=500, y=170)

        label_linha = ctk.CTkLabel(master=self.master, text='ㅤ', image=ButtonHandler.img_linha)
        label_linha.place(x=15, y=95)

        # SEÇÃO DE ENTRYs

        entry_diametroi = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_diametroi.place(x=220, y=10)

        entry_diametrof = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_diametrof.place(x=220, y=50)

        entry_espessura = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_espessura.place(x=640, y=10)

        entry_passe = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_passe.place(x=640, y=50)

        entry_ref = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_ref.place(x=220, y=130)

        entry_ferramenta = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_ferramenta.place(x=220, y=170)

        entry_rotacao = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_rotacao.place(x=640, y=130)

        entry_avanco = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_avanco.place(x=640, y=170)

        # SEÇÃO DE BUTTONs

        button_pos = ctk.CTkButton(master=self.master, command=gcode, height=35, corner_radius=12, text='G-CODE', font=('Arial', 15, 'bold'), image=ButtonHandler.img_code, bg_color=ButtonHandler.cor2, fg_color=ButtonHandler.cor4, hover_color=ButtonHandler.cor5)
        button_pos.place(x=705, y=355)

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
                    rotacao = float(entry_rotacao.get())
                    avanco = float(entry_avanco.get())
                    ncanais = int(entry_ncanais.get())

                    pos_canais = entry_poscanais.get()

                    ciclo_canal = CicloCanal(diametro_inicial=diametro_inicial, diametro_final=diametro_final, n_canais=ncanais, pos_canais=pos_canais)

                    ciclo_canal.rotacao(rpm=rotacao)
                    ciclo_canal.avanco(advance=avanco)
                    ciclo_canal.ferramenta(tool=ferramenta)
                    ciclo_canal.referencia_trabalho(ref=referencia)

                    ciclo_canal.trocax_pos(trocax=self.menu.get_trocax)
                    ciclo_canal.trocaz_pos(trocaz=self.menu.get_trocaz)
                    ciclo_canal.afastx_pos(afastx=self.menu.get_afastx)
                    ciclo_canal.afastz_pos(afastz=self.menu.get_afastz)

                except Exception as e:
                    print(f'Erro! {e}')
                    msg = messagebox.showerror(title='Compilador G-Code', message='Por favor, recompile o ciclo e tente novamente.')
                else:
                    ciclo_canal.gcode()
                    msg = messagebox.showinfo(title='Compilador G-Code', message='O ciclo de canais foi concluído com sucesso e já está salvo em seus arquivos.')
            else:
                pass
                
        # SEÇÃO DE LABELs

        label_diametroi = ctk.CTkLabel(master=self.master, text='DIÂMETRO INICIAL', font=('Corbel', 23), text_color='white')
        label_diametroi.place(x=15, y=10)

        label_diametrof = ctk.CTkLabel(master=self.master, text='DIÂMETRO FINAL', font=('Corbel', 23), text_color='white')
        label_diametrof.place(x=15, y=50)

        label_poscanais = ctk.CTkLabel(master=self.master, text='POS CANAIS', font=('Corbel', 23), text_color='white')
        label_poscanais.place(x=500, y=10)

        label_ncanais = ctk.CTkLabel(master=self.master, text='N.CANAIS', font=('Corbel', 23), text_color='white')
        label_ncanais.place(x=500, y=50)

        label_ref = ctk.CTkLabel(master=self.master, text='REF. DE TRABALHO', font=('Corbel', 23), text_color='white')
        label_ref.place(x=15, y=130)

        label_ferramenta = ctk.CTkLabel(master=self.master, text='FERRAMENTA', font=('Corbel', 23), text_color='white')
        label_ferramenta.place(x=15, y=170)

        label_rotacao = ctk.CTkLabel(master=self.master, text='ROTAÇÃO', font=('Corbel', 23), text_color='white')
        label_rotacao.place(x=500, y=130)

        label_avanco = ctk.CTkLabel(master=self.master, text='AVANÇO', font=('Corbel', 23), text_color='white')
        label_avanco.place(x=500, y=170)

        label_linha = ctk.CTkLabel(master=self.master, text='ㅤ', image=ButtonHandler.img_linha)
        label_linha.place(x=15, y=95)

        # SEÇÃO DE ENTRYs

        entry_diametroi = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_diametroi.place(x=220, y=10)

        entry_diametrof = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_diametrof.place(x=220, y=50)

        entry_poscanais = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_poscanais.place(x=640, y=10)

        entry_ncanais = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_ncanais.place(x=640, y=50)

        entry_ref = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_ref.place(x=220, y=130)

        entry_ferramenta = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_ferramenta.place(x=220, y=170)

        entry_rotacao = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_rotacao.place(x=640, y=130)

        entry_avanco = ctk.CTkEntry(master=self.master, width=200, corner_radius=12, font=('Consola', 16))
        entry_avanco.place(x=640, y=170)

        # SEÇÃO DE BUTTONs

        button_pos = ctk.CTkButton(master=self.master, command=gcode, height=35, corner_radius=12, text='G-CODE', font=('Arial', 15, 'bold'), image=ButtonHandler.img_code, bg_color=ButtonHandler.cor2, fg_color=ButtonHandler.cor4, hover_color=ButtonHandler.cor5)
        button_pos.place(x=705, y=355)