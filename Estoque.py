import PySimpleGUI as sg
from Item import *
class Estoque():

    products = []

    
    def searchProduct(self, id:int):
        if  type(id) != 'int':
            raise Exception("Id must be integer")
        item = filter(lambda p: p.id == id, self.products)
        return item

    def getLastId(self):
        size = len(self.products)
        if size == 0:
            return 0
        item = self.products[size -1]
        return item.id
    def getLayout(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Cadastro de produtos')],
            [sg.Text('Nome', size =(15, 1),key='name'), sg.InputText()],
            [sg.Text('Preço', size =(15, 1),key='price'), sg.InputText()],
            [sg.Text('Estoque', size =(15, 1), key='store'), sg.InputText()],
            [sg.Button("Cadastrar", key='create'), sg.Button("Parar de cadastrar", key='endCreate')]
        ]
        return layout
    
    def addFood(self, name, price, store):
        id = self.getLastId()
        id = id + 1
        self.products.append(Item(name, id, price, store))

