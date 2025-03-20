import textwrap
from tkinter import messagebox
from src.model.cycles.cycle_base import CycleBase

class Desbaste_Funcional(CycleBase):

    def __init__(self, diametro_inicial: float):
        
        if not isinstance(diametro_inicial, float):
            raise ValueError ('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        self.__diametro_inicial = diametro_inicial
        self.__diametro_chanfro = 0
        self.contador = 0

    @property
    def get_diametro_inicial(self):
        return self.__diametro_inicial
    
    @property
    def get_diametro_chanfro(self):
        return self.__diametro_chanfro

    def gerar_coordenadas(self, diametros_finais: str, espessuras: str):

        self.atual_diametros = str(diametros_finais.get())
        self.atual_espessuras = str(espessuras.get())
        self.coordenadas = ''

        self.lista_diametros = list(map(float, self.atual_diametros.split(',')))
        self.lista_espessuras = list(map(float, self.atual_espessuras.split(',')))

        self.__diametro_chanfro = self.lista_diametros[0] - 3

        for cont in self.lista_diametros:
            self.contador += 1

        for coordenada in range(0, self.contador, 1):
            self.coordenadas += (f'\nX{self.lista_diametros[coordenada]}\nZ-{self.lista_espessuras[coordenada]}')

    def gcode(self):
        
        self.gcode_text = textwrap.dedent(f'''
        G291
        G21 G40 G90 G95

        G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        {self.get_ferramenta} M3
        G97 S{self.get_rotacao} M8

        G0 X{self.get_diametro_inicial}
        G0 Z1

        ;GOTOF ACABAMENTO

        G71 U{self.get_passe} R1
        G71 P1 Q2 U1 W0.1 F{self.get_avanco}
        
        N1 G1 X{self.get_diametro_chanfro} Z0''')

        self.gcode_text += self.coordenadas
    
        self.gcode_text += textwrap.dedent(f'''
        N2 X{self.lista_diametros[self.contador - 1]} Z-{self.lista_espessuras[self.contador - 1]}
                                           
        M00; PARADA PROGRAMADA

        ACABAMENTO:

        G70 P1 Q2 F{self.get_avanco}

        G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        M9
        M5
        M30''')

        with open(file='Ciclo de Desbaste (f).txt', mode='w') as file:
            file.write(self.gcode_text)

        messagebox.showinfo(title='Compilador G-Code', message='O ciclo de desbaste (f) foi gerado com sucesso e já está disponível no sistema.')
        print(' - O ciclo de desbaste (f) foi gerado!')