import json
from tkinter import messagebox

from src.model.json_handler import JsonHandler

class ParametersCmds:

    def __init__(self, master):
        self.__master = master
        self.__json = JsonHandler()
        self.__json.convert_files()

    # Método responsável por inserir os parâmetros de corte padrão
    def insert_parameters(self):
        try:
            self.__master.entry_rp.delete(0, 'end')
            self.__master.entry_av.delete(0, 'end')

            self.__master.combo_se.set(self.__json.get_data(self.__json.data_machine, 'sentido_rotação'))
            self.__master.entry_rp.insert(0, self.__json.get_data(self.__json.data_standard, 'rpm'))
            self.__master.entry_av.insert(0, self.__json.get_data(self.__json.data_standard, 'ava'))

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na implementação dos parâmetros de corte padrão:\n\n{e}')
            raise ValueError(f'Erro na implementação dos parâmetros de corte padrão: {e}!')

    # Método responsável por salvar os parâmetros de corte do usuário em json
    def save_parameters(self):
        try:
            self.dic_parameters = {
                "ferramenta": self.__master.combo_fr.get(),
                "sentido": self.__master.combo_se.get(),
                "avanco": self.__master.entry_av.get(),
                "passe": self.__master.entry_ps.get(),
                "rpm": self.__master.entry_rp.get() 
            }

            if '' in self.dic_parameters.values():
                messagebox.showerror('Compilador G-Code', 'Não foi possível salvar os parâmetros de corte, verifique se todos os campos estão preenchidos.')
            else:
                with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_parametros.json', 'w') as file:
                    json.dump(self.dic_parameters, file, indent=4, ensure_ascii=False)
                    messagebox.showinfo('Compilador G-Code', 'Os seus parâmetros de corte foram configurados com sucesso!')
                    self.__master.destroy()                    
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Ocorreu um erro no momento de salvar os seus parâmetros de corte:\n\n{e}')
            print(f'Erro na geração do arquivo de configuração de parâmetros de corte do usuário:{e}!')