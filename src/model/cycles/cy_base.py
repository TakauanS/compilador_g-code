from tkinter import messagebox

class CyBase:

    # Método responsável pela a integração da ferramenta do ciclo
    def ferramenta(self, tool: str):
        try:
            if not isinstance(tool, str):
                raise ValueError ('O valor do parâmetro da ferramenta deve ser do tipo `str`. Por favor, insira um valor válido.')
            
            self.__ferramenta = tool
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na inserção de ferramenta:\n\n{e}')
            print(f'Erro: {e}')

    # Método responsável pela a integração da referência de trabalho
    def referencia_trabalho(self, referencia: str):
        try:
            self.__lista_referencias = ['G54', 'G55', 'G56', 'G57', 'G58', 'G59']

            if not isinstance(referencia, str):
                raise ValueError ('O valor do parâmetro de referência de trabalho deve ser do tipo `str`. Por favor, insira um valor válido.')
            
            if referencia not in self.__lista_referencias:
                messagebox.showerror('Compilador G-Code', 'Valor de referência inválido. Use apenas: G54, G55, G56, G57, G58 ou G59.')
                return

            self.__referencia = referencia
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na integração da referência de trabalho:\n\n{e}')
            print(f'Erro: {e}')

    # Método responsável pela a integração da rotação de trabalho
    def rotacao(self, rpm: float):
        try:
            if not isinstance(rpm, float):
                raise ValueError ('O valor do parâmetro de rotação de trabalho deve ser do tipo `float`. Por favor, insira um valor válido.')
            
            if rpm <= 0:
                messagebox.showerror('Compilador G-Code', 'O valor da rotação deve ser maior que zero para garantir um funcionamento adequado.')
                return

            self.__rotacao = rpm

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na integração da rotação de trabalho:\n\n{e}')

    # Método responsável pela a integração do avanço de trabalho
    def avanco(self, advance: float):
        try:
            if not isinstance(advance, float):
                raise ValueError ('O valor do parâmetro de avanço deve ser do tipo `float`. Por favor, insira um valor válido.')
            
            if advance <= 0:
                messagebox.showerror('Compilador G-Code', 'O valor do avanço deve ser maior que zero para garantir um funcionamento adequado.')
                return
            
            self.__avanco = advance

        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na integração do avanço de trabalho:\n\n{e}')
            print(f'Erro: {e}')

    # Método responsável pela a integração do valor do passe de desbaste do ciclo    
    def passe(self, pf: float):
        try:
            if not isinstance(pf, float):
                raise ValueError ('O valor do parâmetro de passe deve ser do tipo `float`. Por favor, insira um valor válido.')
            
            if pf <= 0:
                messagebox.showerror('Compilador G-Code', 'O valor do passe deve ser maior que zero para garantir um funcionamento adequado.')
                return
            
            self.__passe = pf
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na inserção do passe de desbaste:\n\n{e}')
            print(f'Erro: {e}')

    # Método reponsável pela a integração da posição de segurança no eixo X
    def pos_segurancaX(self, posx: float):
        try:
            if not isinstance(posx, float):
                raise ValueError ('O valor de segurança no eixo X deve ser do tipo `float`.')

            self.__segurancax = posx
            
        except Exception as e:
            messagebox.showerror('Compilador G-Code', f'Erro na integração da posição de segurança no eixo X:\n\n{e}')
            print(f'Erro: {e}')

    # Método reponsável pela a integração da posição de segurança no eixo Z
    def pos_segurancaZ(self, posz: float):
        try:
            if not isinstance(posz, float):
                raise ValueError('O valor de segurança no eixo Z deve ser do tipo `float`.')
            
            self.__segurancaz = posz
        
        except Exception as e:
            messagebox.showerror('Compilador G-Code' , f'Erro na integração da posição de segurança no eixo Z:\n\n{e}')
            print(f'Erro: {e}')

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