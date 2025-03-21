from src.model.cycles.cycles_parametrizados.cycle_canal import Canal_Parametrizado

class Gcode_CanaisP:

    def __init__(self, diametro_i, prof, esp, rpm, n_canais, avanco, passe, ref, tool, pos_canais, posx, posz):
        
        self.diametro_inicial = diametro_i
        self.pos_canais = pos_canais
        self.profundidade = prof
        self.n_canais = n_canais
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
            ciclo_canal = Canal_Parametrizado(self.diametro_inicial, self.profundidade, self.n_canais, self.espessura, self.pos_canais)

            ciclo_canal.referencia_trabalho(self.referencia)
            ciclo_canal.ferramenta(self.ferramenta)
            ciclo_canal.rotacao(self.rotacao)
            ciclo_canal.avanco(self.avanco)
            ciclo_canal.passe(self.passe)

            ciclo_canal.pos_segurancaX(self.posx)
            ciclo_canal.pos_segurancaZ(self.posz)
        
        except Exception as e:
            print(f'Erro! {e}')

        else:
            ciclo_canal.gcode()