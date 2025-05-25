import json
from tkinter import filedialog, messagebox, END

from src.view.view_main_screen import MainScreen

class SetupManagerCmds:

    def __init__(self, master):
        self.__master = master

    # Método responsável por abrir tela para escolher um diretório
    def open_directory(self):
        try:
            self.directory = filedialog.askdirectory(title='Selecione a sua pasta NC')
            self.__master.entry_prc.delete(0, END)
            self.__master.entry_prc.insert(0, self.directory)

            print(f' - Pasta destina para os arquivos G-code: {self.directory}')
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro ao abrir o caminho dos diretórios:\n\n{e}')
            print(f'Erro! {e}')

    # Método responsável por capturar valores dos entrys e gerar os json
    def capture_values(self):
        try:
            self.__master.dic_user = {
                'usuário': self.__master.entry_user.get(),
                'empresa': self.__master.entry_empr.get(),
                'modelo': self.__master.com_modelo.get()
            }

            self.__master.dic_file = {
                'diretório': self.__master.entry_prc.get(),
                'extensão': self.__master.com_extens.get(),
                'contador': self.__master.com_contad.get(),
                'estilo': self.__master.com_estilo.get(),
                'readme': self.__master.strv_read.get(),
                'save_p': self.__master.strv_save.get(),
            }

            self.__master.dic_mach = {
                'sentido_rotação': self.__master.com_sentid.get(),
                'estilo_torre': self.__master.com_torres.get(),
                'offset': self.__master.com_offset.get()
            }

            self.__master.dic_padr = {
                'posx': self.__master.entry_posx.get(),
                'posz': self.__master.entry_posz.get(),
                'rpm': self.__master.entry_rpmn.get(),
                'ava': self.__master.entry_avan.get()
            }

            if '' in self.__master.dic_user.values() or '' in self.__master.dic_file.values() or '' in self.__master.dic_mach.values() or '' in self.__master.dic_padr:
                messagebox.showerror('Compilador G-Code', 'Um ou mais campos estão vazios, preencha todos os campos para prosseguir com a operação.')
            else:
                with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_usuario.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(self.__master.dic_user, arquivo, indent=4, ensure_ascii=False)

                with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_programa.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(self.__master.dic_file, arquivo, indent=4, ensure_ascii=False)

                with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_maquina.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(self.__master.dic_mach, arquivo, indent=4, ensure_ascii=False)

                with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_padrao.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(self.__master.dic_padr, arquivo, indent=4, ensure_ascii=False)

                messagebox.showinfo('Compilador G-Code', 'Os dados foram compilados e armazenados com sucesso no sistema')

            self.__master.destroy()
            self.__mainscreen = MainScreen()
            self.__mainscreen.mainloop()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na captura dos valores para configurar as suas informações:\n\n{e}')
            print(f'Erro! {e}')