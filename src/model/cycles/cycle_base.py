from tkinter import messagebox

class CycleBase:

    def ferramenta(self, tool: str):

        if not isinstance(tool, str):
            raise ValueError ('O valor do parâmetro da ferramenta deve ser do tipo `str`. Por favor, insira um valor válido.')
        else:
            self.__ferramenta = tool

    def referencia_trabalho(self, referencia: str):

        self.__lista_referencias = ['G54', 'G55', 'G56', 'G57', 'G58', 'G59']

        if not isinstance(referencia, str):
            raise ValueError ('O valor do parâmetro de referência de trabalho deve ser do tipo `str`. Por favor, insira um valor válido.')
        
        if referencia not in self.__lista_referencias:
            messagebox.showerror(title='Compilador G-Code', message='Valor de referência inválido. Use apenas: G54, G55, G56, G57, G58 ou G59.')
            return
        else:
            self.__referencia = referencia

    def rotacao(self, rpm: float):

        if not isinstance(rpm, float):
            raise ValueError ('O valor do parâmetro de rotação de trabalho deve ser do tipo `float`. Por favor, insira um valor válido.')
        
        if rpm <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor da rotação deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self.__rotacao = rpm

    def avanco(self, advance: float):

        if not isinstance(advance, float):
            raise ValueError ('O valor do parâmetro de avanço deve ser do tipo `float`. Por favor, insira um valor válido.')
        
        if advance <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do avanço deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self.__avanco = advance
        
    def passe(self, pf: float):

        if not isinstance(pf, float):
            raise ValueError ('O valor do parâmetro de passe deve ser do tipo `float`. Por favor, insira um valor válido.')
        
        if pf <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do passe deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self.__passe = pf

    def pos_segurancaX(self, posx: float):

        if not isinstance(posx, float):
            messagebox.showerror(title='Compilador G-Code', message='O valor de segurança no eixo X não foi informado. Por favor, insira um valor válido.')
            raise ValueError ('O valor de segurança no eixo X deve ser do tipo `float`.')

        self.__segurancax = posx
        
    def pos_segurancaZ(self, posz: float):

        if not isinstance(posz, float):
            messagebox.showerror(title='Compilador G-Code', message='O valor de segurança no eixo Z não foi informado. Por favor, insira um valor válido.')
            raise ValueError ('O valor de segurança no eixo Z deve ser do tipo `float`.')

        self.__segurancaz = posz

    @property
    def get_posx(self):
        return self.__segurancax
    
    @property
    def get_posz(self):
        return self.__segurancaz

    @property
    def get_ferramenta(self):
        return self.__ferramenta
    
    @property
    def get_referencia(self):
        return self.__referencia
    
    @property
    def get_rotacao(self):
        return self.__rotacao

    @property
    def get_avanco(self):
        return self.__avanco
    
    @property
    def get_passe(self):
        return self.__passe