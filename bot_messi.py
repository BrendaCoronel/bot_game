from bot_abstract import BotAbstract

class BotMessi(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "Messi"
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        if jugada_numero == 0:
            return 'M'  # Primera jugada siempre Murciélago
        else:
            if jugada_previa_oponente == 'M':
                return 'M'  # Si el oponente jugó Murciélago, respondemos con Murciélago
            else:
                return 'M'  # Si el oponente jugó Sapo, también jugamos Murciélago
