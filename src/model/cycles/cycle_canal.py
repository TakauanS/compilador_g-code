import textwrap
from tkinter import messagebox
from src.model.cycles.cycle_base import CycleBase

class CicloCanal(CycleBase):
    
    def __init__(self, diametro_inicial: float, diametro_final: float, n_canais: int, pos_canais):

        if not isinstance(diametro_inicial, float):
            raise ValueError('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(diametro_final, float):
            raise ValueError('O valor do diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(n_canais, int):
            raise ValueError('O valor do número de canais deve ser um número inteiro (int). Por favor, insira um valor válido.')

        if diametro_inicial < diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro inicial não pode ser menor que o diâmetro final. Por favor, insira um valor válido.')
            return

        if n_canais < 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do número de canais não pode ser negativo. Por favor, insira um valor válido.')
            return

        self._diametro_inicial = diametro_inicial
        self._diametro_final = diametro_final
        self._n_canais = n_canais
        self._pos_canais = pos_canais

    @property
    def get_diametro_inicial(self):
        return self._diametro_inicial

    @property
    def get_diametro_final(self):
        return self._diametro_final

    @property
    def get_n_canais(self):
        return self._n_canais

    @property
    def get_pos_canais(self):
        return self._pos_canais

    @get_diametro_inicial.setter
    def set_diametro_inicial(self, novo_diametro_inicial: float):

        if not isinstance(novo_diametro_inicial, float):
            raise ValueError ('O valor do novo diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if novo_diametro_inicial < self._diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro inicial não pode ser menor que o diâmetro final. Por favor, insira valores válidos.')
            return
        else:
            self._diametro_inicial = novo_diametro_inicial

    @get_diametro_final.setter
    def set_diametro_final(self, novo_diametro_final: float):

        if not isinstance(novo_diametro_final, float):
            raise ValueError ('O valor do novo diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if novo_diametro_final > self._diametro_inicial:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro final não pode ser maior que o diâmetro inicial. Por favor, insira valores válidos.')
        else:
            self._diametro_final = novo_diametro_final

    @get_n_canais.setter
    def set_n_canais(self, novo_n_canais: int):

        if novo_n_canais < 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do número de canais não pode ser negativo. Por favor, insira um valor válido.')
        else:
            self._n_canais = novo_n_canais

    @get_pos_canais.setter
    def set_pos_canais(self, novo_pos_canais):
        self._pos_canais = novo_pos_canais

    def gcode(self, nome_arquivo='Ciclo de Canais'):

        gcode_text = textwrap.dedent(f'''
        DEF INT CANAIS[{self.get_n_canais}] = SET ({self.get_pos_canais})
        DEF INT N_CANAIS
        DEF INT C_CANAIS
        DEF INT C_MSG
        
        N10 G290
        N20 G18 G40 G90 G95

        N30 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N40 {self.get_ferramenta} M3
        N50 G97 S{self.get_rotacao} M8

        R1 = {self.get_diametro_inicial};
        R2 = {self.get_diametro_final};

        R3 = 0.5;
        R4 = -0.5;
        R5 = (R1 - R2) - 1;

        R7 = {self.get_n_canais};
        R11 = 0;

        N_CANAIS = (R5 * R7) + R7;
        C_CANAIS = 1;
        C_MSG = 0;

        IF R11 == 0
            MSG("INICIAR CICLO DE DESBASTE? - (CYCLE START)")
            M00
            GOTO N60
        ENDIF

        IF R11 == 1
            MSG("INICIAR CICLO DE ACABAMENTO? - (CYCLE START)")
            M00
            GOTO N100
        ENDIF

        IF NOT R11 <> 0 OR 1
            MSG("ERRO: É NECESSÁRIO INFORMAR NA VARIÁVEL R11 SE O PROCESSO É DE DESBASTE (0) OU ACABAMENTO (1) DOS CANAIS.")
            M00
            M30
        ENDIF

        N60 G0 X=R1 Z0

        FOR R6 = 0 TO (R7 - 1)
            C_MSG = C_MSG + 1
            G1 Z=CANAIS[R6] F{self.get_avanco}
            FOR R9 = 0 TO R5
                MSG("CANAL "<<C_MSG<<" | PASSE DE DESBASTE: "<<C_CANAIS<<" DE "<<N_CANAIS)
                G91
                G1 X=R4 F{self.get_avanco}
                X=R3
                X=R4
                C_CANAIS = C_CANAIS + 1
            ENDFOR
            G90
            G0 X=R1
        ENDFOR

        N70 G90
        N80 G0 X=(R1 + 1)
        N90 Z0

        MSG("INICIAR CICLO DE ACABAMENTO? - (CYCLE START)")
        M00

        N100 ; 
        MSG("CICLO DE ACABAMENTO EM ANDAMENTO...")

        FOR R10 = 0 TO (R7 - 1)
            G1 Z=CANAIS[R10] F{self.get_avanco}
            X=R2
            X=R1
        ENDFOR

        MSG("")
        N100 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N120 M9
        N130 M5
        N140 M30''')

        with open(f'{nome_arquivo}.txt', "w") as arquivo:
            arquivo.write(gcode_text)

        messagebox.showinfo(title='Compilador G-Code', message='O ciclo de canais foi gerado com sucesso e já está disponível no sistema.')
        print('- O seu ciclo de canais foi gerado!')
