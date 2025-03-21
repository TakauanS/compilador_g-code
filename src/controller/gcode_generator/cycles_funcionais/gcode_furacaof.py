from src.model.cycles.cycles_funcionais.cycle_furacaof import Furacao_Funcional

class Gcode_FuracaoF:

    def __init__(self, posicao_x, posicao_z, esp, rpm, avanco, passe, ref, tool, posx, posz):

        self.posicao_x = posicao_x
        self.posicao_z = posicao_z
        self.ferramenta = tool
        self.referencia = ref
        self.espessura = esp
        self.avanco = avanco
        self.rotacao = rpm
        self.passe = passe   
        self.posx = posx
        self.posz = posz
    
    def gerar_gcode(self):

        try:
            ciclo_furacao = Furacao_Funcional(self.posicao_x, self.posicao_z, self.espessura, self.passe)

            ciclo_furacao.referencia_trabalho(self.referencia)
            ciclo_furacao.ferramenta(self.ferramenta)
            ciclo_furacao.rotacao(self.rotacao)
            ciclo_furacao.avanco(self.avanco)
            ciclo_furacao.passe(self.passe)

            ciclo_furacao.pos_segurancaX(self.posx)
            ciclo_furacao.pos_segurancaZ(self.posz)

        except Exception as e:
            print(f'Erro! {e}')
        
        else:
            ciclo_furacao.gcode()