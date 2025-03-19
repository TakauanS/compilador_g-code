import textwrap
from tkinter import messagebox
from src.model.cycles.cycle_base import CycleBase

class Furacao_Parametrizado(CycleBase):

    def __init__(self, position_x: float, position_z: float, espessura: float, passe: float):

        if not isinstance(position_z, float):
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

        if passe > 3:
            messagebox.showerror(title='Compilador G-Code', message='O valor do passe não pode ser maior que 3. Por favor, tente novamente um valor válido.')
            return

        if passe <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do passe deve ser maior que zero (0). Por favor, insira um valor válido.')

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

        gcode_text = textwrap.dedent(f'''
        DEF INT I_PASSES
        DEF INT F_PASSES

        N10 G290
        N20 G18 G40 G90 G95

        N30 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N40 {self.get_ferramenta} M3
        N50 G97 S{self.get_rotacao}

        R1 = {self.get_position_x}
        R2 = {self.get_position_z} 

        R3 = -{self.get_passe}
        R4 = -{self.get_espessura}

        R6 = ABS(R4)
        R7 = ABS(R3)

        R9 = R6 / R7
        R10 = ABS(R3)

        I_PASSES = 1
        F_PASSES = R9

        IF R10 == 3
            R10 = 1
        ENDIF

        IF R10 == 2.5
            R10 = 2
        ENDIF

        IF R10 > 3
            MSG("ERRO! PRESSIONE CYCLE START...")
            M00
            M30
        ENDIF

        N60 G0 X=R1
        N70 G0 Z=R2
        N80 G0 Z0

        FOR R5 = 0 TO (R9 - R10)
            MSG("PASSE DE DESBASTE: "<<I_PASSES<<" DE "<<F_PASSES)
            G91
            G1 Z=R3 F1
            G0 Z=R7
            G1 Z=R3 F1
            I_PASSES = I_PASSES + 1
        ENDFOR

        N90 G90
        N100 G1 Z=R4

        MSG("")

        N110 G90
        N120 G0 X=R1
        N130 G0 Z=R2

        N140 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N150 M9
        N160 M5
        N170 M30''')

        with open(file='Ciclo de furação (p).txt', mode='w') as file:
            file.write(gcode_text)

        messagebox.showinfo(title='Compilador G-Code', message='O ciclo de furação (p) foi gerado com sucesso e já está disponível no sistema.')
        print(' - O ciclo de furação (p) foi gerado!')  