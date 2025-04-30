import json
import customtkinter as ctk
from src.model.assents import Assents
from src.view.main_screen import MainScreen
from tkinter import filedialog, messagebox, END

class SetupManager(ctk.CTk):

    cor1 = '#E3E2E1' # Cor branca de FG-COLOR
    cor2 = '#FCF6F2' # Cor branca de FG-COLOR para textos

    def __init__(self):
        super().__init__()

        self.__assents = Assents(self)

        self.geometry('900x500')
        self.title('Setup Compilador G-Code')
        self.config(bg=SetupManager.cor1)
        self.resizable(False, False)

        self.iconbitmap('C:/Users/USUARIO/Documents/Compilador G-Code/assets/imgs/favicon.ico')

        # SEÇÃO DE STRINGVARs

        self.strv_read = ctk.StringVar(value='OP') # StringVar para o radiobutton (Criar Readme)
        self.strv_save = ctk.StringVar(value='OP') # StringVar para o radiobutton (Salvar Pen)

        # SEÇÃO DE FRAMEs e LABELFRAMEs

        self.frame = ctk.CTkFrame(self, corner_radius=15, width=870, height=420, fg_color=SetupManager.cor2, bg_color=SetupManager.cor1).place(x=15, y=60)

        self.frame_file = self.__assents.criar_labelframe(30, 215, 400, 210, 'Dados de Programa', self.frame)
        self.frame_user = self.__assents.criar_labelframe(30, 65, 400, 145, 'Dados do Usuário', self.frame)

        self.frame_maq = self.__assents.criar_labelframe(440, 65, 430, 145, 'Dados da Máquina', self.frame)
        self.frame_pos = self.__assents.criar_labelframe(440, 215, 430, 105, 'Dados de Posição de Segurança', self.frame)

        self.frame_pdr = self.__assents.criar_labelframe(440, 320, 430, 105, 'Dados de Corte Padrão', self.frame)

        # SEÇÃO DE LABELs

        self.label_user = self.__assents.criar_label('PROGRAMADOR:', 37, 94, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_user)
        self.label_empr = self.__assents.criar_label('EMPRESA (OP):', 37, 130, fg_color=SetupManager.cor2, text_color='black', frame=self.frame)
        self.label_mode = self.__assents.criar_label('MODELO MÁQ:', 37, 166, fg_color=SetupManager.cor2, text_color='black', frame=self.frame)

        self.label_exte = self.__assents.criar_label('EXTENSÃO FILE:', 37, 245, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)
        self.label_cont = self.__assents.criar_label('CONT. DE PASS:', 37, 281, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)
        self.label_read = self.__assents.criar_label('CRIAR README:', 37, 353, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)
        self.label_savp = self.__assents.criar_label('SALVAR EM PEN:', 37, 386, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)
        self.label_styl = self.__assents.criar_label('SINTAXE GCODE:', 37, 318, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_file)

        self.label_torr = self.__assents.criar_label('TIPO DE TORRE:', 447, 94, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_maq)
        self.label_refe = self.__assents.criar_label('WORK OFFSET:', 447, 166, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_maq)
        self.label_sent = self.__assents.criar_label('SENTIDO DE ROT:', 447, 130, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_maq)

        self.label_posx = self.__assents.criar_label('POSIÇÃO EM X:', 447, 245, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_pos)
        self.label_posz = self.__assents.criar_label('POSIÇÃO EM Z:', 447, 281, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_pos)

        self.label_rpmn = self.__assents.criar_label('ROTAÇÕES P/MIN:', 447, 350, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_pdr)
        self.label_avan = self.__assents.criar_label('AVANÇO DE CORT:', 447, 386, fg_color=SetupManager.cor2, text_color='black', frame=self.frame_pdr)

        # SEÇÃO DE COMBOBOXs

        self.com_modelo = self.__assents.criar_combobox(200, 168, self.frame, 220, values=('Siemens 828D', 'Siemens 810D', 'Siemens 840Di'))
        self.com_extens = self.__assents.criar_combobox(200, 245, self.frame, 220, values=('.txt', '.nc', '.mpf', '.spf'))
        self.com_contad = self.__assents.criar_combobox(200, 281, self.frame, 220, values=('Sim', 'Não'))
        self.com_estilo = self.__assents.criar_combobox(200, 318, self.frame, 220, values=('G0 - (Rápido)', 'G00 - (Detalhado)'))

        self.com_torres = self.__assents.criar_combobox(625, 94, self.frame, 235, values=('Sistema Fixo', 'Sistema Gang'))
        self.com_sentid = self.__assents.criar_combobox(625, 130, self.frame, 235, values=('Horário', 'Anti-Horário'))
        self.com_offset = self.__assents.criar_combobox(625, 166, self.frame, 235, values=('G54', 'G55', 'G56', 'G57', 'G58', 'G59'))

        # SEÇÃO DE RADIOBUTTONs

        self.rad_readm1 = self.__assents.criar_radionbutton(200, 358, 'SIM', 'SIM', self.strv_read, frame=self.frame_file)
        self.rad_readm2 = self.__assents.criar_radionbutton(278, 358, 'NÃO', 'NÃO', self.strv_read, width=60, frame=self.frame_file)
        self.rad_readm3 = self.__assents.criar_radionbutton(355, 358, 'OP', 'OP', self.strv_read, width=60, frame=self.frame_file)

        self.rad_savep1 = self.__assents.criar_radionbutton(200, 391, 'SIM', 'SIM', self.strv_save, frame=self.frame_file)
        self.rad_savep2 = self.__assents.criar_radionbutton(278, 391, 'NÃO', 'NÃO', self.strv_save, width=60, frame=self.frame_file)
        self.rad_savep3 = self.__assents.criar_radionbutton(355, 391, 'OP', 'OP', self.strv_save, width=60, frame=self.frame_file)

        # SEÇÃO DE ENTRYs

        self.entry_empr = self.__assents.criar_entry(200, 130, 220, 1, self.frame_user)
        self.entry_user = self.__assents.criar_entry(200, 94, 220, 1, self.frame_user)

        self.entry_posx = self.__assents.criar_entry(625, 245, 235, 1, self.frame_pos)
        self.entry_posz = self.__assents.criar_entry(625, 281, 235, 1, self.frame_pos)

        self.entry_rpmn = self.__assents.criar_entry(625, 350, 235, 1, self.frame_pdr)
        self.entry_avan = self.__assents.criar_entry(625, 386, 235, 1, self.frame_pdr)

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
                                     height=35, 
                                     width=50,
                                     text='',  
                                     corner_radius=13,
                                     compound='right', 
                                     font=('Arial', 16, 'bold'),
                                     command=self.open_directory, 
                                     fg_color=self.__assents.cor4, 
                                     image=self.__assents.img_pasta,   
                                     bg_color=SetupManager.cor1, 
                                     hover_color=self.__assents.cor5).place(x=830, y=10)
        
        self.but_savec = ctk.CTkButton(self.frame,
                                     height=35, 
                                     width=110,
                                     text='SAVE',
                                     compound='right',  
                                     corner_radius=13, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up,
                                     command=self.capture_values, 
                                     fg_color=self.__assents.cor4,    
                                     bg_color='#fcf6f2', 
                                     hover_color=self.__assents.cor5).place(x=765, y=435)

    # SEÇÃO DE MÉTODOS (COMANDs) DOS BUTTONs

    def open_directory(self):

        self.directory = filedialog.askdirectory(title='Selecione a sua pasta NC')
        self.entry_prc.delete(0, END)
        self.entry_prc.insert(0, self.directory)

        print(f' - Pasta destina para os arquivos G-code: {self.directory}')

    def capture_values(self):

        self.dic_user = {
            'usuário': self.entry_user.get(),
            'empresa': self.entry_empr.get(),
            'modelo': self.com_modelo.get()
        }

        self.dic_file = {
            'diretório': self.entry_prc.get(),
            'extensão': self.com_extens.get(),
            'contador': self.com_contad.get(),
            'estilo': self.com_estilo.get(),
            'readme': self.strv_read.get(),
            'save_p': self.strv_save.get(),
        }

        self.dic_mach = {
            'sentido_rotação': self.com_sentid.get(),
            'estilo_torre': self.com_torres.get(),
            'offset': self.com_offset.get()
        }

        self.dic_padr = {
            'posx': self.entry_posx.get(),
            'posz': self.entry_posz.get(),
            'rpm': self.entry_rpmn.get(),
            'ava': self.entry_avan.get()
        }

        if '' in self.dic_user.values() or '' in self.dic_file.values() or '' in self.dic_mach.values() or '' in self.dic_padr:
            messagebox.showerror('Compilador G-Code', 'Um ou mais campos estão vazios, preencha todos os campos para prosseguir com a operação.')
        else:
            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_usuario.json', 'w', encoding='utf-8') as arquivo:
                json.dump(self.dic_user, arquivo, indent=4, ensure_ascii=False)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_programa.json', 'w', encoding='utf-8') as arquivo:
                json.dump(self.dic_file, arquivo, indent=4, ensure_ascii=False)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_maquina.json', 'w', encoding='utf-8') as arquivo:
                json.dump(self.dic_mach, arquivo, indent=4, ensure_ascii=False)

            with open('C:/Users/USUARIO/Documents/Compilador G-Code/src/configs/configs_padrao.json', 'w', encoding='utf-8') as arquivo:
                json.dump(self.dic_padr, arquivo, indent=4, ensure_ascii=False)

            messagebox.showinfo('Compilador G-Code', 'Os dados foram compilados e armazenados com sucesso no sistema')
            
            self.destroy()
            self.main_screen = MainScreen()
            self.main_screen.mainloop()

if __name__ == "__main__":
    app = SetupManager()
    app.mainloop()