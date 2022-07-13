import Item
class Sessoes(Item):
    def __init__(self, name: str, id: int, price:float, dateTime:str, type:str, store=0):
        super().__init__(name, id, price, store)
        if type != 'Legendado' or type != 'Dublado':
            raise ValueError("Type can't be different of Legendado or Dublado")
        self.type = type
        self.dateTime = dateTime
