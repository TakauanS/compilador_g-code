from docx import Document
from datetime import date

from src.model.json_handler import JsonHandler

class MachiningReport:
    
    def __init__(self, ordem, material):
        try:
            self._ordem = ordem
            self._material = material

            self.__json = JsonHandler()
            self.__json.convert_files()

            self._doc = Document('C:/Users/USUARIO/Documents/Compilador G-Code/Relatório de Usinagem CNC.docx')

            self._references = {
                'DD/MM/AAAA': str(date.today()),
                'NOME': self.__json.get_data(self.__json.data_user, 'usuário'),
                'EMPRESA': self.__json.get_data(self.__json.data_user, 'empresa'),
                'MAQUINA': self.__json.get_data(self.__json.data_user, 'modelo'),
                'ORDEM': self._ordem,
                'MATERIAL': self._material,
                'FERRAMENTA': self.__json.get_data(self.__json.data_parameters, 'ferramenta'),
                'SPINDLE': self.__json.get_data(self.__json.data_parameters, 'rpm'),
                'PASSE': self.__json.get_data(self.__json.data_parameters, 'passe'),
                }

        except Exception as e:
            raise ValueError(f'Erro na importação dos dados necessários para o relatório de usinagem cnc:{e}')
        
    # Método responsável por gerar o relatório de usinagem cnc
    def create_report(self):
        try:
            for paragraphs in self._doc.paragraphs:
                for run in paragraphs.runs:
                    for key, value in self._references.items():
                        if key in run.text:
                            run.text = run.text.replace(key, value)

        except Exception as e:
            raise ValueError(f'Erro no momento da geração do relatório de usinagem cnc:{e}')
        
        else:
            self._doc.save(f'{self.__json.get_data(self.__json.data_file, 'diretório')}/Relatório de Usinagem CNC.docx')
            print('Tudo rodou redondinho!')