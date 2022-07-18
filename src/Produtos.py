import PySimpleGUI as sg
from Util import *
from Item import *
from Estoque import *
from Carrinho import *
 
class Produtos():  
    def __init__(self):
        #productList = Estoque.products
        sg.theme(Util.theme())
        productList = Estoque.products
        self.layoutProdutos = [
            [sg.Text("Produtos disponíveis", font=('Arial', 15, 'bold'))],
            
            [sg.Text("\n", font = Util.getFont)],
        ]
        for product in productList:
            if isinstance(product, Item):
                self.productAdd = product
                self.layoutProdutos.append([sg.Text(product.getName(), font = Util.getFont), sg.Input(key=product.getId(), size=(10, 1))])
                self.layoutProdutos.append([sg.Button("Adicionar", key = 'add', font=Util.getFont)])

        self.layoutProdutos.append([sg.Text("\n", font = Util.getFont)])
        self.layoutProdutos.append([sg.Button("PRÓXIMO", key='PRÓXIMO', font=Util.getFont)])        

   

    def telaProdutos(self):  
        self.tela = sg.Window('Produtos', self.layoutProdutos, size=Util.screenSize(), element_justification='center') 

        subT = 0
        while True:      
            event, values = self.tela.read()
            
            if event == sg.WINDOW_CLOSED:
                return None
            if event == "Adicionar":
                Carrinho.addProduct(self.productAdd)
            if event == 'PRÓXIMO':
                #fechar janela     
                self.tela.close()
                return True
            
if __name__ == '__main__':
    ini = Produtos()
    ini.telaProdutos()

    