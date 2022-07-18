from Item import *
from Cadeiras import *
from Estoque import *

class Sessoes(Item):
    def __init__(self, name: str, id: int, price:float, dateTime:str, type:str, imagePath:str, store=1):
        super().__init__(name, id, price, store,imagePath)
        if type != 'Legendado' and type != 'Dublado':
            raise ValueError("Type can't be different of Legendado or Dublado")
        self.type = type
        self.dateTime = dateTime
        self.__cadeiras = Cadeiras()

        productList = Estoque.products
        sg.theme(Util.theme())
        
        self.layoutSessoes = [
            [sg.Text("Sessoes disponíveis", font=('Arial', 15, 'bold'))],
            
            [sg.Text("\n", font = Util.getFont)],
        ]

        for product in productList:
            if isinstance(product, Item):
                self.layoutSessoes.append([sg.Text(product.getName(), font = Util.getFont), sg.Input(key=product.getId(), size=(10, 1))])

        self.layoutSessoes.append([sg.Text("\n", font = Util.getFont)])
        self.layoutSessoes.append([sg.Text("SubTotal", size=(15,1), key = 'sub', font=Util.getFont), sg.Text(size=(15,1), key='_OUT_')])
        self.layoutSessoes.append([sg.Button("PRÓXIMO", key='PRÓXIMO', font=Util.getFont)])        

    def telaSessoes(self):  
        self.tela = sg.Window('Produtos', self.layoutSessoes, size=Util.screenSize(), element_justification='center') 

        subT = 0
        while True:      
            event, values = self.tela.read()
            
            if event == sg.WINDOW_CLOSED:
                self.semEstoque()
                return None
            if event == 'PRÓXIMO':
                #fechar janela     
                self.tela.close()
                return True
           
    def getCadeiras(self):
        return self.__cadeiras 

    
