import PySimpleGUI as sg
from Estoque import *

flags = [{0: "HOME", 1: "ESTOQUE", 2: "CARRINHO", 3: "PEDIDOS", 4: "USUARIO"}]




#### Tela de cadastro #####
estoque = Estoque()

estoque.create()