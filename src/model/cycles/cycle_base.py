from tkinter import messagebox

class CycleBase:

    def ferramenta(self, tool: str):

        if not isinstance(tool, str):
            raise ValueError ('O valor do parâmetro da ferramenta deve ser do tipo `str`. Por favor, insira um valor válido.')
        else:
            self._ferramenta = tool
            return self._ferramenta

    def referencia_trabalho(self, referencia: str):

        self.lista_referencias = ['G54', 'G55', 'G56', 'G57', 'G58', 'G59']

        if not isinstance(referencia, str):
            raise ValueError ('O valor do parâmetro de referência de trabalho deve ser do tipo `str`. Por favor, insira um valor válido.')
        
        if referencia not in self.lista_referencias:
            messagebox.showerror(title='Compilador G-Code', message='Valor de referência inválido. Use apenas: G54, G55, G56, G57, G58 ou G59.')
            return
        else:
            self._referencia = referencia
            return self._referencia

    def rotacao(self, rpm: float):

        if not isinstance(rpm, float):
            raise ValueError ('O valor do parâmetro de rotação de trabalho deve ser do tipo `float`. Por favor, insira um valor válido.')
        
        if rpm <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor da rotação deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self._rotacao = rpm
            return self._rotacao

    def avanco(self, advance: float):

        if not isinstance(advance, float):
            raise ValueError ('O valor do parâmetro de avanço deve ser do tipo `float`. Por favor, insira um valor válido.')
        
        if advance <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do avanço deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self._avanco = advance
            return self._avanco
        
    def passe(self, pf: float):

        if not isinstance(pf, float):
            raise ValueError ('O valor do parâmetro de passe deve ser do tipo `float`. Por favor, insira um valor válido.')
        
        if pf <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do passe deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self._passe = pf
            return self._passe

    def pos_segurancaX(self, posx: float):

        if not isinstance(posx, float):
            raise ValueError ('O valor de segurança no eixo X deve ser do tipo `float`.')
        
        if posx <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor de segurança no eixo X deve ser maior que zero.')
            return
        else:
            self._segurancax = posx
            return self._segurancax
        
    def pos_segurancaZ(self, posz: float):

        if not isinstance(posz, float):
            raise ValueError ('O valor de segurança no eixo Z deve ser do tipo `float`.')
        
        if posz <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor de segurança no eixo Z deve ser maior que zero.')
            return
        else:
            self._segurancaz = posz
            return self._segurancaz

    @property
    def get_posx(self):
        return self._segurancax
    
    @property
    def get_posz(self):
        return self._segurancaz

    @property
    def get_ferramenta(self):
        return self._ferramenta
    
    @property
    def get_referencia(self):
        return self._referencia
    
    @property
    def get_rotacao(self):
        return self._rotacao

    @property
    def get_avanco(self):
        return self._avanco
    
    @property
    def get_passe(self):
        return self._passe
    
    @get_ferramenta.setter
    def set_ferramenta(self, nova_ferramenta: str):

        if not isinstance(nova_ferramenta, str):
            raise ValueError ('O valor do parâmetro da ferramenta deve ser do tipo `str`. Por favor, insira um valor válido.')
        else:
            self._ferramenta = nova_ferramenta
            return self._ferramenta

    @get_referencia.setter
    def set_referencia(self, nova_referencia: str):

        if not isinstance(nova_referencia, str):
            raise ValueError ('O valor do parâmetro da referência deve ser do tipo `str`. Por favor, insira um valor válido.')

        if nova_referencia not in self.lista_referencias:
            messagebox.showerror(title='Compilador G-Code', message='Valor da nova referência é inválido. Use apenas: G54, G55, G56, G57, G58 ou G59.')
            return
        else:
            self._referencia = nova_referencia
            return self._referencia

    @get_rotacao.setter
    def set_rotacao(self, nova_rotacao: float):

        if not isinstance(nova_rotacao, float):
            raise ValueError ('O valor do parâmetro de rotação deve ser do tipo `float`. Por favor, insira um valor válido.')
        
        if nova_rotacao <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor da rotação deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self._rotacao = nova_rotacao
            return self._rotacao

    @get_avanco.setter
    def set_avanco(self, novo_avanco: float):

        if not isinstance(novo_avanco, float):
            raise ValueError ('O valor do parâmetro de avanço deve ser do tipo `float`. Por favor, insira um valor válido.')
        
        if novo_avanco <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do avanço deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self._avanco = novo_avanco
            return self._avanco

    @get_passe.setter
    def set_passe(self, novo_passe: float):

        if not isinstance(novo_passe, float):
            raise ValueError ('O valor do parâmetro de passe deve ser do tipo `float`. Por favor, insira um valor válido.')

        if novo_passe <= 0:
            messagebox.showerror(title='Compilador G-Code', message='O valor do passe deve ser maior que zero para garantir um funcionamento adequado.')
            return
        else:
            self._passe = novo_passe
            return self._passe