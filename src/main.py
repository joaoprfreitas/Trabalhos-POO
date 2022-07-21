from Estoque import *
from Inicial import *
from Carrinho import *
from Pagamento import *
from Cadeiras import *
from Login import *
from Sessoes import *
from Produtos import *

from enum import Enum

class Flags(Enum):
    HOME = 0
    MOVIES = 1
    CHAIRS = 2
    PRODUCTS = 3
    CART = 4
    PAYMENT = 5
    QRCODE = 6

    LOGIN = 7
    ADMIN = 8
    ADMIN_SESSION = 9
    ADMIN_FOOD = 10

    FINISH = 11

if __name__ == '__main__':
    screen = Flags.HOME
    totalValue = 0
    userInfos = None

    stock = Estoque()
    cart = Carrinho()
    products = Produtos()

    # MOVIES
    # CHAIRS
    # PRODUCTS
    # CART
    # PAYMENT
    # QRCODE
    # ADMIN
    # ADMIN_SESSION
    # ADMIN_FOOD

    while True:
        if screen is Flags.HOME:
            homeScreen = Inicial()
            next = homeScreen.TelaInicial()

            if next is None:
                break
            elif next:
                screen = Flags.MOVIES
            else:
                screen = Flags.LOGIN

        elif screen is Flags.MOVIES:
            next = stock.createScreenSessionsList()

            if next is None:
                screen = Flags.FINISH
            elif next is False:
                screen = Flags.HOME
            else:
                cart.removeAllTickets(next[1])
                for ticket in next[0]:
                    cart.addProduct(ticket)
                screen = Flags.PRODUCTS

        elif screen is Flags.PRODUCTS:
            products.defProductsLayout(stock)
            next = products.telaProdutos(stock, cart)

            if next is None:
                screen = Flags.FINISH
            elif next is False:
                screen = Flags.MOVIES
            else:
                screen = Flags.CART

        elif screen is Flags.CART:
            cart.cartLayout()
            next = cart.createScreen()

            if next is None:
                screen = Flags.FINISH
            elif next:
                screen = Flags.PAYMENT
                totalValue = cart.getTotalValue()
            else:
                screen = Flags.PRODUCTS
            
        elif screen is Flags.PAYMENT:
            pScreen = PaymentScreen()
            next = pScreen.createScreen()

            if next is None:
                screen = Flags.FINISH
            elif next:
                screen = Flags.QRCODE
                userInfos = pScreen.getInfos()
                # Colocar para colocar as cadeiras selecionadas como ocupadas
            else:
                screen = Flags.CART        
            
        elif screen is Flags.QRCODE:
            cart.qrCodeLayout()
            next = cart.createScreenQrCode()
            cart.finishPayment(stock)

            if next is None:
                screen = Flags.FINISH
            elif next:
                screen = Flags.HOME
            else:
                screen = Flags.PAYMENT
        elif screen is Flags.LOGIN:
            loginScreen = Login()
            next = loginScreen.createScreen()

            if next is None:
                screen = Flags.FINISH
            elif next:
                screen = Flags.ADMIN
            else:
                screen = Flags.HOME
            
        elif screen is Flags.ADMIN:
            next = stock.createScreen()

            if next is None:
                screen = Flags.FINISH
            elif next == 1:
                screen = Flags.ADMIN_FOOD
            elif next == 2:
                screen = Flags.ADMIN_SESSION
            else:
                screen = Flags.HOME
        elif screen is Flags.ADMIN_FOOD:
            next = stock.createScreenFood()
            if next is None:
                screen = Flags.FINISH
            elif next:
                screen = Flags.HOME
            else:
                screen = Flags.ADMIN
        elif screen is Flags.ADMIN_SESSION:
            next = stock.createScreenSession()
            if next is None:
                screen = Flags.FINISH
            elif next:
                screen = Flags.HOME
            else:
                screen = Flags.ADMIN
        elif screen is Flags.FINISH:
            break

