import textwrap
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from src.model.cycles.cycle_base import CycleBase

class Canais_Funcional(CycleBase):

    def __init__(self, diametro_inicial: float, diametro_final: float, distancia_final: float, posicao_final: float, aproximacao_z: float):

        if not isinstance(diametro_inicial, float):
            raise ValueError ('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(distancia_final, float):
            raise ValueError ('O valor da distância final dos canais deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if not isinstance(diametro_final, float):
            raise ValueError ('O valor do diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if not isinstance(posicao_final, float):
            raise ValueError ('O valor da posição final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
            
        if not isinstance(aproximacao_z, float):
            raise ValueError ('O valor da aproximação em Z deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if diametro_inicial <= diametro_final:
            messagebox.showerror(title='Compilador G-Code', message='O diâmetro inicial não pode ser igual ou menor que o diâmetro final. Por favor, tente novamente.')
            return            

        if distancia_final <= 0:
            messagebox.showerror(title='Compilador G-Code', message='A distância final dos canais não pode ser menor ou igual a zero. Por favor, tente novamente.')
            return
        
        if posicao_final <= 0:
            messagebox.showerror(title='Compilador G-Code', message='A posição final não pode ser igual ou menor que zero. Por favor, tente novamente.')
            return

        self.__diametro_inicial = diametro_inicial
        self.__distancia_final = distancia_final
        self.__diametro_final = diametro_final
        self.__posicao_final = posicao_final
        self.__aproximcao_z = aproximacao_z

    @property
    def get_diametro_inicial(self):
        return self.__diametro_inicial
    
    @property
    def get_distancia_final(self):
        return self.__distancia_final

    @property
    def get_diametro_final(self):
        return self.__diametro_final
    
    @property
    def get_posicao_final(self):
        return self.__posicao_final
    
    @property
    def get_aproximacao_z(self):
        return self.__aproximcao_z

    def gcode(self):

        self.gcode_text = textwrap.dedent(f'''
        N10 G291
        N20 G21 G40 G90 G95

        N30 {self.get_referencia} G0 X{self.get_posx} Z{self.get_posz}

        N40 {self.get_ferramenta}
        N50 G97 S{self.get_rotacao} M3

        N60 G0 X{self.get_diametro_inicial} Z{self.get_aproximacao_z} M8

        N70 G75 R1
        N80 G75 X{self.get_diametro_final} Z-{self.get_posicao_final} P{self.get_passe} Q{self.get_distancia_final} F{self.get_avanco}

        N90 {self.get_referencia} G0 X{self.get_posx} Z{self.get_posz}

        N100 M9
        N110 M5
        N120 M30''')

        arquivo = asksaveasfilename(defaultextension='.txt', filetypes=[('Arquivos de Texto', '*.txt'), ('Todos os Arquivos', '*.*')])

        if arquivo:
            with open(arquivo, mode='w') as file:
                file.write(self.gcode_text)
                
            messagebox.showinfo(title='Compilador G-Code', message='O ciclo de canais (f) foi gerado com sucesso e já está disponível no sistema.')
            print(' - O ciclo de canais (f) foi gerado!')