from src.model.cycles.cycles_parametrizados.cycle_faceamento import Faceamento_Parametrizado

class Gcode_FaceamentoP:

    def __init__(self, diametro_i, diametro_f, esp, rpm, avanco, passe, ref, tool, posx, posz):

        self.diametro_inicial = diametro_i
        self.diametro_final = diametro_f
        self.ferramenta = tool
        self.referencia = ref
        self.avanco = avanco
        self.espessura = esp
        self.rotacao = rpm
        self.passe = passe
        self.posx = posx
        self.posz = posz

    def gerar_gcode(self):

        try:
            ciclo_faceamento = Faceamento_Parametrizado(self.diametro_inicial, self.diametro_final, self.espessura)

            ciclo_faceamento.referencia_trabalho(self.referencia)
            ciclo_faceamento.ferramenta(self.ferramenta)
            ciclo_faceamento.rotacao(self.rotacao)
            ciclo_faceamento.avanco(self.avanco)
            ciclo_faceamento.passe(self.passe)
            
            ciclo_faceamento.pos_segurancaX(self.posx)
            ciclo_faceamento.pos_segurancaZ(self.posz)
        
        except Exception as e:
            print(f'Erro! {e}')

        else:
            ciclo_faceamento.gcode()