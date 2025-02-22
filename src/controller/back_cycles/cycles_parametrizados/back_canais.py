from src.model.cycles.cycles_parametrizados.cycle_canal import Canal_Parametrizado
from src.model.assents import Assents
from src.controller.menu import Menu
from tkinter import messagebox

class BackCanais:

    def __init__(self, master):

        self.master = master
        self.menu = Menu(root=self.master)
        self.__assents = Assents(master=self.master)

        # SEÇÃO DE LABELs

        label_diametroi = self.__assents.criar_label(text='DIÂMETRO INICIAL', x=15, y=10)
        label_profundidade = self.__assents.criar_label(text='PROFUND.CANAL', x=15, y=50)

        label_ferramenta = self.__assents.criar_label(text='FERRAMENTA', x=15, y=170)
        label_ref = self.__assents.criar_label(text='REF. DE TRABALHO', x=15, y=130)

        label_poscanais = self.__assents.criar_label(text='POS CANAIS', x=500, y=10)
        label_rotacao = self.__assents.criar_label(text='ROTAÇÃO', x=500, y=130)

        label_ncanais = self.__assents.criar_label(text='N.CANAIS', x=500, y=50)
        label_avanco = self.__assents.criar_label(text='AVANÇO', x=500, y=170)

        label_espessura = self.__assents.criar_label(text='ESPESSURA', x=15, y=210)
        label_passe = self.__assents.criar_label(text='PASSE', x=500, y=210)

        label_posx = self.__assents.criar_label(text='PS.SEGURANÇA (X)', x=15, y=290)
        label_posz = self.__assents.criar_label(text='PS.SEGURANÇA (Z)', x=15, y=330)

        self.__assents.criar_linha(x=15, y=95)
        self.__assents.criar_linha(x=15, y=255)

        # SEÇÃO DE ENTRYs

        self.entry_profundidade = self.__assents.criar_entry(x=220, y=50)
        self.entry_ferramenta = self.__assents.criar_entry(x=220, y=170)

        self.entry_poscanais = self.__assents.criar_entry(x=640, y=10)
        self.entry_diametroi = self.__assents.criar_entry(x=220, y=10)

        self.entry_rotacao = self.__assents.criar_entry(x=640, y=130)
        self.entry_ncanais = self.__assents.criar_entry(x=640, y=50)

        self.entry_avanco = self.__assents.criar_entry(x=640, y=170)
        self.entry_ref = self.__assents.criar_entry(x=220, y=130)

        self.entry_espessura = self.__assents.criar_entry(x=220, y=210)
        self.entry_passe = self.__assents.criar_entry(x=640, y=210)

        self.entry_posx = self.__assents.criar_entry(x=220, y=290)
        self.entry_posz = self.__assents.criar_entry(x=220, y=330)

        # SEÇÃO DE BUTTONs

        self.button_code = self.__assents.criar_button(text='G-CODE', command=self.gcode_canais, image=self.__assents.img_code, x=705, y=355)

    def gcode_canais(self):

        if self.entry_diametroi.get() == '':
            messagebox.showerror(title='Compilador G-Code', message='Os valores de diâmetro inicial devem ser informados para garantir o correto funcionamento do ciclo.')   
        else:
            validacao_diametro = messagebox.askquestion(title='Compilador G-Code', message=f'O diâmetro inicial atual é {self.entry_diametroi.get()}mm. A profundidade do canal é realmente {self.entry_profundidade.get()}mm?')

            if validacao_diametro == 'yes':

                try:
                    diametro_inicial = float(self.entry_diametroi.get())
                    profundidade = float(self.entry_profundidade.get())
                    espessura = float(self.entry_espessura.get())
                    rotacao = float(self.entry_rotacao.get())
                    ncanais = int(self.entry_ncanais.get())
                    avanco = float(self.entry_avanco.get())
                    passe = float(self.entry_passe.get())

                    posx = float(self.entry_posx.get())
                    posz = float(self.entry_posz.get())

                    ferramenta = self.entry_ferramenta.get().upper()
                    referencia = self.entry_ref.get().upper()
                    poscanais = self.entry_poscanais.get()

                    ciclo_canal = Canal_Parametrizado(diametro_inicial=diametro_inicial, profundidade_canal=profundidade, n_canais=ncanais, espessura=espessura, pos_canais=poscanais)

                    ciclo_canal.referencia_trabalho(referencia=referencia)
                    ciclo_canal.ferramenta(tool=ferramenta)
                    ciclo_canal.avanco(advance=avanco)
                    ciclo_canal.rotacao(rpm=rotacao)
                    ciclo_canal.passe(pf=passe)       

                    ciclo_canal.pos_segurancaX(posx=posx)
                    ciclo_canal.pos_segurancaZ(posz=posz)

                except Exception as e:
                    print(f' - Error! {e}')
                else:
                    ciclo_canal.gcode()
            else:
                pass