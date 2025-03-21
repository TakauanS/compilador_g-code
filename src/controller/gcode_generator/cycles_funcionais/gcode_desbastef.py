from src.model.cycles.cycles_funcionais.cycle_desbastef import Desbaste_Funcional

class Gcode_DesbasteF:

    def __init__(self, diametro_i, diametro_f, esps, rpm, avanco, passe, ref, tool, posx, posz):

        self.diametro_inicial = diametro_i
        self.diametro_finais = diametro_f
        self.ferramenta = tool
        self.espessuras = esps
        self.referencia = ref
        self.avanco = avanco
        self.rotacao = rpm
        self.passe = passe
        self.posx = posx
        self.posz = posz

    def gerar_gcode(self):

        try:
            ciclo_desbaste = Desbaste_Funcional(self.diametro_inicial)

            ciclo_desbaste.referencia_trabalho(self.referencia)
            ciclo_desbaste.ferramenta(self.ferramenta)
            ciclo_desbaste.rotacao(self.rotacao)
            ciclo_desbaste.avanco(self.avanco)
            ciclo_desbaste.passe(self.passe)

            ciclo_desbaste.gerar_coordenadas(self.diametro_finais, self.espessuras)

        except Exception as e:
            print(f'Erro! {e}')
        
        else:
            ciclo_desbaste.gcode()