import textwrap
from tkinter import messagebox
from src.model.cycle_base import CycleBase

class CicloDesbaste(CycleBase):

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

        self._diametro_inicial = diametro_inicial
        self._diametro_final = diametro_final
        self._espessura = espessura

    @property
    def get_diametro_inicial(self):
        return self._diametro_inicial

    @property
    def get_diametro_final(self):
        return self._diametro_final
    
    @property
    def get_espessura(self):
        return self._espessura

    @get_diametro_inicial.setter
    def set_diametro_inicial(self, novo_diametro_inicial: float):

        if not isinstance(novo_diametro_inicial, float):
            raise ValueError ('O valor do novo diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if novo_diametro_inicial < self._diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O novo diâmetro não pode ser menor que o diâmetro final. Por favor, insira um valor válido.')
            return
        else:
            self._diametro_inicial = novo_diametro_inicial
            return self._diametro_inicial
    
    @get_diametro_final.setter
    def set_diametro_final(self, novo_diametro_final: float):

        if not isinstance(novo_diametro_final, float):
            raise ValueError ('O valor do novo diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if novo_diametro_final > self._diametro_inicial:
            messagebox.showerror(title='Compilador G-Code', message='O novo diâmetro final não pode ser maior que o diâmetro inicial. Por favor, insira um valor válido.')
            return
        else:
            self._diametro_final = novo_diametro_final
            return self._diametro_final
    
    @get_espessura.setter
    def set_espessura(self, nova_espessura: float):

        if not isinstance(nova_espessura, (float, int)):
            raise ValueError ('O valor da nova espessura deve ser do tipo decimal (float). Por favor, insira um valor válido.')
        
        if nova_espessura < 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor da espessura deve ser maior que zero. Por favor, insira um valor válido.')
            return
        else:
            self._espessura = nova_espessura
            return self._espessura 

    def gcode(self):

        gcode_text = textwrap.dedent(f'''
        DEF INT N_PASSES
        DEF INT C_PASSES

        N10 G290
        N20 G18 G40 G90 G95

        N30 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N40 {self.get_ferramenta} M3
        N50 G97 S{self.get_rotacao}

        R1 = {self.get_diametro_inicial}
        R2 = {self.get_diametro_final}
        R3 = -{self.get_espessura}

        R4 = -{self.get_passe}
        R5 = ABS(R4) * 2
        R6 = (R1 - R2) / R5
        R7 = 0

        N_PASSES = R6
        C_PASSES = 1

        IF R7 == 0
            MSG("INICIAR CICLO DE DESBASTE? - CYCLE START")
            M0
            MSG("")
            GOTO N60
        ENDIF

        IF R7 == 1
            MSG("INICIAR CICLO DE ACABAMENTO? - CYCLE START")
            M0
            MSG("")
            GOTO N90
        ENDIF

        IF R7 == 0 OR 1
            MSG("")
        ELSE
            MSG("ESCOLHA O CICLO QUE DESEJA REALIZAR, ATRIBUINDO UM VALOR A VARIÁVEL DE CONTROLE.")
            M0
            M30    
        ENDIF

        N60 G0 X=(R1 + 10)
        N70 G0 Z2

        N80 G0 X=R1

        FOR R8 = 0 TO (R6 - 1)
            MSG("PASSE DE DESBASTE: "<<C_PASSES<<" DE "<<N_PASSES)
            G91
            G1 X=R4 F{self.get_avanco}
            Z=R3
            X=ABS(R4)
            G0 Z=ABS(R3)
            C_PASSES = C_PASSES + 1
            G1 X=R4 F{self.get_avanco}
        ENDFOR

        MSG("INICIAR CICLO DE ACABAMENTO? - CYCLE START")
        M0
        MSG("PASSE DE ACABAMENTO: 1 DE 1")

        N90 G90
        N100 G0 X=R1

        N110 G0 X=R2
        N120 G1 Z=R3 F{self.get_avanco}
        N130 G0 X=R1

        MSG("")
        N140 G0 {self.get_referencia} X{self.get_posx} Z{self.get_posz}

        N150 M5
        N160 M30''')

        with open(file='Ciclo de Desbaste.txt', mode='w') as file:
            file.write(gcode_text)

        messagebox.showinfo(title='Compilador G-Code', message='O ciclo de desbaste foi gerado com sucesso e já está disponível no sistema.')
        print('- O seu ciclo de desbaste foi gerado!')