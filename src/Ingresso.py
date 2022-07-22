from Item import *

class Ingresso(Item):

    def __init__(self, name:str, numberChair, sessaoId:int, price):
        'Construtor do ingresso'

        super().__init__("Ingresso para " + name + " Cadeira " + numberChair,  int(str(numberChair + str(sessaoId))), price, 1, 'noImage')
        self.numberChair  = numberChair
        self.sessaoId = sessaoId # Id da sessão desse ingresso

    def getNumberChair(self):
        'Retorna o número da cadeira'
        return self.numberChair

    def getSessao(self):
        'Retorna o id da sessão'
        return self.sessaoId

    def __str__(self):
        return super().__str__()
    