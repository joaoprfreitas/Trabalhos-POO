from Estoque import *
from Inicial import *
from Carrinho import *
from Pagamento import *
from Cadeiras import *
from Login import *

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

    FINISH = 9

if __name__ == '__main__':
    screen = Flags.HOME
    totalValue = 0
    userInfos = None

    stock = Estoque()
    cart = Carrinho()
    chairs = Cadeiras()

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
            print('MOVIES')

        elif screen is Flags.CHAIRS:
            next = chairs.createScreen()

            if next is None:
                screen = Flags.HOME
            elif next:
                screen = Flags.PRODUCTS
            else:
                screen = Flags.MOVIES

        elif screen is Flags.PRODUCTS:
            print("PRODUCTS")
            
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
            print("QRCODE")

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
            else:
                screen = Flags.HOME

        elif screen is Flags.FINISH:
            break

