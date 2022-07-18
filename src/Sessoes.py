from Item import *
from Cadeiras import *

class Sessoes(Item):
    def __init__(self, name: str, id: int, price:float, dateTime:str, type:str, imagePath:str, store=1):
        super().__init__(name, id, price, store,imagePath)
        if type != 'Legendado' and type != 'Dublado':
            raise ValueError("Type can't be different of Legendado or Dublado")
        self.type = type
        self.dateTime = dateTime
        self.__cadeiras = Cadeiras()

    def getCadeiras(self):
        return self.__cadeiras
