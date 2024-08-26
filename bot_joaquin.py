from bot_abstract import BotAbstract

class BotJoaquin(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Joaquin"

    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        if jugada_numero == 0:
            # Primera jugada siempre "Murciélago"
            return 'M'
        elif jugada_previa_oponente == 'S':
            # Si el oponente jugó "Sapo", juego "Murciélago" para ganar 2 puntos
            return 'M'
        else:
            # Si el oponente jugó "Murciélago", juego "Sapo" para minimizar el riesgo
            return 'S'
