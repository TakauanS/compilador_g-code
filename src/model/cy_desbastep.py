import os
import textwrap
from tkinter import messagebox

from src.model.cycles.cy_base import CyBase
from src.model.json_manager.json_main import JsonMain
from src.model.json_manager.cy_parametrizados.json_desbastep import JsonDesbasteP

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

        self.jsonM = JsonMain()
        self.jsonC = JsonDesbasteP()

    # Método responsável por armazenar o arquivo main em atributo
    def create_main(self):
        try:
            self.__file_main = textwrap.dedent(f'''
            ; Seção de Definição de Variáveis de Usuário - PUDs
            DEF REAL DIAMETRO_INICIAL;
            DEF REAL DIAMETRO_FINAL;
            DEF REAL ESPESSURA;

            DEF INT FERRAMENTA_DESB;
            DEF INT FERRAMENTA_ACAB;

            DEF REAL X_POS; 
            DEF REAL Z_POS; 
            DEF REAL APRX; 
            DEF REAL APRZ;

            DEF REAL LIMIT_RPM;
            DEF REAL AVANCO;
            DEF REAL PASSE;
            DEF REAL RPM;

            DEF STRING [80] ESTILO;
            DEF STRING [1] FORMA;

            ; Seção de Inserção de Ferramenta
            FERRAMENTA_DESB = {self.jsonC.get_data(self.jsonC.data_desbastep, 'ferd')}; 
            FERRAMENTA_ACAB = {self.jsonC.get_data(self.jsonC.data_desbastep, 'fera')};
            
            ; Seção de Inserção de Parâmetros da Peça
            DIAMETRO_INICIAL = {self.diametro_inicial};
            DIAMETRO_FINAL = {self.diametro_final};
            ESPESSURA = -{self.espessura};

            ; Seção de Inserção de Parâmetros de Corte
            AVANCO = {self.jsonC.get_data(self.jsonC.data_desbastep, 'avan')};
            PASSE = -{self.jsonC.get_data(self.jsonC.data_desbastep, 'pass')};
            RPM = {self.jsonC.get_data(self.jsonC.data_desbastep, 'rpmp')}; 
            LIMIT_RPM = {self.jsonC.get_data(self.jsonC.data_desbastep, 'lims')};

            ; Seção de Inserção de valores de Posicionamentos
            X_POS = {self.jsonC.get_data(self.jsonC.data_desbastep, 'posx')};
            Z_POS = {self.jsonC.get_data(self.jsonC.data_desbastep, 'posz')};
            
            APRX = {self.jsonC.get_data(self.jsonC.data_desbastep, 'aprx')};
            APRZ = {self.jsonC.get_data(self.jsonC.data_desbastep, 'aprz')};

            ; Estilo de Usinagem
            ESTILO = "desbaste-padrao";
            FORMA = "d";

            _N_CMP_CONFIGS_SPF;
            
            M30;''')

            return self.__file_main

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo main, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo configs em atributo
    def create_configs(self):
        try:
            modo_velo = self.jsonC.get_data(self.jsonC.data_rotations, 'modo_velo')
            sent_spin = self.jsonC.get_data(self.jsonC.data_rotations, 'sent_giro')
            #self.modo = self.jsonC.get_data(self.jsonC.data_parameters, 'modo') # Retorna o valor do modo de corte
            #self.sentido = self.jsonC.get_data(self.jsonC.data_parameters, 'sentido') # Retorna o valor do sentido de rotação

            #if self.sentido == 'HORÁRIO':
            #    self.sentido = 'M3'

            #elif self.sentido == 'ANTI-HORÁRIO':
             #   self.sentido = 'M4'

            #if self.modo == 'VC - COSTANTE (G96)':
             #   self.modo = 'G96'
              #  self.modo_avanco = 'G94'
            
            #elif self.modo == 'VC - FIXA (G97)':
             #   self.modo = 'G97'
              #  self.modo_avanco = 'G95'

            self.__file_configs = textwrap.dedent(f'''
            ; Seção de Carregamento de Parâmetros
            MSG("- CARREGANDO PARAMETROS G-CODES...");                                
                                                  
            N10 G290;
            N20 G18 G40 G90 ;
                            
            N30 {modo_velo} S=RPM;
            N40 LIMS=LIMIT_RPM;
            N50 ;
            N60 {sent_spin};

            MSG("");
            _N_CMP_INIT_SPF;
                                            
            N70 RET;
            ''')
            
            return self.__file_configs
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo configs, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo init em atributo
    def create_init(self):
        try:
            tipo_dim = self.jsonC.get_data(self.jsonC.data_desbastep, 'tdim') # retorna o tipo de dimensão (diâmetro ou raio)

            if tipo_dim == 'DIÂMETRO' or tipo_dim == '':
                tipo_dim = 'DIAMON; Programação em Diâmetro'
            
            if tipo_dim == 'RAIO':
                tipo_dim = 'DIAMOF; Programação em Raio'

            self.__file_init = textwrap.dedent(f'''
            ; Seção de Variáveis de Usuário - LUDs
            N10 DEF STRING [30] _RESULT; Var que retorna o valor da forma de usinagem
                        
            ; Seção de Variáveis Secundárias
            N20 R1 = ABS(PASSE); Conversão da var passe
            N30 R2 = (DIAMETRO_INICIAL - DIAMETRO_FINAL) / R1; Número de passes
            N40 R3 = R2 - 1; Condicional para desbaste padrao
            N50 R4 = R2 - R1; Condicional para desbaste zig-zag

            N60 _RESULT = TOUPPER(ESTILO);
            N70 {tipo_dim} 

            ; Estruturas de Controles
            IF R1 <= 0
                MSG("- ERRO NA INSERÇÃO DO VALOR DO PASSE. TENTE NOVAMENTE!");
                M00;
                M30;
            ENDIF

            IF (_RESULT=="DESBASTE-PADRAO")
                MSG("- CARREGANDO CICLO DE DEBSASTE PADRÃO...");
                _N_CMP_DESB_PADRAO_SPF;
            ENDIF

            IF (_RESULT=="DESBASTE-ZIG")
                MSG("- CARREGANDO CICLO DE DESBASTE ZIG-ZAG...");
                _N_CMP_DESB_ZIG_SPF;
            ENDIF

            N80 RET;''')

            return self.__file_init
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo init, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo de ciclo de desbaste padrão em atributo
    def create_desbaste_padrao(self):
        try:
            self.__file_desbastep = textwrap.dedent(f'''
            N10 G0 G54 X=X_POS Z=Z_POS;

            ; Estrutura de Controle - Desbaste & Acabamento
            IF (FORMA=="d")
                MSG("- INICIALIZANDO PARÂMETROS DO CICLO DE DESBASTE - PADRÃO...");
                MSG("");
                GOTO N20;
            ENDIF

            IF (FORMA=="a")
                MSG("- INICIALIZANDO PARÂMETROS DO CICLO DE ACABAMENTO - PADRÃO...")
                MSG("");
                GOTO N70;
            ENDIF

            N20 G0 X=APRX;
            N30 G0 Z=APRZ;
            N40 G90 G0 X=DIAMETRO_INICIAL;

            WHILE R0 <= R3
                MSG("- DESBASTE EM ANDAMENTO...")
                G91 G1 X=PASSE F=AVANCO
                G90 G1 Z=ESPESSURA
                G91 G0 X=ABS(PASSE)
                G90 G0 Z=APRZ
                G91 G1 X=PASSE
                R0 = R0 + 1
            ENDWHILE

            N50 G90;
            N60 G0 G54 X=X_POS Z=Z_POS;

            ; Seção de Acabamento
            MSG("- INICIAR CICLO DE ACABAMENTO? CYCLE START!");
            M00;
            MSG("PASSE DE ACABAMENTO: 1 DE 1");

            N70 T=FERRAMENTA_ACAB;

            N80 G0 X=DIAMETRO_FINAL Z=APRZ;
            N90 G1 Z=ESPESSURA;
            N100 G1 X=DIAMETRO_INICIAL;

            MSG("");
            N110 G0 G54 X=X_POS Z=Z_POS;
            N120 RET;''')
        
            return self.__file_desbastep
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo de ciclo de desbaste padrão, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)
        
    # Método responsável por armazenar o arquivo de ciclo de desbaste zigzag em atributo
    def create_desbaste_zig(self):
        try:
            self.__file_desbastez = textwrap.dedent(f'''
            N10 G0 G54 X=X_POS Z=Z_POS;

            ; Estrutura de Controle - Desbaste & Acabamento
            IF (FORMA=="d")
                MSG("- INICIALIZANDO PARÂMETROS DO CICLO DE DESBASTE - PADRÃO...");
                MSG("");
                GOTO N20;
            ENDIF

            IF (FORMA=="a")
                MSG("- INICIALIZANDO PARÂMETROS DO CICLO DE ACABAMENTO - PADRÃO...")
                MSG("");
                GOTO N70;
            ENDIF

            N20 G0 X=DIAMETRO_INICIAL;
            N30 G0 Z=APZ_D;

            WHILE R0 <= R3
                G91 G1 X=PASSE F=AVANCO
                G90 G1 Z=ESPESSURA
                G91 G0 X=ABS(PASSE)
                G90 G0 Z=APZ_D
                G91 G1 X=PASSE
                R0 = R0 + 1
            ENDWHILE

            N50 G90;
            N60 G0 G54 X=X_POS Z=Z_POS;

            ; Seção de Acabamento
            MSG("- INICIAR CICLO DE ACABAMENTO? CYCLE START!");
            M00;
            MSG("");

            N70 G0 X=DIAMETRO_FINAL Z=APZ_A;
            N80 G1 Z=ESPESSURA;
            N90 G1 X=DIAMETRO_INICIAL;

            N100 G0 G54 X=X_POS Z=Z_POS;
            N110 RET;''')
        
            return self.__file_desbastez
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo de ciclo de desbaste zigzag, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por inicializar os arquivos g-codes
    def initialize_files(self):
        try:
            self.create_main()
            self.create_init()
            self.create_configs()
            self.create_desbaste_zig()
            self.create_desbaste_padrao()
        
        except Exception as e:
            raise ValueError(f'Erro na inicialização dos arquivos g-code: {e}')

    # Método responsável por gerar o g-code do ciclo de desbaste parametrizado
    def generate_gcode(self, name_directory: str):
        try:
            self.__imp = self.jsonM.get_data(self.jsonM.data_programa, 'diretorio') # Importa o caminho do diretório que o usuário escolheu
            self.__directory = f'{self.__imp}/{name_directory}.WPD' # Concatena o nome da pasta com o caminho do diretório

            if os.path.exists(self.__directory):
                messagebox.showerror('Compilador G-Code', 'O nome de projeto inserido já é existente, tente novamente um novo nome de projeto!')
                return
            else:
                os.mkdir(self.__directory)

                with open(f'{self.__directory}/CMP_MAIN.MPF', 'w') as f:
                    f.write(self.file_main)

                with open(f'{self.__directory}/CMP_CONFIGS.SPF', 'w') as f:
                    f.write(self.file_configs)

                with open(f'{self.__directory}/CMP_INIT.SPF', 'w') as f:
                    f.write(self.file_init)

                with open(f'{self.__directory}/CMP_DESB_PADRAO.SPF', 'w') as f:
                    f.write(self.file_desbastep)

                with open(f'{self.__directory}/CMP_DESB_ZIG.SPF', 'w') as f:
                    f.write(self.file_desbastez)

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
    def file_init(self):
        return self.__file_init
    
    @property
    def file_desbastep(self):
        return self.__file_desbastep
    
    @property
    def file_desbastez(self):
        return self.__file_desbastez
    
    @property
    def directory_project(self):
        return self.__directory