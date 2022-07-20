#Adicionar em carrinho
from Item import *
class Ingresso(Item):

    def __init__(self, name:str, numberChair, sessaoId:int, price):
        super().__init__("Ingresso para " + name + " Cadeira " + numberChair,  int(str(numberChair + str(sessaoId))), price, 1, 'noImage')
        self.numberChair  = numberChair
        self.sessao = sessaoId # Id da sessão desse ingresso

    def getNumberChair(self):
        return self.numberChair

    def getSessao(self):
        return self.sessaoId

    
    