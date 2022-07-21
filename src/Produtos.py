import PySimpleGUI as sg
from Util import *
from Item import *
from Estoque import *
from Carrinho import *
 
class Produtos():  

    def defProductsLayout(self, estoque):
        productList = estoque.getProducstList()
        self.layoutProdutos = [
            [sg.Text("Produtos disponíveis", font=Util.getTitleFont())],
            [sg.Text("\n", font = Util.getFont)]
        ]

        layoutProducts = []
        for product in productList:
            if not isinstance(product, Sessoes):
                self.productAdd = product
                layoutProducts.append([sg.Text(product.getName(), font = Util.getFont),
                                       sg.Text("R$:{:.2f}".format(product.getPrice())),
                                       sg.Button("+", key="+ "+ str(product.getId()), size=(2, 1)),
                                       sg.Button("-", key="- "+ str(product.getId()), size=(2, 1))
                                      ])
        self.layoutProdutos.append([sg.Text("\n", font = Util.getFont)])
        self.layoutProdutos.append([sg.Frame("Lista de produtos",
                                             layoutProducts,
                                             element_justification = 'c',
                                            )
                                   ])

        self.layoutProdutos.append([sg.Text("\n\n", font = Util.getFont)])
        self.layoutProdutos.append([sg.Text("\n\n", font = Util.getFont)])
        self.layoutProdutos.append([sg.Button("VOLTAR", key = 'back', font=Util.bigButtonFont()),
                                    sg.Button("PRÓXIMO", key='next', font=Util.bigButtonFont())])
    
    def telaProdutos(self, estoque, carrinho: Carrinho):
        self.tela = sg.Window('Produtos', self.layoutProdutos, size=Util.screenSize(), element_justification='center') 

        listProducts = carrinho.getProductList()

        while True:
            event, values = self.tela.read()
            if event == sg.WIN_CLOSED:
                return None

            elif event == 'next':
                self.tela.close()
                return listProducts

            elif event == 'back':
                self.tela.close()
                return False
            else:
                event, id = event.split(" ")
                x = list(estoque.searchProduct(int(id)))[0]

                if(event == '+'):
                    item = carrinho.getItem(x.getId())
                    if item != None and item.getAmount() + 1 > x .getAmount():
                        sg.PopupError("Item não disponível em estoque")
                    else:
                        carrinho.addProduct(Item(x.getName(), x.getId(), x.getPrice(), 1, x.getImagePath()))
                else:
                        carrinho.addProduct(Item(x.getName(), x.getId(), x.getPrice(), 1, x.getImagePath()), 1)
if __name__ == '__main__':
    ini = Produtos()
    ini.telaProdutos()

    