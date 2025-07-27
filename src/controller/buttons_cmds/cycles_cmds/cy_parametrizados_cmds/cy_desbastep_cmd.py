import json
from tkinter import messagebox

from src.model.assents import Assents

class DesbastePCmds:

    txt = 'Escolha um nome de pasta para salvar o seu ciclo/projeto:'

    def __init__(self, master):
        self.__master = master
        self.__assents = Assents(self.__master)

    # Método responsável por fazer a chamada da tela de parâmetros de corte
    def call_parameters(self):
        try:
            from src.view.view_parameters import ViewParameters
            view_parameters = ViewParameters()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na chamada da tela de parâmetros de corte:\n\n{e}')
            raise ValueError(f'Erro na chamada da tela de parâmetros de corte: {e}')

    # Método responsável por fazer a chamada da tela de posicionamentos dos parametrizados
    def call_positioning(self):
        try:
            from src.view.view_pos.view_posp import ViewPosp
            view_posp = ViewPosp()
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Aconteceu um erro inesperado no momento de chamar a tela de posicionamentos:\n\n{e}')
            raise ValueError(f'Aconteceu um erro inesperado no momento de chamar a tela de posicionamentos: {e}')

    # Método responsável por fazer a chamada da tela de configuração de rotações
    def call_rotations(self):
        try:
            from src.view.view_menus.cy_parametrizados.view_rpm_desbp_men import ViewRpmDesbasp_Men
            view_rpm = ViewRpmDesbasp_Men()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Aconteceu um erro inesperado no momento de chamar a tela de configuração de velocidade de corte:\n\n{e}')
            raise ValueError(f'Aconteceu um erro inesperado no momento de chamar a tela de configuração de velocidade de corte: {e}')

    # Método responsável por liberar a alteração de dimensões
    def unlock_dimension(self):
        try:
            self.__master.combo_pro.configure(state='readonly')
            self.__master.check_pro.configure(state='disabled')

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de liberar a alteração de dimensão:\n\n{e}')
            raise ValueError(f'Erro no momento de liberar a alteração de dimensão: {e}')
        
    # Método responsável por liberar a alteração do readme user
    def unlock_readme(self):
        try:
            self.__master.combo_rea.configure(state='readonly')
            self.__master.check_rea.configure(state='disabled')

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de liberar a alteração do readme user:\n\n{e}')
            raise ValueError(f'Erro no momento de liberar a alteração do readme user: {e}')

    # Método responsável por carregar os dados do ciclo do json
    def load_json(self):
        try:
            from src.model.json_handler import JsonHandler

            self.json = JsonHandler()
            self.json.convert_files()

            # Seção de carregamento de dados de posicionamentos
            self.posx = self.json.get_data(self.json.data_pos, 'posx')
            self.posz = self.json.get_data(self.json.data_pos, 'posz')
            self.aprx = self.json.get_data(self.json.data_pos, 'aprx')
            self.aprz = self.json.get_data(self.json.data_pos, 'aprz')

            # Seção de carregamento de dados de parâmetros de corte
            self.ferra = self.json.get_data(self.json.data_parameters, 'ferramenta')
            self.avanc = self.json.get_data(self.json.data_parameters, 'avanco')
            self.passe = self.json.get_data(self.json.data_parameters, 'passe')
            self.lirpm = self.json.get_data(self.json.data_parameters, 'lim')
            self.marpm = self.json.get_data(self.json.data_parameters, 'rpm')
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de carregar os valores do ciclo:\n\n{e}')
            raise ValueError(f'Erro no momento de carregar os valores do ciclo: {e}')

    # Método responsável por abrir a tela de verificação de dados do ciclo
    def view_gcode(self):
        try:
            from src.view.view_verification.cycles_parametrizados.view_verification_desbastep import ViewVerificationDesbasteP

            # Seção de conversão de dados de entrys do ciclo
            self.dii_parcial = float(self.__master.entry_dii.get()) # Conversão do campo de entry - diâmetro inicial
            self.dif_parcial = float(self.__master.entry_dif.get()) # Conversão do campo de entry - diâmetro final
            self.esp_parcial = float(self.__master.entry_esp.get()) # Conversão do campo de entry - espessura

            self.load_json() # Carrega os dados do método json
            self.view_verif = ViewVerificationDesbasteP()

            # Seção de inserção de dados json aos entrys da tela de verificação
            self.view_verif.entry_dii.insert('0', self.dii_parcial)
            self.view_verif.entry_dif.insert('0', self.dif_parcial)
            self.view_verif.entry_esp.insert('0', self.esp_parcial)

            self.view_verif.entry_pox.insert('0', self.posx)
            self.view_verif.entry_poz.insert('0', self.posz)
            self.view_verif.entry_apx.insert('0', self.aprx)
            self.view_verif.entry_apz.insert('0', self.aprz)

            self.view_verif.entry_fea.insert('0', self.ferra)
            self.view_verif.entry_fed.insert('0', self.ferra)

            self.view_verif.entry_ava.insert('0', self.avanc)
            self.view_verif.entry_pas.insert('0', self.passe)
            self.view_verif.entry_rpm.insert('0', self.marpm)
            self.view_verif.entry_lim.insert('0', self.lirpm)

            self.view_verif.entry_sdi.insert('0', self.dii_parcial)
            self.view_verif.entry_szc.insert('0', self.esp_parcial)
            self.view_verif.entry_szs.insert('0', self.esp_parcial)

            self.view_verif.mainloop()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', 'Erro na geração do g-code, revise os campos e tente novamente!')
            print(f'Erro na geração do g-code final:\n\n{e}')

    # Método responsável por bloquear a edição dos entrys
    def validate_gcode(self):
        try:
            dii = float(self.__master.entry_dii.get())
            dif = float(self.__master.entry_dif.get())
            esp = float(self.__master.entry_esp.get())

            ava = float(self.__master.entry_ava.get())
            pas = float(self.__master.entry_pas.get())
            rpm = float(self.__master.entry_rpm.get())
            lim = float(self.__master.entry_lim.get())

            apx = float(self.__master.entry_apx.get())
            apz = float(self.__master.entry_apz.get())
            pox = float(self.__master.entry_pox.get())
            poz = float(self.__master.entry_poz.get())

            sim_espc = float(self.__master.entry_szc.get())
            sim_espu = float(self.__master.entry_szs.get())

            # Seção de validação de parâmetros de simulação
            if sim_espc < sim_espu or sim_espc < 0:
                messagebox.showerror('Compilador G-Code', 'Erro, os valores de parâmetros de simulação estão incorretos:\n\na espessura completa da peça não pode ser menor que a espessura de segurança ou igual a zero!')
                return

            # Seção de validação de parâmetros de dimensões
            if dif > dii or dif <= 0:
                messagebox.showerror('Compilador G-Code', 'Erro, os valores de dimensões estão incorretos:\n\no diâmetro final não pode ser maior que o diâmetro inicial ou igual a zero!')
                return

            if esp <= 0:
                messagebox.showerror('Compilador G-Code', 'Erro, os valores de parâmetros de dimensões estão incorretos:\n\no valor da espessura não pode ser menor ou igual a zero!')
                return

            # Seção de validação de parâmetros de corte
            if ava <= 0:
                messagebox.showerror('Compilador G-Code', 'Erro, os valores de parâmetros de corte estão incorretos:\n\no valor de avanço não pode ser menor ou igual a zero!')
                return
            
            if pas <= 0:
                messagebox.showerror('Compilador G-Code', 'Erro, os valores de parâmetros de corte estão incorretos:\n\no valor do passe de profundidade não pode ser menor ou igual a zero!')
                return

            if rpm > lim or rpm <= 0:
                messagebox.showerror('Compilador G-Code', 'Erro, os valores de parâmetros de corte estão incorretos:\n\no valor de rpm não pode ser maior que o limite de rpm ou igual a zero!')
                return

            # Seção de validação de parâmetros de posicionamento
            if pox <= apx:
                messagebox.showerror('Compilador G-Code', 'Erro, os valores de parâmetros de posicionamento estão incorretos:\n\no valor de posicionamento no eixo X não pode ser menor ou igual ao valor de aproximação no eixo X!')
                return

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de validar os campos que se abaixo encontra:\n\n{e}')
            raise ValueError(f'Erro no momento de validar os campos que se encontra abaixo: {e}')

        else:
            messagebox.showinfo('Compilador G-Code', 'Todos os campos foram verificados e você já pode gerar o seu ciclo de desbaste parametrizado!')

    # Método responsável por salvar o g-code do ciclo de desbaste parametrizado
    def save_gcode(self):
        try:
            from src.model.cy_desbastep import CyDesbasteP

            # Seção de conversão de entrys da tela de verificação
            self.dii_real = float(self.__master.entry_dii.get())
            self.dif_real = float(self.__master.entry_dif.get())
            self.esp_real = float(self.__master.entry_esp.get())

            self.data_cycle = {
                'diai': self.dif_real,
                'diaf': self.dif_real,
                'espe': self.esp_real,
                'fera': self.__master.entry_fea.get(),
                'ferd': self.__master.entry_fed.get(),
                'avan': self.__master.entry_ava.get(),
                'pass': self.__master.entry_pas.get(),
                'rpmp': self.__master.entry_rpm.get(),
                'lims': self.__master.entry_lim.get(),
                'posx': self.__master.entry_pox.get(),
                'posz': self.__master.entry_poz.get(),
                'aprx': self.__master.entry_apx.get(),
                'aprz': self.__master.entry_apz.get(),
                'tdim': self.__master.combo_pro.get()
            }

            self.input_dialog = self.__assents.criar_inputdialog('Compilador G-Code', 'Dê um nome à pasta do ciclo de desbaste parametrizado.')
            self.nome_project = self.input_dialog.get_input()

            if self.nome_project == '' or self.nome_project == None:
                messagebox.showerror('Compilador G-Code', 'Erro, você deve informar o nome da pasta para compilar o ciclo.')
                return
            else:
                with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_cycles/cycles_parametrizados/cycle_desbastep/configs_desbastep.json', 'w', encoding='utf-8') as file:
                    json.dump(self.data_cycle, file, indent=4, ensure_ascii=False)

                self.desbastep = CyDesbasteP(self.dii_real, self.dif_real, self.esp_real)
                self.desbastep.initialize_files()
                self.desbastep.generate_gcode(self.nome_project)

                messagebox.showinfo('Compilador G-Code', 'Seu ciclo de desbaste parametrizado foi compilado com sucesso e já está disponível em seus arquivos!')
                self.__master.destroy()

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de salvar o g-code do ciclo de desbaste parametrizado:\n\n{e}')
            raise ValueError(f'Erro no momento de salvar o g-code do ciclo de desbaste parametrizado: {e}')