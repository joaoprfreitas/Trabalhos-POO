import PySimpleGUI as sg
from Util import *
from Item import *
from Estoque import *
 
class Produtos():  
    def __init__(self, productList):
        #productList = Estoque.products
        sg.theme(Util.theme())
        
        self.layoutProdutos = [
            [sg.Text("Produtos disponíveis", font=('Arial', 15, 'bold'))],
            
            [sg.Text("\n", font = Util.getFont)],
        ]

        for product in productList:
            if isinstance(product, Item):
                self.layoutProdutos.append([sg.Text(product.getName(), font = Util.getFont), sg.Input(key=product.getId(), size=(10, 1))])

        self.layoutProdutos.append([sg.Text("\n", font = Util.getFont)])
        self.layoutProdutos.append([sg.Text("SubTotal", size=(15,1), key = 'sub', font=Util.getFont), sg.Text(size=(15,1), key='_OUT_')])
        self.layoutProdutos.append([sg.Button("PRÓXIMO", key='PRÓXIMO', font=Util.getFont)])        

   

    def telaProdutos(self):  
        self.tela = sg.Window('Produtos', self.layoutProdutos, size=Util.screenSize(), element_justification='center') 

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
            
if __name__ == '__main__':
    ini = Produtos()
    ini.telaProdutos()

    