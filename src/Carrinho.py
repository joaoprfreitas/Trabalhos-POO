import PySimpleGUI as sg
from Util import *
from Item import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, Frame
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

        self.totalValue = 0

        # Cabeçalho
        self.layout.append([sg.Text('Carrinho', font=Util.getTitleFont(), justification='center')])
        self.layout.append([sg.Text('\n')])

        headings = ['Produto', 'Valor', 'Quantidade', 'Subtotal']

        list = []

        for product in self.productList:
            if isinstance(product, Item):
                subTotal = product.getPrice() * product.getAmount()
                list.append([product.getName(), '{:.2f}'.format(product.getPrice()), str(product.getAmount()), '{:.2f}'.format(subTotal)])
                self.totalValue += subTotal

        self.layout.append([sg.Table(values=list, 
                                     headings=headings, 
                                     max_col_width=35,
                                     auto_size_columns=True,
                                     display_row_numbers=False,
                                     justification='right',
                                     num_rows=10,
                                     key='-TABLE-',
                                     row_height=35)])

        # Total
        self.layout.append([sg.Text('\n'),
                            sg.Text('Total:', font=Util.getFont(), justification='center'),
                            sg.Text('{:.2f}'.format(self.totalValue), font=Util.getFont(), justification='center')
                            ])

        # Botões
        self.layout.append([sg.Text('\n'),
                            sg.Button('Voltar', size=(10, 1), font=Util.getFont(), button_color=Util.getButtonColor()),
                            sg.Button('Confirmar', size=(10, 1), font=Util.getFont(), button_color=Util.getButtonColor())
                            ])

        sg.theme(Util.theme())
        self.screen = sg.Window('Carrinho', self.layout, size=Util.screenSize(), element_justification='center')

    def qrCodeLayout(self):
        'Cria o layout do qr code'

        self.layout = []

        # Cabeçalho
        self.layout.append([sg.Text('Ticket', font=Util.getTitleFont(), justification='center')])
        self.layout.append([sg.Text('\n')])

        headings = ['Produto', 'Valor', 'Quantidade', 'Subtotal']

        list = []

        for product in self.productList:
            if isinstance(product, Item):
                subTotal = product.getPrice() * product.getAmount()
                list.append([product.getName(), '{:.2f}'.format(product.getPrice()), str(product.getAmount()), '{:.2f}'.format(subTotal)])
                self.totalValue += subTotal

        self.layout.append([sg.Table(values=list, 
                                     headings=headings, 
                                     max_col_width=35,
                                     auto_size_columns=True,
                                     display_row_numbers=False,
                                     justification='right',
                                     num_rows=10,
                                     key='-TABLE-',
                                     row_height=35)])

        # Total
        self.layout.append([sg.Text('Total:', font=Util.getFont(), justification='center'),
                            sg.Text('{:.2f}'.format(self.totalValue), font=Util.getFont(), justification='center')
                            ])

        self.layout.append([sg.Text('\n')])

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
        result = []
        for pro in self.productList:
            if not (isinstance(pro, Ingresso) and pro.getSessao() ==idSession):
                result.append(pro)
        self.productList = result

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

    def emptyProductList(self):
        self.productList = []

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
                self.createPdf()
                return True
            elif self.button == 'Voltar':
                self.screen.close()
                return False

    def createPdf(self):
        PAGE_SIZE = (8.27*inch, 11.69*inch)
        width, height = PAGE_SIZE

        self.c = canvas.Canvas("Ticket.pdf", pagesize=PAGE_SIZE)
        text = ''
        codQr = ''
        for product in self.productList:
            text += str(product) + "<br/>"
            codQr += product.getName() + str(product.getId())
        styles = getSampleStyleSheet()
        styleH = styles['Heading1']
        title = """Apresente seu ticket para retirada de produtos"""
        p = Paragraph(title, styleH)
        data = [[p]]
        table_side2 = Table(data, colWidths=5.25*inch, rowHeights=2.55*inch)
        table_side2.setStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("TOPPADDING", (0, 0), (-1, -1), 3),
                        ])
        styleH3 = styles['Heading3']

        front_page = []
        front_page.append(table_side2)
        p2 = Paragraph(text, styleH3)
        data = [[p2]]
        table_side2 = Table(data, colWidths=5.25*inch, rowHeights=2.55*inch)
        table_side2.setStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("TOPPADDING", (0, 0), (-1, -1), 3),
                        ])
        
        front_page.append(table_side2)
       
        f = Frame(inch*.25, inch*.5, width-.5*inch, height-1*inch, showBoundary=1)
        f.addFromList(front_page, self.c)
        self.c.showPage()
        front_page = []
        qr = QRCodeImage(codQr, size=75 * mm)
        data = [ [qr]]
        table_side2 = Table(data, colWidths=5.25*inch, rowHeights=2.55*inch)
        table_side2.setStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("TOPPADDING", (0, 0), (-1, -1), 3),
                        ])
        
        front_page.append(table_side2)
        f.addFromList(front_page, self.c)
        self.c.showPage()
        self.c.save()

    def coord(self, x, y, height, unit=1):
        x, y = x * unit, height -  y * unit
        return x, y
