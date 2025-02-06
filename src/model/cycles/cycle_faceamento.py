import textwrap
from tkinter import messagebox
from src.model.cycles.cycle_base import CycleBase

class CicloFaceamento(CycleBase):

    def __init__(self, diametro_inicial: float, diametro_final: float):

        if not isinstance(diametro_inicial, float):
            raise ValueError ('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(diametro_final, float):
            raise ValueError ('O valor do diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if diametro_inicial < diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro inicial não pode ser menor que o diâmetro final. Por favor, insira um valor válido.')
            return

        self._diametro_inicial = diametro_inicial
        self._diametro_final = diametro_final

    @property
    def get_diametro_inicial(self):
        return self._diametro_inicial
    
    @property
    def get_diametro_final(self):
        return self._diametro_final
    
    @get_diametro_inicial.setter
    def set_diametro_inicial(self, novo_diametro_inicial: float):

        if not isinstance(novo_diametro_inicial, float):
            raise ValueError ('O valor do novo diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if novo_diametro_inicial == self._diametro_inicial:
            messagebox.showinfo(title='Compilador G-Code', message='O novo diâmetro inicial informado é igual ao diâmetro inicial anterior.')

        if novo_diametro_inicial < self._diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O novo diâmetro inicial informado é igual ao diâmetro inicial anterior.')
            return

        self._diametro_inicial = novo_diametro_inicial
        return self._diametro_inicial

    @get_diametro_final.setter
    def set_diametro_final(self, novo_diametro_final: float):

        if not isinstance(novo_diametro_final, float):
            raise ValueError ('O valor do diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if novo_diametro_final == self._diametro_final:
            messagebox.showinfo(title='Compilador G-Code', message='O novo diâmetro final informado é igual ao diâmetro inicial anterior.')

        if novo_diametro_final > self._diametro_inicial:
            messagebox.showerror(title='Compilador G-Code', message='O novo diâmetro final é maior que o diâmetro inicial. Por favor, verifique os valores e tente novamente.')
            return

        self._diametro_final = novo_diametro_final
        return self._diametro_final
    
    def gcode(self, nome_arquivo='Ciclo de Faceamento'):

        gcode_text = textwrap.dedent(f'''
        G290
        G18 G40 G90 G95

        G0 G54 X400 Z1

        T1D1 M3
        G97 S500

        R1 = {self.get_diametro_inicial}
        R2 = {self.get_diametro_final}
        R3 = -5  ; ESPESSURA

        R4 = -1.5  ; PASSE DE PROFUNDIDADE
        R6 = 0   ; CONDICIONAL

        R7 = ABS(R3) 
        R8 = ABS(R4)
        R9 = R7 / R8

        G0 X=(R1 + 1) M8
        G0 Z0

        WHILE R6 < R9
            G90
            G1 X=R2 F1
            G91
            Z=ABS(R4)
            G90
            X=R1
            G91
            Z=(R4 * 2)
            R6 = R6 + 1
        ENDWHILE

        M00

        G90
        G0 X=(R1 + 1)
        G0 Z0

        G0 Z=R3
        G1 X=R2 F1
        G0 X=(R1 + 1)

        G0 G54 X400 Z1

        M5
        M9
        M30''')

        with open(f'{nome_arquivo}.txt', 'w') as arquivo:
            arquivo.write(gcode_text)

        messagebox.showinfo(title='Compilador G-Code', message='O ciclo de faceamento foi gerado com sucesso e já está disponível no sistema.')
        print('- O seu ciclo de faceamento foi gerado!')
