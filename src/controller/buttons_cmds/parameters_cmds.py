import json
from tkinter import messagebox

from src.model.json_manager.json_main import JsonMain

class ParametersCmds:

    def __init__(self, master):
        self.__master = master
        self.json = JsonMain()

    # Método responsável por inserir os parâmetros de corte padrão
    def insert_parameters(self):
        try:
            self.__master.entry_rpm.delete(0, 'end')
            self.__master.entry_avan.delete(0, 'end')

            self.__master.com_sent.set(self.json.get_data(self.json.data_maquina, 'sentido_rotacao'))
            self.__master.entry_rpm.insert(0, self.json.get_data(self.json.data_padrao, 'rpm'))
            self.__master.entry_avan.insert(0, self.json.get_data(self.json.data_padrao, 'ava'))

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na implementação dos parâmetros de corte padrão:\n\n{e}')
            raise ValueError(f'Erro na implementação dos parâmetros de corte padrão: {e}!')

    # Método responsável por salvar os parâmetros de corte do usuário em json
    def save_parameters(self):
        try:
            self.dic_parameters = {
                "ferramenta": self.__master.com_ferr.get(),
                "sentido": self.__master.com_sent.get(),
                "avanco": self.__master.entry_avan.get(),
                "passe": self.__master.entry_pass.get(),
                "modo": self.__master.com_modo.get(),
                "rpm": self.__master.entry_rpm.get(),
                "lim": self.__master.entry_lim.get() 
            }

            if '' in self.dic_parameters.values():
                messagebox.showerror('Compilador G-Code', 'Não foi possível salvar os parâmetros de corte, verifique se todos os campos estão preenchidos.')
            else:
                with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_main/configs_parametros.json', 'w', encoding='utf-8') as file:
                    json.dump(self.dic_parameters, file, indent=4, ensure_ascii=False)
                    messagebox.showinfo('Compilador G-Code', 'Os seus parâmetros de corte foram configurados com sucesso!')
                    self.__master.destroy()                   
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Ocorreu um erro no momento de salvar os seus parâmetros de corte:\n\n{e}')
            print(f'Erro na geração do arquivo de configuração de parâmetros de corte do usuário:{e}!')