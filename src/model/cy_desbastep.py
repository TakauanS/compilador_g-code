import os
import textwrap
from tkinter import messagebox
from src.model.cycles.cy_base import CyBase

from src.model.json_handler import JsonHandler

class CyDesbasteP(CyBase):

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

        self.__json = JsonHandler()
        self.__json.convert_files()

    # Método responsável por armazenar o arquivo main em atributo
    def create_main(self):
        try:
            self.__file_main = textwrap.dedent(f'''
            N10 _N_CMP_CONFIGS_SPF;

            N20 R1 = {self.diametro_inicial} 
            N30 R2 = {self.diametro_final}

            N40 R3 = -{self.espessura}
            N50 R4 = -{self.__json.get_data(self.__json.data_parameters, 'passe')}

            N60 _N_CMP_MACVARS_SPF;

            N70 M30;''')

            return self.__file_main

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo main, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo configs em atributo
    def create_configs(self):
        try:
            self.__file_configs = textwrap.dedent(f'''
            ; G-Code configuration
            N10 G290;
            N20 G18 G40 G90 G95;

            ; Tool and rpm senttings
            N30 G97 S{self.__json.get_data(self.__json.data_standard, 'rpm')};
            N40 {self.__json.get_data(self.__json.data_parameters, 'ferramenta')};
            N50 M3;

            N60 RET;''')
            
            return self.__file_configs
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo configs, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo controls em atributo
    def create_controls(self):
        try:
            self.__file_controls = textwrap.dedent(f'''
            ; Macro configuration section
            N10 DEFINE POS_SEG AS G0 {self.__json.get_data(self.__json.data_machine, 'offset')} X{self.__json.get_data(self.__json.data_standard, 'posx')} Z{self.__json.get_data(self.__json.data_standard, 'posz')}; Safety positions macro
            N20 DEFINE APROX AS G0 X=R1 Z0; X approximation macro

            N30 POS_SEG;
            N40 APROX;

            ; Repeating structure section
            FOR R8 = 1 TO R7
                G91
                G1 X=R4 F{self.__json.get_data(self.__json.data_parameters, 'avanco')}
                G1 Z=R3
                G0 X=R5 Z=ABS(R3)
                G1 X=R4
            ENDFOR

            N50 RET;''')

            return self.__file_controls
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo controls, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo macvars em atributo
    def create_macvars(self):
        try:
            self.__file_macvars = textwrap.dedent(f'''
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
        
            return self.__file_macvars
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo macvars, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por inicializar os arquivos g-codes
    def initialize_files(self):
        try:
            self.create_main()
            self.create_macvars()
            self.create_configs()
            self.create_controls()
        
        except Exception as e:
            raise ValueError(f'Erro na inicialização dos arquivos g-code:\n\n{e}')

    # Método responsável por gerar o g-code do ciclo de desbaste parametrizado
    def generate_gcode(self, name_directory: str):
        try:
            self.__imp = self.__json.get_data(self.__json.data_file, 'diretório') # Importa o caminho do diretório que o usuário escolheu
            self.__directory = f'{self.__imp}/{name_directory}' # Concatena o nome da pasta com o caminho do diretório

            if os.path.exists(self.__directory):
                messagebox.showerror('Compilador G-Code', f'Erro na geração do g-code, pois o nome de projeto:\n\n{name_directory}, já é existente!')
                return
            else:
                os.mkdir(self.__directory)

                with open(f'{self.__directory}/CMP_MAIN.mpf', 'w') as f:
                    f.write(self.file_main)

                with open(f'{self.__directory}/CMP_CONFIGS.spf', 'w') as f:
                    f.write(self.file_configs)

                with open(f'{self.__directory}/CMP_CONTROLS.spf', 'w') as f:
                    f.write(self.file_controls)

                with open(f'{self.__directory}/CMP_MACVARS.spf', 'w') as f:
                    f.write(self.file_macvars)

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na geração do g-code, verifique o seguinte problema:\n\n{e}')
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
    
    @property
    def file_main(self):
        return self.__file_main
    
    @property
    def file_configs(self):
        return self.__file_configs
    
    @property
    def file_controls(self):
        return self.__file_controls
    
    @property
    def file_macvars(self):
        return self.__file_macvars