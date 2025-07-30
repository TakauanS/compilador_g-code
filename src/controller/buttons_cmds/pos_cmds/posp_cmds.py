import json
from tkinter import messagebox

class PospCmds:

    def __init__(self, master):
        try:
            self.__master = master

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de chamar a classe de comandos dos posicionamentos:\n\n{e}')
            raise ValueError(f'Erro no momento de chamar a classe de comandos dos posicionamentos: {e}')
        
    # Método responsável por salvar os posicionamentos
    def save_positioning(self):
        try:
            self.dic_positioning = {
                "posx": self.__master.entry_posx.get(),
                "posz": self.__master.entry_posz.get(),
                "aprx": self.__master.entry_aprx.get(),
                "aprz": self.__master.entry_aprz.get()
            }

            if '' in self.dic_positioning.values():
                messagebox.showerror('Compilador G-Code', 'Erro no momento de salvar os posicionamentos do usuário:\n\n- os campos acima não podem ficar em branco.')
                return
            else:
                with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_main/configs_pos.json', 'w', encoding='utf-8') as file:
                    json.dump(self.dic_positioning, file, indent=4, ensure_ascii=False)
                    messagebox.showinfo('Compilador G-Code', 'Os seus posicionamentos foram configurados com sucesso!')
                    self.__master.destroy()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de salvar os posicionamentos do usuário:\n\n{e}')
            raise ValueError(f'Erro no momento de salvar os posicionamentos do usuário: {e}')