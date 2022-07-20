from multiprocessing.sharedctypes import Value
import PySimpleGUI as sg
from Util import *
from Item import *
from Estoque import *
from Carrinho import *
 
class Produtos():  


    def defProductsLayout(self, estoque):
    
        productList = estoque.getProducstList()
        self.layoutProdutos = [
            [sg.Text("Produtos disponíveis", font=('Arial', 15, 'bold'))],
            
            [sg.Text("\n", font = Util.getFont)],
        ]
        for product in productList:
            if not isinstance(product, Sessoes):
                self.productAdd = product
                self.layoutProdutos.append([sg.Text(product.getName(), font = Util.getFont), sg.Button("+", key="+ "+ str(product.getId()), size=(2, 1)), sg.Button("-", key="- "+ str(product.getId()), size=(2, 1))])

        self.layoutProdutos.append([sg.Text("\n", font = Util.getFont)])
        self.layoutProdutos.append([sg.Button("PRÓXIMO", key='PRÓXIMO', font=Util.getFont)])        
        self.layoutProdutos.append([sg.Button("VOLTAR", key = 'back', font=Util.getFont)])
    
    def telaProdutos(self, estoque):
        self.tela = sg.Window('Produtos', self.layoutProdutos, size=Util.screenSize(), element_justification='center') 

        subT = 0
        listProducts = []
        while True:
            event, values = self.tela.read()
            print(event, values)
            if event == sg.WINDOW_CLOSED:
                return None
            elif event == 'PRÓXIMO':
                self.tela.close()
                return listProducts
            elif event == 'VOLTAR':
                self.tela.close()
                return False
            else:
                event, id = event.split(" ")
                index = 0
                item = None
                for pro in listProducts:
                    if pro.getId() == int(id):
                        item = pro
                        break
                    index+=1
                if(item == None):
                    if(event == '+'):
                        x = list(estoque.searchProduct(int(id)))[0]
                        listProducts.append(Item(x.getName(), x.getId(), x.getPrice(), 1, x.getImagePath()))
                    else:
                        continue
                else:
                    qtt = 0
                    if(event == "+"):
                        qtt = 1
                    else:
                        qtt = -1     
                    listProducts[index].upAmount(qtt)
if __name__ == '__main__':
    ini = Produtos()
    ini.telaProdutos()

    