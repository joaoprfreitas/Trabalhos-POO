import PySimpleGUI as sg
from Util import *

class Carrinho():
    'Classe do tipo carrinho'

    def __init__(self, productList):
        'Construtor do carrinho'

        self.productList = productList
        self.totalValue = 0


    def cartLayout(self):
        'Cria o layout do carrinho'
        self.layout = []

        # Cabeçalho
        self.layout.append([sg.Text('Carrinho', font=Util.getTitleFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor())])

        # Cabeçalho da tabela
        self.layout.append([sg.Text('Produto', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor()),
                            sg.Text('Valor', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor()),
                            sg.Text('Quantidade', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor()),
                            sg.Text('Subtotal', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor())
                            ])

        
        # Lista de produtos
        whiteBackground = True
        for product in self.productList:
            backgroundColor = '#ffffff'
            if not whiteBackground: backgroundColor = Util.fontBackgroundColor()

            whiteBackground = not whiteBackground

            subTotal = product[1] * product[2]
            self.layout.append([sg.Text(product[0], font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
                                sg.Text(str(product[1]), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
                                sg.Text(str(product[2]), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
                                sg.Text(str(subTotal), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor())
                                ])

            self.totalValue += subTotal

        # Total
        self.layout.append([sg.Text('Total:', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor()),
                            sg.Text(str(self.totalValue), font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor())
                            ])

        # Botões
        self.layout.append([sg.Button('Voltar', size=(10, 1), font=Util.getFont()),
                            sg.Button('Confirmar', size=(10, 1), font=Util.getFont())
                            ])

        sg.theme(Util.theme())
        self.screen = sg.Window('Carrinho', self.layout, size=Util.screenSize(), element_justification='center')



    def getTotalValue(self):
        'Retorna o valor total do carrinho'
        return self.totalValue

    def createScreen(self):
        'Inicia a tela de carrinho, retornando True se o usuário confirmar, '
        'False se o usuário cancelar o pagamento e None se o usuário encerrar o programa'

        while True:
            self.button, self.values = self.screen.read()
            if self.button == sg.WIN_CLOSED:
                return None
            elif self.button == 'Confirmar':
                return True
            elif self.button == 'Voltar':
                return False

if __name__ == '__main__':
    lista = [["Produto 1", 10.00, 2],
             ["Produto 2", 20.00, 1],
             ["Produto 3", 30.00, 3],
             ["Produto 4", 40.00, 4],
             ["Produto 5", 50.00, 5],
             ["Produto 6", 60.00, 6],
             ["Produto 7", 70.00, 7]]
    carrinho = Carrinho(lista)
    carrinho.cartLayout()
    retorno = carrinho.createScreen()

    print(retorno)