import json
from tkinter import messagebox

class ParametersCmds:

    def __init__(self, master):
        self.__master = master

    # Método responsável por salvar os parâmetros de corte do usuário em json
    def save_parameters(self):
        try:
            self.dic_parameters = {
                "ferramenta": self.__master.combo_fr.get(),
                "sentido": self.__master.combo_se.get(),
                "avanco": self.__master.entry_av.get(),
                "passe": self.__master.entry_ps.get(),
                "modo": self.__master.combo_md.get() 
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