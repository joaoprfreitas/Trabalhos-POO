import PySimpleGUI as sg
from requests import Session
from Item import *
from Sessoes import *
from Util import *
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
    def getLayoutFood(self):
        sg.theme(Util.theme())
        layout = [
            [sg.Text('Cadastro de alimentos')],
            [sg.Text('Nome', size =(15, 1),key='name'), sg.InputText()],
            [sg.Text('Preço', size =(15, 1),key='price'), sg.InputText()],
            [sg.Text('Estoque', size =(15, 1), key='store'), sg.InputText()],
            [sg.Text('Imagem', key='image', size=(15,1)), sg.Input(size=(35,1)), sg.FileBrowse(file_types=[("Image files", "*.png *.jpeg")], key="-IN-")],
            [sg.Button("Cadastrar", key='create'), sg.Button("Parar de cadastrar", key='endCreate')]
        ]
        return layout
    def getLayoutSession(self):
        sg.theme(Util.theme())
        layout = [
            [sg.Text('Cadastro de sessões')],
            [sg.Text('Nome do filme', size =(15, 1),key='name'), sg.InputText()],
            [sg.Text('Preço', size =(15, 1),key='price'), sg.InputText()],
            [sg.Text('Tipo', size=(15,1)), sg.Listbox(values=['Dublado', 'Legendado'])],
            [sg.Text('Horário', size=(15,1)), sg.InputText()],
            [sg.Button("Cadastrar", key='create'), sg.Button("Parar de cadastrar", key='endCreate')]
        ]
        return layout
    def addFood(self, name, price, store):
        id = self.getLastId()
        id = id + 1
        self.products.append(Item(name, id, price, store))

    def addSession(self, name, price, type, dateTime):
        id = self.getLastId()
        id = id + 1
        self.products.append(Sessoes(name, id, price, dateTime, type))
    def create(self):
        layout = [
            [sg.Text("O que você deseja cadastrar?", size=(30,2), background_color='#b0aac2', text_color='#000814',auto_size_text=True, justification='center', font=(Util.getFont(), 20))],
            [sg.Button(button_text='Alimentos', key='food', button_color=['#000', '#3478C1']), sg.Button(button_text='Sessões',button_color=['#000', '#3478C1'], key='sessions')],

        ]
        sg.theme(Util.theme())
        window = sg.Window('Tela de cadastro', layout,size=(1080, 1080), location=(0,0), element_justification='c')
        isFood = False
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close' or event == 'endCreate':
                break
            if event == 'food':
                isFood = True
                window.close()
                layout = self.getLayoutFood()
                window = sg.Window('Tela de cadastro', layout,size=(1080, 1080), location=(0,0), element_justification='c')
            elif event == 'sessions':
                isFood = False
                window.close()
                layout = self.getLayoutSession()
                window = sg.Window('Tela de cadastro', layout,size=(1080, 1080), location=(0,0), element_justification='c')
            elif event == 'create':
                try:
                    if isFood:
                        self.addFood(values[0], float(values[1]), int(values[2]))
                    else:
                        self.addSession(values[0], float(values[1]), values[2][0], values[3])
                    sg.Popup("Produto cadastro com sucesso")
                except Exception as error:
                    sg.PopupError(error.args)
            

