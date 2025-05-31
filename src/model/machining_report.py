from docx import Document
from datetime import date
from tkinter import messagebox

from src.model.json_handler import JsonHandler

class MachiningReport:
    
    def __init__(self, ordem: str, material: str):
        try:
            self._ordem = ordem
            self._material = material

            self.__json = JsonHandler()
            self.__json.convert_files()

            self._doc = Document('C:/Users/USUARIO/Documents/Compilador G-Code/docs/Relatório de Usinagem CNC.docx')

            self._references = {
                'DD/MM/AAAA': str(date.today()),
                'NOME': self.__json.get_data(self.__json.data_user, 'usuario'),
                'EMPRESA': self.__json.get_data(self.__json.data_user, 'empresa'),
                'MAQUINA': self.__json.get_data(self.__json.data_user, 'modelo'),
                'ORDEM': self._ordem,
                'MATERIAL': self._material,
                'FERRAMENTA': self.__json.get_data(self.__json.data_parameters, 'ferramenta'),
                'SPINDLE': self.__json.get_data(self.__json.data_parameters, 'rpm'),
                'PASSE': self.__json.get_data(self.__json.data_parameters, 'passe'),
                'AVANÇO': self.__json.get_data(self.__json.data_parameters, 'avanco')
                }

        except Exception as e:
            raise ValueError(f'Erro na importação dos dados necessários para o relatório de usinagem cnc:{e}')
        
    # Método responsável por gerar o relatório de usinagem cnc
    def create_report(self, directoy: str):
        try:
            if '' in self._references.values():
                messagebox.showerror('Compilador G-Code', 'Erro na geração do relatório de usinagem: observe se todos os campos estão preenchidos')
                raise ValueError('Erro na geração do relatório de usinagem.')
            else:
                for paragraphs in self._doc.paragraphs:
                    for run in paragraphs.runs:
                        for key, value in self._references.items():
                            if key in run.text:
                                run.text = run.text.replace(key, value)
        except Exception as e:
            raise ValueError(f'Erro no momento da geração do relatório de usinagem cnc:{e}')           
        else:
            self._doc.save(f'{directoy}/Relatório de Usinagem CNC.docx')
            print(' - O Relatório de Usinagem CNC foi gerado com sucesso!')