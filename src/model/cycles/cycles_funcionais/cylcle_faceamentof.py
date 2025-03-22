from src.model.cycles.cycle_base import CycleBase
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import textwrap

class Faceamento_Funcional(CycleBase):

    def __init__(self, diametro_inicial: float, diametro_final: float, espessura: float):

        if not isinstance(diametro_inicial, float):
            raise ValueError ('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(diametro_final, float):
            raise ValueError ('O valor do diâmetro final deve ser informado como um número decimal (float), Por favor, insira o um valor válido.')

        if not isinstance(espessura, float):
            raise ValueError ('O valor da espessura deve ser do tipo decimal (float). Por favor, insira um valor válido.')
        
        if diametro_inicial <= diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro inicial não pode ser menor ou igual ao diâmetro final. Por favor, insira um valor válido.')
            return

        if espessura <= 0:
            messagebox.showerror(title='Compilador G-Code', message='A espessura não pode ser menor ou igual a zero. Por favor, insira um valor válido.')
            return

        self.__diametro_inicial = diametro_inicial
        self.__diametro_final = diametro_final
        self.__espessura = espessura

        self.__dist_diametro_inicial = self.__diametro_inicial + 3 # Retorna a coordenada de aproximação em X

    @property
    def get_diametro_inicial(self):
        return self.__diametro_inicial
    
    @property
    def get_diametro_final(self):
        return self.__diametro_final
    
    @property
    def get_dist_diametro_inicial(self):
        return self.__dist_diametro_inicial

    @property
    def get_espessura(self):
        return self.__espessura
    
    def gcode(self):

        self.gcode_text = textwrap.dedent(f'''
        N20 G291
        N30 G21 G40 G90 G95

        N40 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N50 {self.get_ferramenta} M3
        N60 G97 S{self.get_rotacao}

        N70 G0 X{self.get_dist_diametro_inicial}
        N80 G0 Z0

        ;GOTOF ACABAMENTO

        N90 G72 W{self.get_passe} R1
        N100 G72 P110 Q130 U0.1 W0.1 F{self.get_avanco}

        N110 G1 Z-{self.get_espessura}
        N120 X{self.get_diametro_final}
        N130 X0 Z-{self.get_espessura}

        N140 M00 ; PARADA PROGRAMADA

        N150 ACABAMENTO:

        N160 G70 P110 Q130 F{self.get_avanco};

        N170 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N180 M9
        N190 M5
        N200 M30''')

        arquivo = asksaveasfilename(defaultextension='.txt', filetypes=[('Arquivos de Texto', '*.txt'), ('Todos os Arquivos', '*.*')])

        if arquivo:
            with open(arquivo, mode='w') as file:
                file.write(self.gcode_text)

            messagebox.showinfo(title='Compilador G-Code', message='O ciclo de faceamento (f) foi gerado com sucesso e já está disponível no sistema.')
            print(' - O ciclo de faceamento (f) foi gerado!')