import customtkinter as ctk
from src.model.assents import Assents

class MainCycles(ctk.CTk):

    cor1 = '#F2F1F0' # Cor branca de FG-COLOR
    cor2 = '#FCF6F2' # Cor branca de BG-COLOR

    def __init__(self):
        super().__init__()

        self.__assents = Assents(self)

        self.geometry('610x300')
        self.title('Compilador G-Code | Cycles')
        self.resizable(False, False)
        self.config(bg=MainCycles.cor1)
        self.iconbitmap('C:/Users/USUARIO/Documents/Compilador G-code/assets/imgs/favicon.ico')

        # SEÇÃO DE TABVIEWs

        self.tabview = ctk.CTkTabview(self, 
                                      width=590, 
                                      height=295,
                                      border_width=1, 
                                      corner_radius=12,           
                                      bg_color=MainCycles.cor1,
                                      fg_color=MainCycles.cor1,
                                      segmented_button_selected_color=self.__assents.cor4)
        self.tabview.place(x=10, y=-5)

        self.aba_cycles = self.tabview.add('CYCLES')

        # SEÇÃO DE LABELFRAMEs

        self.fra_desb = self.__assents.criar_labelframe(0, 0, 270, 110, 'Cycles Desbaste', MainCycles.cor1, self.aba_cycles)
        self.fra_cana = self.__assents.criar_labelframe(295, 0, 270, 110, 'Cycles Canal', MainCycles.cor1, self.aba_cycles)

        self.fra_face = self.__assents.criar_labelframe(0, 120, 270, 110, 'Cycles Faceamento', MainCycles.cor1, self.aba_cycles)
        self.fra_fura = self.__assents.criar_labelframe(295, 120, 270, 110, 'Cycles Furação', MainCycles.cor1, self.aba_cycles)

        # SEÇÃO DE BUTTONs

        self.but_desp = ctk.CTkButton(self.fra_desb,
                                     height=28, 
                                     width=55,  
                                     corner_radius=8,                           
                                     compound='right',  
                                     bg_color=MainCycles.cor2, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up, 
                                     fg_color=self.__assents.cor4,
                                     text='Desbaste - Parametrizado     ',    
                                     hover_color=self.__assents.cor5).place(x=30, y=70)
        
        self.but_desf = ctk.CTkButton(self.fra_desb,
                                     height=28, 
                                     width=55,  
                                     corner_radius=8,                           
                                     compound='right',  
                                     bg_color=MainCycles.cor2, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up, 
                                     fg_color=self.__assents.cor4,
                                     text='Desbaste - Funcional             ',    
                                     hover_color=self.__assents.cor5).place(x=30, y=110)
        
        self.but_facp = ctk.CTkButton(self.fra_face,
                                     height=28, 
                                     width=55,  
                                     corner_radius=8,                           
                                     compound='right',  
                                     bg_color=MainCycles.cor2, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up, 
                                     fg_color=self.__assents.cor4,
                                     text='Faceamento - Parametrizado',    
                                     hover_color=self.__assents.cor5).place(x=30, y=190)
        
        self.but_facf = ctk.CTkButton(self.fra_face,
                                     height=28, 
                                     width=55,  
                                     corner_radius=8,                           
                                     compound='right',  
                                     bg_color=MainCycles.cor2, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up, 
                                     fg_color=self.__assents.cor4,
                                     text='Faceamento - Funcional        ',    
                                     hover_color=self.__assents.cor5).place(x=30, y=230)
        
        self.but_furp = ctk.CTkButton(self.fra_fura,
                                     height=28, 
                                     width=55,  
                                     corner_radius=8,                           
                                     compound='right',  
                                     bg_color=MainCycles.cor2, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up, 
                                     fg_color=self.__assents.cor4,
                                     text='Furação - Parametrizado       ',    
                                     hover_color=self.__assents.cor5).place(x=325, y=190)
        
        self.but_furf = ctk.CTkButton(self.fra_fura,
                                     height=28, 
                                     width=55,  
                                     corner_radius=8,                           
                                     compound='right',  
                                     bg_color=MainCycles.cor2, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up, 
                                     fg_color=self.__assents.cor4,
                                     text='Furação - Funcional               ',    
                                     hover_color=self.__assents.cor5).place(x=325, y=230)
        
        self.but_canp = ctk.CTkButton(self.fra_cana,
                                     height=28, 
                                     width=55,  
                                     corner_radius=8,                           
                                     compound='right',  
                                     bg_color=MainCycles.cor2, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up, 
                                     fg_color=self.__assents.cor4,
                                     text='Canal - Parametrizado            ',    
                                     hover_color=self.__assents.cor5).place(x=325, y=70)
        
        self.but_canf = ctk.CTkButton(self.fra_cana,
                                     height=28, 
                                     width=55,  
                                     corner_radius=8,                           
                                     compound='right',  
                                     bg_color=MainCycles.cor2, 
                                     font=('Arial', 15, 'bold'),
                                     image=self.__assents.img_up, 
                                     fg_color=self.__assents.cor4,
                                     text='Canal - Funcional                    ',    
                                     hover_color=self.__assents.cor5).place(x=325, y=110)