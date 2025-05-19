import json

class JsonHandler():

    def __init__(self):

        self.__data_user = {} # Retorna dicionário com os dados do usuário
        self.__data_file = {} # Retorna dicionário com os dados do programa (arquivo)

        self.__data_machine = {}  # Retorna dicionário com os dados da máquina 
        self.__data_standard = {} # Retorna dicionário com os dados padrões

        self.__data_parameters = {} # Retorna dicionário com os dados de parâmetros de corte

    # Método responsável por conveter os arquivos json em dicionários
    def convert_files(self):
        try:
            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_parametros.json', 'r', encoding='utf-8') as file:
                self.__data_parameters = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_usuario.json', 'r', encoding='utf-8') as file:
                self.__data_user = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_programa.json', 'r', encoding='utf-8') as file:
                self.__data_file = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_maquina.json', 'r', encoding='utf-8') as file:
                self.__data_machine = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_padrao.json', 'r', encoding='utf-8') as file:
                self.__data_standard = json.load(file)

        except Exception as e:
            print(f'Erro: {e}')

    # Método responsável por fazer o retorno de valores dos dicionários
    def get_data(self, dictionary: dict, data: str):
        
        if not isinstance(dictionary, dict):
            raise TypeError('O tipo de dado para especificar o dicionário deve ser do tipo Dict!')

        if not isinstance(data, str):
            raise TypeError('O tipo de dado de para comando deve ser do tipo String!')
        
        return dictionary[data]

    @property
    def data_user(self):
        return self.__data_user

    @property
    def data_file(self):
        return self.__data_file
    
    @property
    def data_machine(self):
        return self.__data_machine
    
    @property
    def data_standard(self):
        return self.__data_standard
    
    @property
    def data_parameters(self):
        return self.__data_parameters