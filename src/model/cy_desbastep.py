import textwrap
from tkinter import messagebox
from src.model.cycles.cycle_base import CycleBase

class CyDesbasteP(CycleBase):

    def __init__(self, di_inicial: float, di_final: float, espessura: float):

        if not isinstance(di_inicial, float):
            raise TypeError('O tipo de valor para diâmetro inicial deve ser do tipo Float!')

        if not isinstance(di_final, float):
            raise TypeError('O tipo de valor para diâmetro final deve ser do tipo Float!')
        
        if not isinstance(espessura, float):
            raise TypeError('O tipo de valor para espessura deve ser do tipo Float!')

        if di_inicial <= di_final:
            messagebox.showerror('Compilador G-Code', 'Erro: o diâmetro inicial é menor ou igual ao diâmetro final!')
            raise ValueError('O diâmetro inicial é menor ou igual ao diâmetro final!')

        if espessura <= 0:
            messagebox.showerror('Compilador G-Code', 'Erro: a espessura especificada é igual ou menor que zero!')
            raise ValueError('A espessura especificada é igual ou menor que zero!')

        self.__di_inicial = di_inicial
        self.__di_final = di_final
        self.__espessura = espessura

    # Método responsável por armazenar o arquivo main em atributo
    def generate_main(self):
        try:
            self.__main = textwrap.dedent(f'''
            N10 _N_CMP_CONFIGS_SPF;

            N20 R1 = {self.diametro_inicial} 
            N30 R2 = {self.diametro_final}

            N40 R3 = -{self.espessura}
            N50 R4 = -1.6

            N60 _N_CMP_MACVARS_SPF;

            N70 M30;''')

            return self.__main
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo main, revise os campos de entrada e tente novamente!\n\n{e}')
            print(f'Erro: {e}')
    
    # Método responsável por armazenar o arquivo configs em atributo
    def generate_configs(self):
        try:
            self.__configs = textwrap.dedent(f'''
            ; G-Code configuration
            N10 G290;
            N20 G18 G40 G90 G95;

            ; Tool and rpm senttings
            N30 G97 S100;
            N40 T11D1;
            N50 M3;

            N60 RET;''')
            
            return self.__configs
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo configs, revise os campos de entrada e tente novamente!\n\n{e}')
            print(f'Erro: {e}')

    # Método responsável por armazenar o arquivo controls em atributo
    def generate_controls(self):
        try:
            self.__controls = textwrap.dedent(f'''
            ; Macro configuration section
            N10 DEFINE POS_SEG AS G0 G54 X400 Z400; Safety positions macro
            N20 DEFINE APROX AS G0 X=R1 Z0; X approximation macro

            N30 POS_SEG;
            N40 APROX;

            ; Repeating structure section
            FOR R8 = 1 TO R7
                G91
                G1 X=R4 F1
                G1 Z=R3
                G0 X=R5 Z=ABS(R3)
                G1 X=R4
            ENDFOR

            N50 RET;''')

            return self.__controls
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo controls, revise os campos de entrada e tente novamente!\n\n{e}')
            print(f'Erro: {e}')

    # Método responsável por armazenar o arquivo macvars em atributo
    def generate_macvars(self):
        try:
            self.__macvars = textwrap.dedent(f'''
            ; Secondary variable section
            N10 R5 = ABS(R4); Pass variable conversion
            N20 R6 = (R1 - R2) / R5; Number of passes variable

            N30 R7 = (R6 / 2) - 0.5;

            ; Control structure section
            IF R5 > 1.5
                MSG("- OCORREU UM ERRO NA INSERÇÃO DO VALOR DO PASSE. TENTE NOVAMENTE!");
                M00;
                M30;
            ELSE
                _N_CMP_CONTROLS_SPF; 
            ENDIF

            N40 RET;''')
        
            return self.__macvars
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo macvars, revise os campos de entrada e tente novamente!\n\n{e}')
            print(f'Erro: {e}')

    @property
    def diametro_inicial(self):
        return self.__di_inicial
    
    @property
    def diametro_final(self):
        return self.__di_final
    
    @property
    def espessura(self):
        return self.__espessura