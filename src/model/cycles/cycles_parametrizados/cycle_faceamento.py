import textwrap
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from src.model.cycles.cy_base import CycleBase

class Faceamento_Parametrizado(CycleBase):

    def __init__(self, diametro_inicial: float, diametro_final: float, espessura: float):

        if not isinstance(diametro_inicial, float):
            raise ValueError ('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(diametro_final, float):
            raise ValueError ('O valor do diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(espessura, float):
            raise ValueError ('O valor da espessura deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if diametro_inicial < diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro inicial não pode ser menor que o diâmetro final. Por favor, insira um valor válido.')
            return

        if espessura <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor da espessura deve ser maior que zero. Por favor, verifique e tente novamente!')
            return

        self.__diametro_inicial = diametro_inicial
        self.__diametro_final = diametro_final
        self.__espessura = espessura

    @property
    def get_diametro_inicial(self):
        return self.__diametro_inicial
    
    @property
    def get_diametro_final(self):
        return self.__diametro_final
    
    @property
    def get_espessura(self):
        return self.__espessura

    def gcode(self, nome_arquivo='Ciclo de Faceamento'):

        self.gcode_text = textwrap.dedent(f'''
        N10 G290
        N20 G18 G40 G90 G95

        N30 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N40 {self.get_ferramenta} M3
        N50 G97 S{self.get_rotacao} M8

        R1 = {self.get_diametro_inicial}
        R2 = {self.get_diametro_final}
        R3 = -{self.get_espessura}

        R4 = -{self.get_passe}
        R5 = 0
        R6 = ABS(R3) / ABS(R4)

        R7 = 0

        IF R7 == 0
            MSG("CICLO DE FACEAMENTO EM ANDAMENTO (DBT)...")
            GOTO N60
        ENDIF

        IF R7 == 1
            MSG("CICLO DE FACEAMENTO EM ANDAMENTO (ACB)...")
            GOTO N110
        ENDIF

        N60 G0 X=(R1 + 1) 
        N70 G0 Z0

        WHILE R5 < R6
        G90 G1 X=R2 F{self.get_avanco}
        X=R1
        G91 Z=R4
        R5 = R5 + 1
        ENDWHILE

        N80 G90
        N90 G0 X=(R1 + 1) 
        N100 G0 Z0

        MSG("INICIAR CICLO DE FACEAMENTO (ACB)? - CYCLE START")

        M00

        MSG("")
        MSG("CICLO DE FACEAMENTO EM ANDAMENTO (ACB)...")

        N110 G1 Z=R3 F{self.get_avanco}
        N120 X=R2
        N130 G0 Z=(R3 + 1)

        MSG("")

        N140 G0 G54 X400 Z1

        N150 M9
        N160 M5
        N170 M30''')

        arquivo = asksaveasfilename(defaultextension='.txt', filetypes=[('Arquivos de Texto', '*.txt'), ('Todos os Arquivos', '*.*')])

        if arquivo:
            with open(arquivo, mode='w') as file:
                file.write(self.gcode_text)

            messagebox.showinfo(title='Compilador G-Code', message='O ciclo de faceamento (p) foi gerado com sucesso e já está disponível no sistema.')
            print(' - O seu ciclo de faceamento foi gerado!')