import json

class JsonMain:

    def __init__(self):
        try:
            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_main/configs_parametros.json', 'r', encoding='utf-8') as file:
                self.__data_parametros = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_main/configs_programa.json', 'r', encoding='utf-8') as file:
                self.__data_programa = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_main/configs_usuario.json', 'r', encoding='utf-8') as file:
                self.__data_user = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_main/configs_maquina.json', 'r', encoding='utf-8') as file:
                self.__data_maquina = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_main/configs_padrao.json', 'r', encoding='utf-8') as file:
                self.__data_padrao = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_main/configs_pos.json', 'r', encoding='utf-8') as file:
                self.__data_pos = json.load(file)

        except Exception as e:
            raise Exception(f'Aconteceu um erro inesperado no momento de carregar os dados json principais do software: {e}')
        
    # Método responsável por retornar os dados de configuração do software
    def get_data(self, dictionary: str, data: str):
        try:            
            if not isinstance(data, str):
                raise TypeError('O tipo de dado para data deve ser do tipo de dado String!')

            return dictionary[data]
        
        except Exception as e:
            raise Exception(f'Aconteceu um erro no momento de buscar os dados json do software: {e}')

    @property
    def data_parametros(self):
        return self.__data_parametros

    @property
    def data_programa(self):
        return self.__data_programa

    @property
    def data_user(self):
        return self.__data_user

    @property
    def data_maquina(self):
        return self.__data_maquina

    @property
    def data_padrao(self):
        return self.__data_padrao

    @property
    def data_pos(self):
        return self.__data_pos 