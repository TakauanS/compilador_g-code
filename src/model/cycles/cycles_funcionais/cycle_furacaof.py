import textwrap
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from src.model.cycles.cycle_base import CycleBase

class Furacao_Funcional(CycleBase):

    def __init__(self, position_x: float, position_z: float, espessura: float, passe: float):

        if not isinstance(position_x, float):
            raise ValueError ('O valor da posição do furo no eixo X deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(position_z, float):
            raise ValueError ('O valor da posição do furo no eixo Z deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if not isinstance(espessura, float):
            raise ValueError ('O valor da espessura deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(passe, float):
            raise ValueError ('O valor do passe deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if espessura <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor da espessura deve ser maior que zero (0). Por favor, insira um valor válido.')
            return
        
        if passe <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do passe deve ser maior que zero (0). Por favor, insira um valor válido.')
            return

        self.__position_x = position_x
        self.__position_z = position_z
        self.__espessura = espessura
        self.__passe = passe

    @property
    def get_position_x(self):
        return self.__position_x
    
    @property
    def get_position_z(self):
        return self.__position_z

    @property
    def get_espessura(self):
        return self.__espessura
    
    @property
    def get_passe(self):
        return self.__passe
    
    def gcode(self):

        self.gcode_text = textwrap.dedent(f'''
        N10 G291
        N20 G21 G40 G90 G95

        N30 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N40 {self.get_ferramenta} M3
        N50 G97 S{self.get_rotacao}

        N60 G0 X{self.get_position_x}
        N70 G0 Z{self.get_position_z} M8

        N80 G74 R1
        N90 G74 Z-{self.get_espessura} Q{self.get_passe:.0f} F{self.get_avanco}

        N100 G0 G54 X{self.get_posx} Z{self.get_posz}

        N110 M9
        N120 M5
        N130 M30''')

        arquivo = asksaveasfilename(defaultextension='.txt', filetypes=[('Arquivos de Texto', '*.txt'), ('Todos os Arquivos', '*.*')])

        if arquivo:
            with open(arquivo, mode='w') as file:
                file.write(self.gcode_text)

            messagebox.showinfo(title='Compilador G-Code', message='O ciclo de furação (f) foi gerado com sucesso e já está disponível no sistema.')
            print(' - O ciclo de furação (f) foi gerado!')