import customtkinter as ctk
from src.model.assents import Assents

from src.controller.buttons_cmds.setup_manager_cmds import SetupManagerCmds

class SetupManager(ctk.CTk):

    cor1 = '#E3E2E1' # Cor branca de FG-COLOR
    cor2 = '#FCF6F2' # Cor branca de FG-COLOR para textos

    def __init__(self):
        super().__init__()

        self.__assents = Assents(self)
        self.__cmds = SetupManagerCmds(self)

        self.geometry('900x500')
        self.title('Compilador G-Code | Setup')
        self.config(bg=SetupManager.cor1)
        self.resizable(False, False)

        self.iconbitmap('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/favicon.ico')

        # SEÇÃO DE STRINGVARs
        self.strv_read = ctk.StringVar(value='OP') # StringVar para o radiobutton (Criar Readme)
        self.strv_save = ctk.StringVar(value='OP') # StringVar para o radiobutton (Salvar Pen)

        # SEÇÃO DE FRAMEs e LABELFRAMEs
        self.frame = ctk.CTkFrame(self, corner_radius=15, width=870, height=420, fg_color=SetupManager.cor2, bg_color=SetupManager.cor1).place(x=15, y=60)

        self.frame_file = self.__assents.criar_labelframe(30, 215, 400, 210, 'Dados de Programa', SetupManager.cor2, self.frame)
        self.frame_user = self.__assents.criar_labelframe(30, 65, 400, 145, 'Dados do Usuário', SetupManager.cor2, self.frame)

        self.frame_maq = self.__assents.criar_labelframe(440, 65, 430, 145, 'Dados da Máquina', SetupManager.cor2, self.frame)
        self.frame_pos = self.__assents.criar_labelframe(440, 215, 430, 105, 'Dados de Posição de Segurança', SetupManager.cor2, self.frame)

        self.frame_pdr = self.__assents.criar_labelframe(440, 320, 430, 105, 'Dados de Corte Padrão', SetupManager.cor2, self.frame)

        # SEÇÃO DE LABELs
        self.label_user = self.__assents.criar_label('PROGRAMADOR:', 5, 5, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_user)
        self.label_empr = self.__assents.criar_label('EMPRESA (OP):', 5, 40, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_user)
        self.label_mode = self.__assents.criar_label('MODELO MÁQ:', 5, 75, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_user)

        self.label_exte = self.__assents.criar_label('EXTENSÃO FILE:', 5, 5, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)
        self.label_cont = self.__assents.criar_label('CONT. DE PASS:', 5, 40, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)
        self.label_read = self.__assents.criar_label('CRIAR README:', 5, 145, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)
        self.label_savp = self.__assents.criar_label('SALVAR EM PEN:', 5, 110, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)
        self.label_styl = self.__assents.criar_label('SINTAXE GCODE:', 5, 75, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)

        self.label_torr = self.__assents.criar_label('TIPO DE TORRE:', 5, 5, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_maq)
        self.label_refe = self.__assents.criar_label('WORK OFFSET:', 5, 40, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_maq)
        self.label_sent = self.__assents.criar_label('SENTIDO DE ROT:', 5, 75, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_maq)

        self.label_posx = self.__assents.criar_label('POSIÇÃO EM X:', 5, 5, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_pos)
        self.label_posz = self.__assents.criar_label('POSIÇÃO EM Z:', 5, 40, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_pos)

        self.label_rpmn = self.__assents.criar_label('ROTAÇÕES P/MIN:', 5, 5, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_pdr)
        self.label_avan = self.__assents.criar_label('AVANÇO DE CORT:', 5, 40, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_pdr)

        # SEÇÃO DE COMBOBOXs
        self.com_modelo = self.__assents.criar_combobox(165, 75, self.frame_user, 220, values=('Siemens 828D', 'Siemens 810D', 'Siemens 840Di'))
        self.com_extens = self.__assents.criar_combobox(165, 5, self.frame_file, 220, values=('.txt', '.nc', '.mpf', '.spf'))
        self.com_contad = self.__assents.criar_combobox(165, 40, self.frame_file, 220, values=('Sim', 'Não'))
        self.com_estilo = self.__assents.criar_combobox(165, 75, self.frame_file, 220, values=('G0 - (Rápido)', 'G00 - (Detalhado)'))

        self.com_torres = self.__assents.criar_combobox(175, 5, self.frame_maq, 245, values=('SISTEMA FIXO', 'SISTEMA GANG'))
        self.com_sentid = self.__assents.criar_combobox(175, 75, self.frame_maq, 245, values=('SENTIDO - HR', 'SENTIDO - AHR'))
        self.com_offset = self.__assents.criar_combobox(175, 40, self.frame_maq, 245, values=('G54', 'G55', 'G56', 'G57', 'G58', 'G59'))

        # SEÇÃO DE RADIOBUTTONs
        self.rad_readm1 = self.__assents.criar_radionbutton(165, 145, 'SIM', 'SIM', self.strv_read, frame=self.frame_file)
        self.rad_readm2 = self.__assents.criar_radionbutton(250, 145, 'NÃO', 'NÃO', self.strv_read, width=60, frame=self.frame_file)
        self.rad_readm3 = self.__assents.criar_radionbutton(335, 145, 'OP', 'OP', self.strv_read, width=60, frame=self.frame_file)

        self.rad_savep1 = self.__assents.criar_radionbutton(165, 110, 'SIM', 'SIM', self.strv_save, frame=self.frame_file)
        self.rad_savep2 = self.__assents.criar_radionbutton(250, 110, 'NÃO', 'NÃO', self.strv_save, width=60, frame=self.frame_file)
        self.rad_savep3 = self.__assents.criar_radionbutton(335, 110, 'OP', 'OP', self.strv_save, width=60, frame=self.frame_file)

        # SEÇÃO DE ENTRYs
        self.entry_empr = self.__assents.criar_entry(165, 40, 220, 1, self.frame_user)
        self.entry_user = self.__assents.criar_entry(165, 5, 220, 1, self.frame_user)

        self.entry_posx = self.__assents.criar_entry(175, 5, 245, 1, self.frame_pos)
        self.entry_posz = self.__assents.criar_entry(175, 40, 245, 1, self.frame_pos)

        self.entry_rpmn = self.__assents.criar_entry(175, 5, 245, 1, self.frame_pdr)
        self.entry_avan = self.__assents.criar_entry(175, 40, 245, 1, self.frame_pdr)

        self.entry_prc = ctk.CTkEntry(self,
                                  height=35, 
                                  width=805, 
                                  border_width=0, 
                                  corner_radius=12, 
                                  font=('Corbel', 17),  
                                  bg_color=SetupManager.cor1, 
                                  placeholder_text='Escolha a pasta para salvar os arquivos NC...')
        self.entry_prc.place(x=15, y=10)

        # SEÇÃO DE BUTTONs
        self.but_direc = ctk.CTkButton(self,
                                       text='',
                                       width=50,
                                       height=35, 
                                       compound='right',
                                       corner_radius=13,
                                       font=('Arial', 16, 'bold'), 
                                       bg_color=SetupManager.cor1,
                                       fg_color=self.__assents.cor4, 
                                       image=self.__assents.img_pasta,
                                       hover_color=self.__assents.cor5,
                                       command=self.__cmds.open_directory).place(x=830, y=10)
        
        self.but_savec = ctk.CTkButton(self.frame,
                                       width=110,
                                       height=35, 
                                       text='SAVE',
                                       compound='right',
                                       corner_radius=13,
                                       font=('Arial', 15, 'bold'), 
                                       bg_color=SetupManager.cor2,
                                       image=self.__assents.img_up,
                                       fg_color=self.__assents.cor4, 
                                       hover_color=self.__assents.cor5,
                                       command=self.__cmds.capture_values).place(x=765, y=435)