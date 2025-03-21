from src.model.cycles.cycles_parametrizados.cycle_desbaste import Desbaste_Parametrizado

class Gcode_DesbasteP:

    def __init__(self, diametro_i, diametro_f, esp, rpm, avanco, passe, ref, tool, posx, posz):

        self.diametro_inicial = diametro_i
        self.diametro_final = diametro_f
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
            ciclo_desbaste = Desbaste_Parametrizado(self.diametro_inicial, self.diametro_final, self.espessura)

            ciclo_desbaste.referencia_trabalho(self.referencia)
            ciclo_desbaste.ferramenta(self.ferramenta)
            ciclo_desbaste.rotacao(self.rotacao)
            ciclo_desbaste.avanco(self.avanco)
            ciclo_desbaste.passe(self.passe)

            ciclo_desbaste.pos_segurancaX(self.posx)
            ciclo_desbaste.pos_segurancaZ(self.posz)
        
        except Exception as e:
            print(f'Erro! {e}')

        else:
            ciclo_desbaste.gcode()