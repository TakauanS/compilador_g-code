from src.model.cycles.cycles_funcionais.cycle_canaisf import Canais_Funcional

class Gcode_CanaisF:

    def __init__(self, diametro_i, diametro_f, aprox, rpm, position, avanco, passe, dist, ref, tool, posx, posz):

        self.diametro_inicial = diametro_i
        self.diametro_final = diametro_f
        self.aproximaxcao = aprox
        self.position = position
        self.ferramenta = tool
        self.referencia = ref
        self.avanco = avanco
        self.passe = passe
        self.rotacao = rpm
        self.dist = dist
        self.posx = posx
        self.posz = posz

    def gerar_gcode(self):

        try:
            ciclo_canais = Canais_Funcional(self.diametro_inicial, self.diametro_final, self.dist, self.position, self.aproximaxcao)

            ciclo_canais.referencia_trabalho(self.referencia)
            ciclo_canais.ferramenta(self.ferramenta)
            ciclo_canais.rotacao(self.rotacao)
            ciclo_canais.avanco(self.avanco)
            ciclo_canais.passe(self.passe)

            ciclo_canais.pos_segurancaX(self.posx)
            ciclo_canais.pos_segurancaZ(self.posz)

        except Exception as e:
            print(f'Erro! {e}')

        else:
            ciclo_canais.gcode()