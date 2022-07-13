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


    def create(self):
        layout = [
            [sg.Text("O que você deseja cadastrar")],
            [sg.Button(button_text='Alimentos', key='food'), sg.Button('Sessões', key='sessions')],

        ]
        window = sg.Window('Tela de cadastro', layout,size=(1080, 1080), location=(0,0))
        while True:
            event, values = window.read()
            print(values)
            if event == sg.WIN_CLOSED or event == 'Close':
                break
            if event == 'food':
                window.close()
                layout = self.getLayout()
                window = sg.Window('Tela de cadastro', layout,size=(1080, 1080), location=(0,0))
            if event == 'create':
                try:
                    name = values[0]
                    price = values[1]
                    store = values[2]
                
                    self.addFood(name, float(price), int(store))
                    sg.Popup("Produto cadastro com sucesso")
                except Exception as error:
                    sg.PopupError(error.args)


