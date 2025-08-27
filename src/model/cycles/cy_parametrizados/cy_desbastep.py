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
            ava_tipo = self.jsonC.get_data(self.jsonC.data_advance, 'tipo_avanco')
            ava_desb = self.jsonC.get_data(self.jsonC.data_advance, 'ava_desbast')
            ava_acab = self.jsonC.get_data(self.jsonC.data_advance, 'ava_acabame')

            rpm_mod = self.jsonC.get_data(self.jsonC.data_rotations, 'modo_velo')
            rpm_min = self.jsonC.get_data(self.jsonC.data_rotations, 'lim_inf')
            rpm_max = self.jsonC.get_data(self.jsonC.data_rotations, 'lim_sup')

            self.__file_main = textwrap.dedent(f'''
            ; Seção de Definição de Variáveis de Usuário - PUDs
            DEF REAL DIAMETRO_INICIAL, DIAMETRO_FINAL, ESPESSURA, X_POS, Z_POS, APRX, APRZ;
            DEF REAL AVANCO_DESB, AVANCO_ACAB, RPM_MIN, RPM_MAX, RPM, PASSE;
            DEF STRING [80] TIPO_AVANCO, RPM_MODO, ESTILO, FORMA;
            DEF INT FERRAMENTA_DESB, FERRAMENTA_ACAB
                                        
            ; Seção de Inserção de Parâmetros da Peça
            DIAMETRO_INICIAL = {self.diametro_inicial};
            DIAMETRO_FINAL = {self.diametro_final};
            ESPESSURA = -{self.espessura};

            ; Seção de Inserção de valores de Posicionamentos
            X_POS = {self.jsonC.get_data(self.jsonC.data_desbastep, 'posx')};
            Z_POS = {self.jsonC.get_data(self.jsonC.data_desbastep, 'posz')};

            APRX = {self.jsonC.get_data(self.jsonC.data_desbastep, 'aprx')};
            APRZ = {self.jsonC.get_data(self.jsonC.data_desbastep, 'aprz')};

            ; Seção de Inserção de Parâmetros de Corte
            RPM = {self.jsonC.get_data(self.jsonC.data_desbastep, 'rpmp')};
            RPM_MIN = {rpm_min};
            RPM_MAX = {rpm_max};
            RPM_MODO = "{rpm_mod}";

            TIPO_AVANCO = "{ava_tipo}";
            AVANCO_DESB = {ava_desb};
            AVANCO_ACAB = {ava_acab};

            PASSE = -{self.jsonC.get_data(self.jsonC.data_desbastep, 'pass')};

            ; Seção de Inserção de Ferramenta
            FERRAMENTA_DESB = {self.jsonC.get_data(self.jsonC.data_desbastep, 'ferd')}; 
            FERRAMENTA_ACAB = {self.jsonC.get_data(self.jsonC.data_desbastep, 'fera')};
            
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
            sent_giro = self.jsonC.get_data(self.jsonC.data_rotations, 'sent_giro')

            if modo_prog == '' or modo_prog == 'DIÂMETRO':
                modo_prog = 'DIAMON'

            if modo_prog == 'RAIO':
                modo_prog = 'DIAMOF'

            if sent_giro == '' or sent_giro == 'HORÁRIO':
                sent_giro = 'M3'

            if sent_giro == 'ANTI-HORÁRIO':
                sent_giro = 'M4'

            self.__file_configs = textwrap.dedent(f'''
            ; Seção de Variáveis de Usuário - LUDs
            N10 DEF STRING [30] _RESULT_AVANCO, _RESULT_RPM; Var que Converte os Valores

            N20 _RESULT_AVANCO = TOUPPER(TIPO_AVANCO);
            N30 _RESULT_RPM = TOUPPER(RPM_MODO);

            ; Seção de Validação de Parâmetros
            IF (_RESULT_RPM=="CONSTANTE")
                IF (_RESULT_AVANCO=="MM/ROT")
                    G[15]=4; G96
                ENDIF
                IF (_RESULT_AVANCO=="MM/MIN")
                    G[15]=7; G961
                ENDIF
            ENDIF

            IF (_RESULT_RPM=="FIXA")
                IF (_RESULT_AVANCO=="MM/ROT")
                    G[15]=5; G97
                ENDIF
                IF (_RESULT_AVANCO=="MM/MIN")
                    G[15]=8; G971
                ENDIF
            ENDIF

            ; Seção de Carregamento de Parâmetros
            MSG("- CARREGANDO PARAMETROS G-CODES...");                                

            N40 G0 G54 X=X_POS Z=Z_POS;
                                                                                   
            N50 G290;
            N60 G18 G40 G90;

            N70 G25 S=RPM_MIN;
            N80 G26 S=RPM_MAX;
            N90 S=RPM;

            N100 T=FERRAMENTA_DESB;
            N110 {sent_giro};

            N120 {modo_prog};

            MSG("");
            _N_CMP_INIT_SPF;

            N130 RET;''')
            
            return self.__file_configs
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo configs, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo init em atributo
    def create_init(self):
        try:
            self.__file_init = textwrap.dedent(f'''
            ; Seção de Variáveis de Usuário - LUDs
            N10 DEF STRING [30] _ESTILO, _FORMA; Var que retorna o valor de forma e estilo
            N20 DEF BOOL _RESULT_DESB_PADRAO, _RESULT_DESB_ZIG; Var que retorna existência de arquivos
            N30 DEF REAL _TIPO; Var que retorna o tipo de ferramenta

            ; Seção de Variáveis Secundárias
            N40 R0 = 0; CO para todos os desbastes
            N50 R1 = ABS(PASSE); Conversão da var passe
            N60 R2 = (DIAMETRO_INICIAL - DIAMETRO_FINAL) / R1; Número de passes
            N70 R3 = R2 - 1; CO para desbaste padrao
            N80 R5 = R2 - 1; CO para desbaste zig

            N90 _ESTILO = TOUPPER(ESTILO);
            N100 _FORMA = TOUPPER(FORMA);

            N110 _RESULT_DESB_PADRAO = ISFILE("_N_CMP_DESB_PADRAO_SPF");
            N120 _RESULT_DESB_ZIG = ISFILE("_N_CMP_DESB_ZIG_SPF");
            N130 _TIPO = $TC_DP1[FERRAMENTA_DESB, 1];

            WORKPIECE(,,,"CYLINDER",0,0,ESPESSURA,ESPESSURA,DIAMETRO_INICIAL)

            ; Seção de Validação de Existência de Arquivos de Ciclos
            IF (_RESULT_DESB_PADRAO==FALSE)
            SETAL(61032, "_N_CMP_DESB_PADRAO_SPF"); 
            ENDIF

            IF (_RESULT_DESB_ZIG==FALSE)
                SETAL(61032, "_N_CMP_DESB_ZIG_SPF");
            ENDIF

            ; Seção de Saltos para Ciclos de Usinagem
            IF (_ESTILO=="DESBASTE-PADRAO")
                IF (_FORMA=="D")
                    MSG(" - CARREGANDO CICLO DE DESBASTE PADRÃO...");
                    _N_CMP_DESB_PADRAO_SPF;
                ENDIF
                IF (_FORMA=="A")
                    MSG(" - CARREGANDO CICLO DE ACABAMENTO PADRÃO...");
                    CALL "_N_CMP_DESB_PADRAO_SPF" BLOCK "INICIO_ACABAMENTO" TO "FIM_ACABAMENTO"
                ENDIF
            ENDIF

            IF (_ESTILO == "DESBASTE-ZIG")
                IF (_FORMA == "D")
                    IF NOT (_TIPO==550)
                        SETAL(61212);
                    ELSE
                        MSG(" - CARREGANDO CICLO DE DESBASTE ZIG-ZAG...")
                        _N_CMP_DESB_ZIG_SPF;
                    ENDIF
                ENDIF
                IF (_FORMA == "A")
                    MSG(" - CARREGANDO CICLO DE ACABAMENTO ZIG-ZAG...")
                    CALL "_N_CMP_DESB_ZIG_SPF" BLOCK "INICIO_ACABAMENTO" TO "FIM_ACABAMENTO"
                ENDIF
            ENDIF

            N140 RET;''')

            return self.__file_init
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo init, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)

    # Método responsável por armazenar o arquivo de ciclo de desbaste padrão em atributo
    def create_desbaste_padrao(self):
        try:
            modo_avanco = self.jsonC.get_data(self.jsonC.data_advance, 'modo_avanco')

            self.__file_desbastep = textwrap.dedent(f'''
            N10 G0 X=APRX Z=APRZ;
            N20 G0 X=DIAMETRO_INICIAL; 

            WHILE R0 <= R3
                MSG(" - DESBASTE EM ANDAMENTO...")
                G1 X=IC(PASSE) F=AVANCO_DESB {modo_avanco}
                G1 Z=ESPESSURA
                G1 X=IC(5)
                G0 Z=APRZ
                G0 X=IC(-5)
                R0 = R0 + 1
            ENDWHILE

            INICIO_ACABAMENTO:

            MSG("");
            N30 G0 G54 X=X_POS Z=Z_POS;

            IF FERRAMENTA_DESB <> FERRAMENTA_ACAB
                T=FERRAMENTA_ACAB;
            ENDIF

            MSG("PASSE DE ACABAMENTO: 1 DE 1");
                            
            N40 G0 X=DIAMETRO_FINAL Z=APRZ;
            N50 G1 Z=ESPESSURA FB=AVANCO_ACAB {modo_avanco};
            N60 G1 X=DIAMETRO_INICIAL FB=AVANCO_ACAB {modo_avanco};

            MSG("");
            N70 G0 G54 X=X_POS Z=Z_POS;

            FIM_ACABAMENTO:
            N80 RET;''')
        
            return self.__file_desbastep
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro: ao gerar o arquivo de ciclo de desbaste padrão, revise os campos de entrada e tente novamente!\n\n{e}')
            raise ValueError(e)
        
    # Método responsável por armazenar o arquivo de ciclo de desbaste zigzag em atributo
    def create_desbaste_zig(self):
        try:
            modo_avanco = self.jsonC.get_data(self.jsonC.data_advance, 'modo_avanco')

            self.__file_desbastez = textwrap.dedent(f'''
            N10 G0 X=APRX Z=APRZ;
            N20 G0 X=DIAMETRO_INICIAL;

            WHILE R0 <= R5
                MSG(" - DESBASTE EM ANDAMENTO...")
                G1 X=IC(PASSE) F=AVANCO_DESB {modo_avanco}
                G1 Z=ESPESSURA
                R0 = R0 + 1
                G1 X=IC(PASSE)
                G1 Z=APRZ
                R0 = R0 + 1
            ENDWHILE

            INICIO_ACABAMENTO:

            MSG("");
            N30 G0 G54 X=X_POS Z=Z_POS;

            IF FERRAMENTA_DESB <> FERRAMENTA_ACAB
                T=FERRAMENTA_ACAB;
            ENDIF

            N40 G0 X=DIAMETRO_FINAL Z=APRZ;
            N50 G1 Z=ESPESSURA FB=AVANCO_ACAB {modo_avanco};
            N60 G1 X=DIAMETRO_INICIAL FB=AVANCO_ACAB {modo_avanco};

            N70 G0 G54 X=X_POS Z=Z_POS;

            FIM_ACABAMENTO:
            N80 RET;''')
        
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