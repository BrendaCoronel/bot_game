from bot_abstract import BotAbstract

class BotMessi(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Ganador"
    
    def __init__(self):
        self.ultima_jugada_oponente = None
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        if jugada_numero == 0:
            # Primera jugada siempre es Murciélago
            return 'M'
        
        # Estrategia basada en la jugada previa del oponente
        if jugada_previa_oponente == 'M':
            return 'S'  # Responder a Murciélago con Sapo
        elif jugada_previa_oponente == 'S':
            return 'M'  # Responder a Sapo con Murciélago
