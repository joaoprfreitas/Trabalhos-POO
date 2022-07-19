#Adicionar em carrinho
class Ingresso():

    def __init__(self, numberChair, sessao:int):
        self.numberChair  = numberChair
        self.sessao = sessao # Id da sessão desse ingresso

    def getNumberChair(self):
        return self.numberChair

    def getSessao(self):
        return self.sessao

    