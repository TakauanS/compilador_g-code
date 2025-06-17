import customtkinter as ctk
from tkinter import messagebox, Menu

from src.model.assents import Assents
from src.controller.buttons_cmds.cycles_cmds.cy_parametrizados_cmds.cy_desbastep_cmd import DesbastePCmds

class ViewVerificationDesbasteP(ctk.CTkToplevel):

    cor1 = '#FCF6F2' # Cor branca para FG-COLOR
    cor2 = '#1A8AE5' # Cor azul para butões FG-COLOR
    cor3 = '#3757A0' # Cor azul para botões HOUVER-COLOR
    cor4 = 'black'   # Cor preta para TEXT-COLOR

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
            self.fra_cod = self.__assents.criar_labelframe(10, 155, 340, 265, 'Códigos G', ViewVerificationDesbasteP.cor1, self.fra_p)
            self.fra_par = self.__assents.criar_labelframe(360, 3, 460, 150, 'Parâmetros de Cortes', ViewVerificationDesbasteP.cor1, self.fra_p)
            self.fra_pos = self.__assents.criar_labelframe(360, 155, 460, 110, 'Posicionamentos da Ferramenta', ViewVerificationDesbasteP.cor1, self.fra_p)
            self.fra_out = self.__assents.criar_labelframe(360, 267, 460, 152, 'Outros', ViewVerificationDesbasteP.cor1, self.fra_p)

            # SEÇÃO DE MENU BAR
            self.menu = Menu(self)
            self.menu_arquivo = Menu(self.menu, tearoff=0)
            self.menu_editar = Menu(self.menu, tearoff=0)

            self.menu_arquivo.add_command(label='SALVAR DADOS .txt')
            self.menu_arquivo.add_command(label='VOLTAR', command=self.destroy)
            self.menu.add_cascade(label='ARQUIVO', menu=self.menu_arquivo)

            self.menu_editar.add_command(label='DESBLOQUEAR', command=self.__cmds.unlock_entrys)
            self.menu_editar.add_command(label='BLOQUEAR', command=self.__cmds.lock_entrys)
            self.menu.add_cascade(label='EDITAR', menu=self.menu_editar)

            self.menu.add_command(label='GERAR G-CODE', command=self.__cmds.save_gcode)

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

            self.label_tip = self.__assents.criar_label('TIPO DE VARIÁVEL:', 10, 85, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_out)
            self.label_sis = self.__assents.criar_label('SISTEMA DE CÓD. G:', 10, 5, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_out)
            self.label_rea = self.__assents.criar_label('ARQUIVO DE INTRO:', 10, 45, 0, '', ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor1, ViewVerificationDesbasteP.cor4, ('Corbel', 18, 'normal'), self.fra_out)

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

            self.entry_tip = self.__assents.criar_entry(180, 85, 260, 1, 'center', self.fra_out)
            self.entry_sis = self.__assents.criar_entry(180, 5, 260, 1, 'center', self.fra_out)
            self.entry_rea = self.__assents.criar_entry(180, 45, 260, 1, 'center', self.fra_out)

            self.config(bg=ViewVerificationDesbasteP.cor1, menu=self.menu)

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro no momento de carregar a tela de verificação de dados de ciclo:\n\n{e}')
            raise ValueError(f'Erro no momento de carregar a tela de verificação de dados de ciclo: {e}')