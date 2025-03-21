from src.controller.gcode_generator.cycles_parametrizados.gcode_faceamentop import Gcode_FaceamentoP
from src.model.assents import Assents
from src.controller.menu import Menu
from tkinter import messagebox

class FaceamentoP_Manager:

    def __init__(self, master):

        self.master = master
        self.menu = Menu(root=self.master)
        self.__assents = Assents(master=self.master)

        # SEÇÃO DE LABELs

        self.label_diametroi = self.__assents.criar_label(text='DIÂMETRO INICIAL', x=15, y=10)
        self.label_diametrof = self.__assents.criar_label(text='DIÂMETRO FINAL', x=15, y=50)

        self.label_ferramenta = self.__assents.criar_label(text='FERRAMENTA', x=15, y=170)
        self.label_ref = self.__assents.criar_label(text='REF. DE TRABALHO', x=15, y=130)

        self.label_espessura = self.__assents.criar_label(text='ESPESSURA', x=500, y=10)
        self.label_rotacao = self.__assents.criar_label(text='ROTAÇÃO', x=500, y=130)

        self.label_passe = self.__assents.criar_label(text='PASSE', x=500, y=50)
        self.label_avanco = self.__assents.criar_label(text='AVANÇO', x=500, y=170)

        self.label_posx = self.__assents.criar_label(text='PS.SEGURANÇA (X)', x=15, y=245)
        self.label_posz = self.__assents.criar_label(text='PS.SEGURANÇA (Z)', x=15, y=285)

        self.__assents.criar_linha(x=15, y=95)
        self.__assents.criar_linha(x=15, y=210)

        # SEÇÃO DE ENTRYs

        self.entry_ferramenta = self.__assents.criar_entry(x=220, y=170)
        self.entry_espessura = self.__assents.criar_entry(x=640, y=10)

        self.entry_diametroi = self.__assents.criar_entry(x=220, y=10)
        self.entry_diametrof = self.__assents.criar_entry(x=220, y=50)

        self.entry_rotacao = self.__assents.criar_entry(x=640, y=130)
        self.entry_passe = self.__assents.criar_entry(x=640, y=50)

        self.entry_avanco = self.__assents.criar_entry(x=640, y=170)
        self.entry_ref = self.__assents.criar_entry(x=220, y=130)

        self.entry_posx = self.__assents.criar_entry(x=220, y=245)
        self.entry_posz = self.__assents.criar_entry(x=220, y=285)

        # SEÇÃO DE BUTTONs

        self.button_code = self.__assents.criar_button(text='G-CODE', command=self.gcode_faceamento, image=self.__assents.img_code, x=705, y=355)

    def gcode_faceamento(self):

        if self.entry_diametroi.get() == '' or self.entry_diametrof.get() == '':
            messagebox.showerror(title='Compilador G-Code', message='Os valores de diâmetro inicial e diâmetro final devem ser informados para garantir o correto funcionamento do ciclo.')   
        else:
            validacao_diametro = messagebox.askquestion(title='Compilador G-Code', message=f'O diâmetro inicial atual é {self.entry_diametroi.get()}mm. O diâmetro final desejado é realmente {self.entry_diametrof.get()}mm?')

            if validacao_diametro == 'yes':

                try:
                    diametro_inicial = float(self.entry_diametroi.get())
                    diametro_final = float(self.entry_diametrof.get())
                    espessura = float(self.entry_espessura.get())
                    rotacao = float(self.entry_rotacao.get())
                    avanco = float(self.entry_avanco.get())
                    passe = float(self.entry_passe.get())

                    posx = float(self.entry_posx.get())
                    posz = float(self.entry_posz.get())

                    ferramenta = self.entry_ferramenta.get().upper()
                    referencia = self.entry_ref.get().upper()

                    ciclo_faceamento = Gcode_FaceamentoP(diametro_inicial, diametro_final, espessura, rotacao, avanco, passe, referencia, ferramenta, posx, posz)

                except Exception as e:
                    print(f' - Erro! {e}')
                else:
                    ciclo_faceamento.gerar_gcode()