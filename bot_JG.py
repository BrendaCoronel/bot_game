from bot_abstract import BotAbstract

class BotBueno(BotAbstract):
    
    @property
    def Nombre(self) -> str:
        return "GRUPO 4"
    
    def Jugar(self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        if jugada_previa_oponente == 'S':
            return 'M'
        elif jugada_previa_oponente == 'M':
                return 'M'
        return 'S'