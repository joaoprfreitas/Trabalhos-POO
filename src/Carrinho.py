from math import prod
import PySimpleGUI as sg
from Util import *
from Item import *
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab_qrcode import QRCodeImage

from Sessoes import *
from Ingresso import *
from Estoque import *

class Carrinho():
    'Classe do tipo carrinho'

    def __init__(self):
        'Construtor do carrinho'

        self.productList = []
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
            if isinstance(product, Item):
                backgroundColor = '#ffffff'
                if not whiteBackground: backgroundColor = Util.fontBackgroundColor()

                whiteBackground = not whiteBackground

                subTotal = product.getPrice() * product.getAmount()
                self.layout.append([sg.Text(product.getName(), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
                                    sg.Text(str(product.getPrice()), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
                                    sg.Text(str(product.getAmount()), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
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

    def qrCodeLayout(self): #Não testado
        'Cria o layout do qr code'
        self.report = canvas.Canvas("Ticket.pdf")

        self.layout = []

        # Cabeçalho
        self.layout.append([sg.Text('Ticket', font=Util.getTitleFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor())])

        # Cabeçalho da tabela
        self.layout.append([sg.Text('Produto', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor()),
                            sg.Text('Valor', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor()),
                            sg.Text('Quantidade', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor()),
                            sg.Text('Subtotal', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor())
                            ])

        
        # Lista de produtos
        whiteBackground = True
        for product in self.productList:
            if isinstance(product, Item):
                backgroundColor = '#ffffff'
                if not whiteBackground: backgroundColor = Util.fontBackgroundColor()

                whiteBackground = not whiteBackground
                self.report.drawString(50, 800, str(product) + "\n")

                subTotal = product.getPrice() * product.getAmount()
                self.layout.append([sg.Text(product.getName(), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
                                    sg.Text(str(product.getPrice()), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
                                    sg.Text(str(product.getAmount()), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor()),
                                    sg.Text(str(subTotal), font=Util.getFont(), justification='center', background_color=backgroundColor, text_color=Util.fontColor())
                                    ])

                self.totalValue += subTotal

        qr = QRCodeImage('Aleatório', size=30 * mm)
        qr.drawOn(self.report, 0, 0)
        self.report.showPage()
        # Total
        self.layout.append([sg.Text('Total:', font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor()),
                            sg.Text(str(self.totalValue), font=Util.getFont(), justification='center', background_color=Util.fontBackgroundColor(), text_color=Util.fontColor())
                            ])

        # Botões
        self.layout.append([sg.Button('Voltar', size=(10, 1), font=Util.getFont()),
                            sg.Button('Baixar pdf', size=(10, 1), font=Util.getFont())
                            ])

        sg.theme(Util.theme())
        self.screen = sg.Window('Carrinho', self.layout, size=Util.screenSize(), element_justification='center')

    def determineTicket(ticket, idSession):

        if isinstance(ticket, Ingresso) and ticket.getSessao() == idSession:
            return True
    def removeAllTickets(self, idSession:int):
        self.productList = [x for x in self.productList if print(x) and not self.determineTicket(x, idSession)]

    def addProduct(self, product : Item):
        'Adiciona um produto ao carrinho'

        if not isinstance(product, Item):
            raise TypeError('O produto deve ser do tipo Item')

        self.productList.append(product)

    def getProductList(self):
        'Retorna a lista de produtos do carrinho'
        return self.productList

    def getTotalValue(self):
        'Retorna o valor total do carrinho'
        return self.totalValue

    def finishPayment(self, estoque):
        for product in self.productList:
            estoque.sell(product)
        self.productList = []

    def createScreen(self):
        'Inicia a tela de carrinho, retornando True se o usuário confirmar, '
        'False se o usuário cancelar o pagamento e None se o usuário encerrar o programa'

        while True:
            self.button, self.values = self.screen.read()
            if self.button == sg.WIN_CLOSED:
                return None
            elif self.button == 'Confirmar':
                self.screen.close()
                return True
            elif self.button == 'Voltar':
                self.screen.close()
                return False
    def createScreenQrCode(self):
        'Inicia a tela de carrinho, retornando True se o usuário confirmar, '
        'False se o usuário cancelar o pagamento e None se o usuário encerrar o programa'

        while True:
            self.button, self.values = self.screen.read()
            if self.button == sg.WIN_CLOSED:
                return None
            elif self.button == 'Baixar pdf':
                self.screen.close()
                self.report.save()
                return True
            elif self.button == 'Voltar':
                self.screen.close()
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