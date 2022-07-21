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
        self.layout.append([sg.Text('Carrinho', font=Util.getTitleFont(), justification='center')])

        # Cabeçalho da tabela
        self.layout.append([sg.Text('Produto', font=Util.getFont(), justification='center'),
                            sg.Text('Valor', font=Util.getFont(), justification='center'),
                            sg.Text('Quantidade', font=Util.getFont(), justification='center'),
                            sg.Text('Subtotal', font=Util.getFont(), justification='center')
                            ])

        self.totalValue = 0
        
        # Lista de produtos
        for product in self.productList:
            if isinstance(product, Item):
                subTotal = product.getPrice() * product.getAmount()
                self.layout.append([sg.Text(product.getName(), font=Util.getFont(), justification='center'),
                                    sg.Text('{:.2f}'.format(product.getPrice()), font=Util.getFont(), justification='center'),
                                    sg.Text(product.getAmount(), font=Util.getFont(), justification='center'),
                                    sg.Text('{:.2f}'.format(subTotal), font=Util.getFont(), justification='center')
                                    ])

                self.totalValue += subTotal
                print('Iteracao: {}'.format(self.totalValue))

        # Total
        self.layout.append([sg.Text('Total:', font=Util.getFont(), justification='center'),
                            sg.Text('{:.2f}'.format(self.totalValue), font=Util.getFont(), justification='center')
                            ])

        # Botões
        self.layout.append([sg.Button('Voltar', size=(10, 1), font=Util.getFont(), button_color=Util.getButtonColor()),
                            sg.Button('Confirmar', size=(10, 1), font=Util.getFont(), button_color=Util.getButtonColor())
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

        self.totalValue = 0

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
        index  = 0
        for pro in self.productList:
            if isinstance(pro, Ingresso) and pro.getSessao() ==idSession:
                self.productList.pop(index)
                index -=1
            index +=1

    def addProduct(self, product : Item, remove = 0):
        'Adiciona um produto ao carrinho'

        if not isinstance(product, Item):
            raise TypeError('O produto deve ser do tipo Item')

        index = 0
        item = None
        for pro in self.productList:
                if pro.getId() == int(product.getId()):
                    item = pro
                    break
                index+=1
        if item is None:
            if not remove:
                self.productList.append(product)
        else:
            amount = product.getAmount()
            if remove:
                amount = -1
            self.productList[index].upAmount(amount)
            if self.productList[index].getAmount() == 0:
                self.productList.pop(index)

    def getProductList(self):
        'Retorna a lista de produtos do carrinho'
        return self.productList

    def getItem(self, id:int):
        'Retorna um item do carrinho'
        if  type(id) != int:
            raise Exception("Id must be integer")
        item = list(filter(lambda p: p.id == id, self.productList))
        if item == []:
            return None
        else:
            return item[0]

    def getTotalValue(self):
        'Retorna o valor total do carrinho'
        print('Valor: {}'.format(self.totalValue))
        return self.totalValue

    def finishPayment(self, estoque):
        self.totalValue = 0
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
