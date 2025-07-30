import json

class JsonDesbasteP:

    def __init__(self):
        try:
            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_cycles/cycles_parametrizados/cycle_desbastep/configs_desbastep.json', 'r', encoding='utf-8') as file:
                self.__data_desbastep = json.load(file)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_cycles/cycles_parametrizados/cycle_desbastep/configs_rotations.json', 'r', encoding='utf-8') as file:
                self.__data_rotations = json.load(file)

        except Exception as e:
            raise Exception(f'Erro ao inicializar os dados json do ciclo de desbaste parametrizado: {e}')

    # Método responsável por retornar os dados de configuração do ciclo
    def get_data(self, dictionary: str, data: str):
        try:
            if not isinstance(data, str):
                raise TypeError('O tipo de valor deve ser do tipo String!')
            
            return dictionary[data]
        
        except Exception as e:
            raise Exception(f'Erro no momento de retornar os dados do ciclo de debaste parametrizado: {e}')

    # Retorna os dados principais do ciclo
    @property
    def data_desbastep(self):
        return self.__data_desbastep
    
    # Retorna os dados de rotações do fuso
    @property
    def data_rotations(self):
        return self.__data_rotations