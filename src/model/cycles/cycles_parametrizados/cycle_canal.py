import textwrap
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from src.model.cycles.cy_base import CycleBase

class Canal_Parametrizado(CycleBase):
    
    def __init__(self, diametro_inicial: float, profundidade_canal: float, n_canais: int, espessura: float, pos_canais):

        if not isinstance(diametro_inicial, float):
            raise ValueError('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(profundidade_canal, float):
            raise ValueError('O valor da profundidade do canal deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(n_canais, int):
            raise ValueError('O valor do número de canais deve ser um número inteiro (int). Por favor, insira um valor válido.')

        if not isinstance(espessura, float):
            raise ValueError ('O valor da espessura deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if espessura <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor da espessura (abertura) do canal deve ser maior que zero. Por favor, verifique e tente novamente!')
            return

        if n_canais < 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do número de canais não pode ser negativo. Por favor, insira um valor válido.')
            return

        self.__profundidade_canal = profundidade_canal
        self.__diametro_inicial = diametro_inicial
        self.__pos_canais = pos_canais
        self.__espessura = espessura
        self.__n_canais = n_canais

    @property
    def get_profundidade_canal(self):
        return self.__profundidade_canal

    @property
    def get_diametro_inicial(self):
        return self.__diametro_inicial

    @property
    def get_n_canais(self):
        return self.__n_canais

    @property
    def get_espessura(self):
        return self.__espessura

    @property
    def get_pos_canais(self):
        return self.__pos_canais

    def gcode(self, nome_arquivo='Ciclo de Canais'):

        self.gcode_text = textwrap.dedent(f'''
        DEF INT POS_CANAIS [{self.get_n_canais}] = SET ({self.get_pos_canais})

        N10 G290
        N20 G18 G40 G90 G95

        N30 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N40 {self.get_ferramenta} M3
        N50 G97 S{self.get_rotacao} M8

        R1 = {self.get_diametro_inicial}
        R2 = {self.get_profundidade_canal}
        R3 = {self.get_espessura}

        R4 = -{self.get_passe}
        R5 = ABS(R4)
        R6 = {self.get_n_canais}

        R8 = 0
        R9 = 0

        R10 = 0
        R11 = R1

        IF R10 == 0
            MSG("CICLO DE CANAIS EM ANDAMENTO (DBT)...")
            GOTO N60
        ENDIF

        IF R10 == 1
            GOTO N80
        ENDIF

        N60 G0 X=R1
        N70 G0 Z0

        FOR R8 = 0 TO R6 - 1
            G90
            G0 X=R1
            G0 Z=POS_CANAIS[R8]
            R7 = (R1 + R2) - R5
            R11 = R1
            WHILE R7 > R11
                G91
                G1 X=R4 F{self.get_avanco}
                Z=R3
                G0 X=ABS(R4)
                G0 Z=ABS(R3)
                G1 X=R4 F{self.get_avanco}
                R11 = R11 + R5
            ENDWHILE
        ENDFOR

        N80 G90
        N90 G0 X=(R1 + 1)
        N100 G0 Z0

        MSG("INICIAR O ACABAMENTO DOS CANAIS? - CYCLE START")
        M00
        MSG("CICLO DE CANAIS EM ANDAMENTO (ACB)...")

        FOR R9 = 0 TO R6 - 1
            G90
            G0 X=R1
            G0 Z=POS_CANAIS[R9]
            G1 X=(R1 - R2) F{self.get_avanco}
            G91 Z=R3
            G90 X=R1
        ENDFOR

        MSG("")

        N110 G0 X=(R1 + 1)
        N120 G0 Z0

        N130 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N140 M9
        N150 M5
        N160 M30''')

        arquivo = asksaveasfilename(defaultextension='.txt', filetypes=[('Arquivos de Texto', '*.txt'), ('Todos os Arquivos', '*.*')])

        if arquivo:
            with open(arquivo, mode='w') as file:
                file.write(self.gcode_text)

            messagebox.showinfo(title='Compilador G-Code', message='O ciclo de canal (p) foi gerado com sucesso e já está disponível no sistema.')
            print(' - O seu ciclo de canais foi gerado!')