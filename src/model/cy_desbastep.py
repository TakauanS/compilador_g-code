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
            DEF REAL DIAMETRO_INICIAL, DIAMETRO_FINAL, ESPESSURA;
            DEF INT FERRAMENTA_DESB, FERRAMENTA_ACAB;
            DEF REAL LIMIT_RPM, AVANCO, PASSE, RPM;
            DEF REAL X_POS, Z_POS, APRX, APRZ;
            DEF STRING [80] ESTILO, FORMA;

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
            modo_prog = self.jsonC.get_data(self.jsonC.data_desbastep, 'tdim')
            modo_velo = self.jsonC.get_data(self.jsonC.data_rotations, 'modo_velo')
            sent_giro = self.jsonC.get_data(self.jsonC.data_rotations, 'sent_giro')

            if modo_prog == '' or modo_prog == 'DIÂMETRO':
                modo_prog = 'DIAMON'

            if modo_prog == 'RAIO':
                modo_prog = 'DIAMOF'

            if modo_velo == '' or modo_velo == 'FIXA':
                modo_velo = 'G97'

            if modo_velo == 'CONSTANTE':
                modo_velo = 'G96'

            if sent_giro == '' or sent_giro == 'HORÁRIO':
                sent_giro = 'M3'

            if sent_giro == 'ANTI-HORÁRIO':
                sent_giro = 'M4'

            if modo_velo == 'G96':
                modo_avanco = 'G95'

            if modo_velo == 'G97':
                modo_avanco  = 'G94'

            self.__file_configs = textwrap.dedent(f'''
            ; Seção de Carregamento de Parâmetros
            MSG("- CARREGANDO PARAMETROS G-CODES...");                                
                                                  
            N10 G290;
            N20 G18 G40 G90 {modo_avanco};
                            
            N30 {modo_velo} S=RPM;
            N40 LIMS=LIMIT_RPM;
            N50 {self.jsonC.get_data(self.jsonC.data_desbastep, 'ferd')}
            N60 {sent_giro};

            N70 {modo_prog};
            
            MSG("");
            _N_CMP_INIT_SPF;
                                            
            N80 RET;
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
            N10 DEF STRING [30] _ESTILO; Var que retorna o valor do estilo de usinagem
            N20 DEF STRING [1] _FORMA; Var que retorna o valor da forma de usinagem
                        
            ; Seção de Variáveis Secundárias
            N30 R1 = ABS(PASSE); Conversão da var passe
            N40 R2 = (DIAMETRO_INICIAL - DIAMETRO_FINAL) / R1; Número de passes
            N50 R3 = R2 - 1; Condicional para desbaste padrao
            N60 R4 = R2 - R1; Condicional para desbaste zig-zag
            R5 = R2 - 2.5

            N70 _ESTILO = TOUPPER(ESTILO);
            N80 _FORMA = TOUPPER(FORMA);

            IF (_ESTILO=="DESBASTE-PADRAO")
                IF (_FORMA=="D")
                    MSG(" - CARREGANDO CICLO DE DESBASTE PADRÃO...");
                    _N_CMP_DESB_PADRAO_SPF;
                ENDIF
                IF (_FORMA=="A")
                    MSG(" - CARREGANDO CICLO DE DESBASTE PADRÃO...");
                    CALL "_N_CMP_DESB_PADRAO_SPF" BLOCK "INICIO_ACABAMENTO" TO "FIM_ACABAMENTO"
                ENDIF
            ENDIF

            IF (_ESTILO == "DESBASTE-ZIG")
                IF (_FORMA == "D")
                    MSG(" - CARREGANDO CICLO DE DESBASTE ZIG-ZAG...");
                    _N_CMP_DESB_ZIG_SPF;
                ENDIF
            ENDIF

            N90 RET;''')

            return self.__file_init
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo init, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo de ciclo de desbaste padrão em atributo
    def create_desbaste_padrao(self):
        try:
            self.__file_desbastep = textwrap.dedent(f'''
            N10 G0 G54 X=X_POS Z=Z_POS;

            N20 G0 X=APRX;
            N30 G0 Z=APRZ;
            N40 G0 X=DIAMETRO_INICIAL; 

            WHILE R0 <= R3
                MSG(" - DESBASTE EM ANDAMENTO...")
                G1 X=IC(PASSE) F=AVANCO
                G1 Z=ESPESSURA
                G0 X=IC(ABS(PASSE))
                G0 Z=APRZ
                G1 X=IC(PASSE)
                R0 = R0 + 1
            ENDWHILE

            INICIO_ACABAMENTO:

            N50 G0 G54 X=X_POS Z=Z_POS;
            MSG("");

            IF FERRAMENTA_DESB <> FERRAMENTA_ACAB
                T=FERRAMENTA_ACAB;
            ENDIF

            MSG("PASSE DE ACABAMENTO: 1 DE 1");

            N70 G0 X=DIAMETRO_FINAL Z=APRZ;
            N80 G1 Z=ESPESSURA;
            N90 G1 X=DIAMETRO_INICIAL;

            MSG("");
            N100 G0 G54 X=X_POS Z=Z_POS;

            FIM_ACABAMENTO:
            N110 RET;''')
        
            return self.__file_desbastep
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo de ciclo de desbaste padrão, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)
        
    # Método responsável por armazenar o arquivo de ciclo de desbaste zigzag em atributo
    def create_desbaste_zig(self):
        try:
            self.__file_desbastez = textwrap.dedent(f'''
            MSG("");
            N10 G0 G54 X=X_POS Z=Z_POS;

            N20 G0 X=APRX;
            N30 G0 Z=APRZ;
            N40 G0 X=DIAMETRO_INICIAL;

            WHILE R0 <= R5
                MSG(" - DESBASTE EM ANDAMENTO...")
                G1 X=IC(PASSE) F=AVANCO
                G1 Z=ESPESSURA
                R0 = R0 + 1
                G1 X=IC(PASSE)
                G1 Z=APRZ
                R0 = R0 + 1
            ENDWHILE

            M00

            N40 G90;
            N50 G0 G54 X=X_POS Z=Z_POS;

            ; Seção de Acabamento
            MSG("- INICIAR CICLO DE ACABAMENTO? CYCLE START!");
            M00;
            MSG("");

            N60 G0 X=DIAMETRO_FINAL Z=APRZ;
            N70 G1 Z=ESPESSURA;
            N80 G1 X=DIAMETRO_INICIAL;

            N90 G0 G54 X=X_POS Z=Z_POS;
            N100 RET;''')
        
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