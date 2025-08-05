import customtkinter as ctk
from tkinter import messagebox, Menu

from src.model.assents import Assents
from src.controller.buttons_cmds.cycles_cmds.cy_parametrizados_cmds.cy_desbastep_cmd import DesbastePCmds

class ViewVerificationDesbasteP(ctk.CTkToplevel):

    cor1 = '#FFFFFF'
    cor2 = '#1A8AE5'
    cor3 = '#3757A0'
    cor4 = '#000000'
    cor5 = '#adadad'

    def __init__(self):
        try:
            super().__init__()

            self.__assents = Assents(self)
            self.__cmds = DesbastePCmds(self)

            self.geometry('850x470')
            self.title('Compilador G-Code | Verificação de Dados')
            self.resizable(False, False)
            self.grab_set() # Dar foco máximo a tela de verificação
        
            # SEÇÃO DE FRAMEs E LABELFRAMEs
            self.fra_p = self.__assents.criar_frame(10, 10, 430, 830, 0, 1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, self)

            self.fra_dim = self.__assents.criar_labelframe(10, 3, 340, 150, 'Dimensões da Peça', ViewVerificationDesbasteP.cor1, self.fra_p)
            self.fra_sim = self.__assents.criar_labelframe(10, 155, 340, 265, 'Parâmetros de Simulação', ViewVerificationDesbasteP.cor1, self.fra_p)
            self.fra_par = self.__assents.criar_labelframe(360, 3, 460, 150, 'Parâmetros de Cortes', ViewVerificationDesbasteP.cor1, self.fra_p)
            self.fra_pos = self.__assents.criar_labelframe(360, 155, 460, 110, 'Posicionamentos da Ferramenta', ViewVerificationDesbasteP.cor1, self.fra_p)
            self.fra_out = self.__assents.criar_labelframe(360, 267, 460, 152, 'Outros', ViewVerificationDesbasteP.cor1, self.fra_p)

            # SEÇÃO DE MENU BAR
            self.menu = Menu(self)
            self.menu_arquivo = Menu(self.menu, tearoff=0) # Menu para arquivo
            self.menu_configs = Menu(self.menu, tearoff=0) # Menu para configurações
            self.menu_avancad = Menu(self.menu_configs, tearoff=0) # Menu para opções avançadas
            self.menu_paramet = Menu(self.menu_avancad, tearoff=0) # Menu para parâmetros de corte

            self.menu_arquivo.add_command(label='SALVAR DADOS .txt')
            self.menu_arquivo.add_command(label='GERAR G-CODE', command=self.__cmds.save_gcode)
            self.menu_arquivo.add_command(label='VOLTAR', command=self.destroy)
            self.menu.add_cascade(label='ARQUIVO', menu=self.menu_arquivo)

            self.menu_configs.add_command(label='VALIDAR G-CODE', command=self.__cmds.validate_gcode)
            self.menu_configs.add_cascade(label='AVANÇADOS', menu=self.menu_avancad)
            self.menu.add_cascade(label='CONFIGURAÇÕES', menu=self.menu_configs)

            self.menu_avancad.add_cascade(label='PARÂMETROS DE CORTE', menu=self.menu_paramet)
            self.menu_avancad.add_command(label='POSICIONAMENTOS')
            self.menu_avancad.add_command(label='OFFSET')

            self.menu_paramet.add_command(label='ROTAÇÃO', command=self.__cmds.call_rotations)
            self.menu_paramet.add_command(label='AVANÇO', command=self.__cmds.call_advance)

            # SEÇÃO DE LABELs
            self.label_dii = self.__assents.criar_label('DIÂMETRO INICIAL:', 10, 5, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_dim)
            self.label_dif = self.__assents.criar_label('DIÂMETRO FINAL:', 10, 45, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_dim)
            self.label_esp = self.__assents.criar_label('ESPESSURA:', 10, 85, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_dim)
            
            self.label_ava = self.__assents.criar_label('AVANÇO (F):', 10, 5, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_par)
            self.label_pas = self.__assents.criar_label('PASSE (Ap):', 240, 5, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_par)
            self.label_rpm = self.__assents.criar_label('ROT. (RPM):', 10, 45, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_par)
            self.label_lim = self.__assents.criar_label('LIM. (RPM):', 240, 45, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_par)
            self.label_fed = self.__assents.criar_label('FER. DESB:', 10, 85, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_par)
            self.label_fea = self.__assents.criar_label('FER. ACAB:', 240, 85, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_par)

            self.label_pox = self.__assents.criar_label('POSX. SEG:', 10, 5, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_pos)
            self.label_poz = self.__assents.criar_label('POSX. SEG:', 240, 5, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_pos)
            self.label_apx = self.__assents.criar_label('APRX. SEG:', 10, 45, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_pos)
            self.label_apz = self.__assents.criar_label('APRZ. SEG:', 240, 45, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_pos)

            self.label_rea = self.__assents.criar_label('README USER:', 10, 45, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_out)
            self.label_pro = self.__assents.criar_label('DIMENSÕES EM:', 10, 5, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_out)

            self.label_sdi = self.__assents.criar_label('DIÂMETRO INICIAL:', 10, 5, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_sim)
            self.label_szc = self.__assents.criar_label('ESPESSURA CMP:', 10, 45, 0, 'ESPESSURA COMPLETA', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_sim)
            self.label_szs = self.__assents.criar_label('ESPESSURA USI:', 10, 85, 0, 'ESPESSURA USINÁVEL', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_sim)

            # SEÇÃO DE COMBOBOXs
            self.combo_rea = self.__assents.criar_combobox(150, 43, self.fra_out, 220, 10, ('SIM', 'NÃO'), 'center', 'disabled')
            self.combo_pro = self.__assents.criar_combobox(150, 3, self.fra_out, 220, 10, ('DIÂMETRO', 'RAIO'), 'center', 'disabled')

            # SEÇÃO DE ENTRYs
            self.entry_dii = self.__assents.criar_entry(170, 5, 150, 1, 'center', self.fra_dim)
            self.entry_dif = self.__assents.criar_entry(170, 45, 150, 1, 'center', self.fra_dim)
            self.entry_esp = self.__assents.criar_entry(170, 85, 150, 1, 'center', self.fra_dim)

            self.entry_ava = self.__assents.criar_entry(120, 5, 100, 1, 'center', self.fra_par)
            self.entry_pas = self.__assents.criar_entry(340, 5, 100, 1, 'center', self.fra_par)
            self.entry_rpm = self.__assents.criar_entry(120, 45, 100, 1, 'center', self.fra_par)
            self.entry_lim = self.__assents.criar_entry(340, 45, 100, 1, 'center', self.fra_par)
            self.entry_fed = self.__assents.criar_entry(120, 85, 100, 1, 'center', self.fra_par)
            self.entry_fea = self.__assents.criar_entry(340, 85, 100, 1, 'center', self.fra_par)

            self.entry_pox = self.__assents.criar_entry(120, 5, 100, 1, 'center', self.fra_pos)
            self.entry_poz = self.__assents.criar_entry(340, 5, 100, 1, 'center', self.fra_pos)
            self.entry_apx = self.__assents.criar_entry(120, 45, 100, 1, 'center', self.fra_pos)
            self.entry_apz = self.__assents.criar_entry(340, 45, 100, 1, 'center', self.fra_pos)

            self.entry_sdi = self.__assents.criar_entry(170, 5, 150, 1, 'center', self.fra_sim)
            self.entry_szc = self.__assents.criar_entry(170, 45, 150, 1, 'center', self.fra_sim)
            self.entry_szs = self.__assents.criar_entry(170, 85, 150, 1, 'center', self.fra_sim)

            # SEÇÃO DE CHECKBOXs
            self.check_pro = self.__assents.criar_checkbox(380, 5, self.__cmds.unlock_dimension, self.fra_out)
            self.check_rea = self.__assents.criar_checkbox(380, 45, self.__cmds.unlock_readme, self.fra_out)

            self.config(bg=ViewVerificationDesbasteP.cor1, menu=self.menu)

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de carregar a tela de verificação de dados de ciclo:\n\n{e}')
            raise ValueError(f'Erro no momento de carregar a tela de verificação de dados de ciclo: {e}')