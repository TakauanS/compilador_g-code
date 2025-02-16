import textwrap
from tkinter import messagebox
from src.model.cycles.cycle_base import CycleBase

class Desbaste_Funcional(CycleBase):

    def __init__(self, diametro_inicial: float, diametro_final: float, espessura: float):
        
        if not isinstance(diametro_inicial, float):
            raise ValueError ('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(diametro_final, float):
            raise ValueError ('O valor do diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(espessura, float):
            raise ValueError ('O valor da espessura deve ser do tipo decimal (float). Por favor, insira um valor válido.')

        if diametro_inicial < diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro inicial não pode ser menor que o diâmetro final. Por favor, insira um valor válido.')
            return
        
        if espessura <= 0:
            messagebox.showerror(title='Compilador G-Code', message='A espessura não pode ser menor ou igual a zero. Por favor, insira um valor válido.')
            return

        self.__diametro_inicial = diametro_inicial
        self.__diametro_final = diametro_final
        self.__espessura = espessura

        self.__diametro_chanfro = self.get_diametro_final - 2

    @property
    def get_diametro_inicial(self):
        return self.__diametro_inicial
    
    @property
    def get_diametro_final(self):
        return self.__diametro_final
    
    @property
    def get_espessura(self):
        return self.__espessura

    @property
    def get_diametro_chanfro(self):
        return self.__diametro_chanfro

    @get_diametro_inicial.setter
    def set_diametro_inicial(self, novo_diametro_inicial: float):

        if not isinstance(novo_diametro_inicial, float):
            raise ValueError ('O valor do novo diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if novo_diametro_inicial < self.__diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro inicial não pode ser menor que o diâmetro final. Por favor, insira um valor válido.')
            return
        else:
            self.__diametro_inicial = novo_diametro_inicial

    @get_diametro_final.setter
    def set_diametro_final(self, novo_diametro_final: float):

        if not isinstance(novo_diametro_final, float):
            raise ValueError ('O valor do novo diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if novo_diametro_final > self.__diametro_inicial:
            messagebox.showerror(title='Compilador G-Code', message='O novo diâmetro final não pode ser maior que o diâmetro inicial. Por favor, insira um valor válido.')
            return
        else:
            self.__diametro_final = novo_diametro_final 

    @get_espessura.setter
    def set_espessura(self, nova_espessura: float):

        if not isinstance(nova_espessura, float):
            raise ValueError ('O valor da nova espessura deve ser do tipo decimal (float). Por favor, insira um valor válido.')
        
        if nova_espessura < 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor da espessura deve ser maior que zero. Por favor, insira um valor válido.')
            return
        else:
            self.__espessura = nova_espessura

    def gcode(self):
        
        gcode_text = textwrap.dedent(f'''
        N10 G291
        N20 G21 G40 G90 G95

        N30 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N40 {self.get_ferramenta} M3
        N50 G97 S{self.get_rotacao} M8

        N60 G0 X{self.get_diametro_inicial}
        N70 G0 Z1

        ;GOTOF ACABAMENTO

        N80 G71 U{self.get_passe} R1
        N90 G71 P100 Q130 U1 W0.1 F{self.get_avanco}

        N100 G1 X{self.get_diametro_chanfro} Z0
        N110 X{self.get_diametro_final} ,C2
        N120 Z-{self.get_espessura}
        N130 X{self.get_diametro_final} Z-{self.get_espessura}

        N140 M00; PARADA PROGRAMADA

        ACABAMENTO:

        N150 G70 P100 Q130 F{self.get_avanco}

        N160 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N170 M9
        N180 M5
        N190 M30''')

        with open(file='Ciclo de Desbaste (f).txt', mode='w') as file:
            file.write(gcode_text)

        messagebox.showinfo(title='Compilador G-Code', message='O ciclo de desbaste (f) foi gerado com sucesso e já está disponível no sistema.')
        print(' - O ciclo de desbaste (f) foi gerado!')