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
            self.sentido = self.__json.get_data(self.__json.data_parameters, 'sentido') # Retorna o valor do sentido de rotação

            if self.sentido == 'HORARIO':
                self.sentido = 'M3'
            
            elif self.sentido == 'ANTI-HORARIO':
                self.sentido = 'M4'

            self.__file_configs = textwrap.dedent(f'''
            ; G-Code Configurações
            N10 MSG("CARREGANDO PARÂMETROS DE CORTE...")

            N20 G290;
            N30 G18 G40 G90 G95;

            N40 G97 S{self.__json.get_data(self.__json.data_parameters, 'rpm')};
            N50 {self.__json.get_data(self.__json.data_parameters, 'ferramenta')};
            N60 {self.sentido};

            N70 RET;''')
            
            return self.__file_configs
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo configs, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo controls em atributo
    def create_controls(self):
        try:
            self.__file_controls = textwrap.dedent(f'''
            ; Seção de Configurações de Macros
            N10 DEFINE POS_SEG AS G0 {self.__json.get_data(self.__json.data_machine, 'offset')} X{self.__json.get_data(self.__json.data_standard, 'posx')} Z{self.__json.get_data(self.__json.data_standard, 'posz')}; Posicionamento de Segurança
            N20 DEFINE AFAST AS G90 G0 X{self.__json.get_data(self.__json.data_standard, 'posx')} Z{self.__json.get_data(self.__json.data_standard, 'posz')}; Afastamento da Peça

            N30 DEFINE APROX_D AS G0 X=R1 Z0; Aproximação da Peça - Desbaste
            N40 DEFINE APROX_A AS G0 X=R2 Z0; Aproximação da peça - Acabamento

            N50 POS_SEG;
            N60 APROX_D;

            N70 MSG("CARREGANDO MACROS...");
            N80 MSG("");

            ; Estrutura de repetição - Desbaste
            FOR R8 = 1 TO R7
                G91
                G1 X=R4 F{self.__json.get_data(self.__json.data_parameters, 'avanco')}
                G1 Z=R3
                G0 X=R5 Z=ABS(R3)
                G1 X=R4
            ENDFOR

            N90 AFAST;

            ; Seção de Acabamento da Peça
            N100 MSG("INICIAR ACABAMENTO? - CYCLE START!");
            N110 M00;
            N120 MSG("PASSE DE ACABAMENTO: 1 DE 1");

            N130 APROX_A;
            N140 G1 Z=R3;
            N150 G1 X=R1;
            N160 APROX_D;

            N170 MSG("");
            N180 AFAST;

            N190 RET;''')

            return self.__file_controls
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo controls, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo macvars em atributo
    def create_macvars(self):
        try:
            self.__file_macvars = textwrap.dedent(f'''
            ; Seção de Variáveis Secudárias
            N10 R5 = ABS(R4); Conversão da var de passe
            N20 R6 = (R1 - R2) / R5; Número de passes
            N30 R7 = R6 - 1; Variável de condicional para desbaste 
            N40 DIAMON; Programação em diâmetro

            ; Estrutura de Controle - Passe
            IF R5 <= 0
                MSG("- OCORREU UM ERRO NA INSERÇÃO DO VALOR DO PASSE. TENTE NOVAMENTE!");
                M00;
                M30;
            ELSE
                MSG("CARREGANDO LÓGICAS DE VARIÁVEIS...")
                _N_CMP_CONTROLS_SPF; 
            ENDIF

            N50 RET;''')
        
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
            self.__imp = self.__json.get_data(self.__json.data_file, 'diretorio') # Importa o caminho do diretório que o usuário escolheu
            self.__directory = f'{self.__imp}/{name_directory}.WPD' # Concatena o nome da pasta com o caminho do diretório

            if os.path.exists(self.__directory):
                raise ValueError('Erro na geração do g-code')
            else:
                os.mkdir(self.__directory)

                with open(f'{self.__directory}/CMP_MAIN.MPF', 'w') as f:
                    f.write(self.file_main)

                with open(f'{self.__directory}/CMP_CONFIGS.SPF', 'w') as f:
                    f.write(self.file_configs)

                with open(f'{self.__directory}/CMP_CONTROLS.SPF', 'w') as f:
                    f.write(self.file_controls)

                with open(f'{self.__directory}/CMP_MACVARS.SPF', 'w') as f:
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
    
    @property
    def directory_project(self):
        return self.__directory