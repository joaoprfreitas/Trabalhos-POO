from Item import *
from Cadeiras import *
from Estoque import *
from Carrinho import *

class Sessoes(Item):
    
    def __init__(self, name: str, id: int, price:float, dateTime:str, type:str, imagePath:str, store=1):
        'Construtor da sessão'

        super().__init__(name, id, price, store,imagePath)
        if type != 'Legendado' and type != 'Dublado':
            raise ValueError("Type can't be different of Legendado or Dublado")
        self.type = type
        self.dateTime = dateTime
        self.__cadeiras = Cadeiras()

    def getCadeiras(self):
        return self.__cadeiras 

    def getHorario(self):
        return self.dateTime