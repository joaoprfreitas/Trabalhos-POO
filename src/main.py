from Estoque import *
from enum import Enum
from Inicial import *
from Carrinho import *
from Pagamento import *

class Flags(Enum):
    HOME = 0
    MOVIES = 1
    PRODUCTS = 2
    CART = 3
    PAYMENT = 4
    QRCODE = 5

    ADMIN = 6
    ADMIN_MOVIES = 7
    ADMIN_PRODUCTS = 8

    FINISH = 9


if __name__ == '__main__':
    screen = Flags.HOME
    totalValue = 0
    userInfos = None

    stock = Estoque()
    cart = Carrinho()

    while True:
        if screen is Flags.HOME:
            homeScreen = Inicial()
            next = homeScreen.TelaInicial()

            screen = Flags.FINISH if next is None else Flags.MOVIES

        elif screen is Flags.MOVIES:
            print("MOVIES")

        elif screen is Flags.PRODUCTS:
            print("PRODUCTS")
            
        elif screen is Flags.CART:
            cart.cartLayout()
            next = cart.createScreen()

            if next is None:
                screen = Flags.FINISH
            elif next is False:
                screen = Flags.PRODUCTS
            else:
                screen = Flags.PAYMENT
                totalValue = cart.getTotalValue()
            
        elif screen is Flags.PAYMENT:
            pScreen = PaymentScreen()
            next = pScreen.createScreen()

            if next is None:
                screen = Flags.FINISH
            elif next is False:
                screen = Flags.CART
            else:
                screen = Flags.QRCODE
                userInfos = pScreen.getInfos()
            
        elif screen is Flags.QRCODE:
            print("QRCODE")
            
        elif screen is Flags.ADMIN:
            print("ADMIN")
            
        elif screen is Flags.ADMIN_MOVIES:
            print("ADMIN_MOVIES")

        elif screen is Flags.ADMIN_PRODUCTS:
            print("ADMIN_PRODUCTS")

        elif screen is Flags.FINISH:
            break

