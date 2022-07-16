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
            [sg.Text('Cadastro de alimentos',size=(30,2), background_color='#b0aac2', text_color='#000814',auto_size_text=True, justification='center', font=(Util.getFont(), 20))],
            [sg.Text('Nome', size =(15, 1)), sg.InputText(key='name')],
            [sg.Text('Preço', size =(15, 1)), sg.InputText(key='price')],
            [sg.Text('Estoque', size =(15, 1)), sg.InputText( key='store')],
            [sg.Text('Imagem',size=(15,1)), sg.Input(key='image',size=(35,1)), sg.FileBrowse(file_types=[("Image files", "*.png *.jpeg")], key="-IN-")],
            [sg.Button("Cadastrar", key='create'), sg.Button("Parar de cadastrar", key='endCreate')]
        ]
        return layout
    def getLayoutSession(self):
        sg.theme(Util.theme())
        layout = [
            [sg.Text('Cadastro de sessões', size=(30,2), background_color='#b0aac2', text_color='#000814',auto_size_text=True, justification='center', font=(Util.getFont(), 20))],
            [sg.Text('Nome do filme', size =(15, 1)), sg.InputText(key='name')],
            [sg.Text('Preço', size =(15, 1)), sg.InputText(key='price')],
            [sg.Text('Tipo', size=(15,1)), sg.Listbox(values=['Dublado', 'Legendado'], key='type')],
            [sg.Text('Horário', size=(15,1)), sg.InputText(key='dateTime')],
           [sg.Text('Imagem', size=(15,1)), sg.Input(key='image',size=(35,1)), sg.FileBrowse(file_types=[("Image files", "*.png *.jpeg")], key="-IN-")],

            [sg.Button("Cadastrar", key='create'), sg.Button("Parar de cadastrar", key='endCreate')]
        ]
        return layout
    def addFood(self, name, price, store, image):
        id = self.getLastId()
        id = id + 1
        self.products.append(Item(name, id, price, store, image))

    def addSession(self, name, price, type, dateTime, image):
        id = self.getLastId()
        id = id + 1
        self.products.append(Sessoes(name, id, price, dateTime, type, image))
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
                    if values['name'] == "":
                        sg.PopupError("O campo nome é obrigatório")
                        window.Element('name').SetFocus(True)
                        continue
                    if values['price'] == "":
                        sg.PopupError("O campo preço é obrigatório")
                        window.Element('price').SetFocus(True)
                        continue
                    price = 0
                    try:
                        price = float(values['price'])
                    except ValueError:
                        sg.PopupError("O campo preço deve ser um número")
                        window.Element('price').SetFocus(True)
                        continue
                
                    if price <= 0:
                        sg.PopupError("O campo Preço deve ser maior que zero")
                        window.Element('price').SetFocus(True)
                        continue

                    if isFood:
                        if values['store'] == "":
                            sg.PopupError("O campo Estoque é obrigatório")
                            window.Element('store').SetFocus(True)
                            continue
                        store = 0
                        try:
                            store = int(values['store'])
                        except ValueError:
                            sg.PopupError("O campo Estoque deve ser um número inteiro")
                            window.Element('store').SetFocus(True)
                            continue
                        if store <=0:
                            sg.PopupError("O campo Estoque deve ser maior que zero")
                            window.Element('store').SetFocus(True)
                            continue
                        if values['image'] == "":
                            sg.PopupError("O campo imagem é obrigatório")
                            window.Element('image').SetFocus(True)
                            continue
                        self.addFood(values['name'], price, int(values['store']), values['image'])
                        window.Element('store').Update('')
                    else:
                        if values['type'] == []:
                            sg.PopupError("O campo Tipo é obrigatório")
                            window.Element('type').SetFocus(True)
                            continue
                        if values['dateTime'] == "":
                            sg.PopupError("O campo Horário é obrigatório")
                            window.Element('dateTime').SetFocus(True)
                            continue
                        time = values['dateTime'].split(":")
                        if len(time) !=2:
                            sg.PopupError("O campo Horário deve ser seguir a formatação HH:mm")
                            window.Element('dateTime').SetFocus(True)
                            continue
                        hour = 0
                        minuts = 0
                        try:
                            hour = int(time[0])
                            minuts = int(time[1])
                        except ValueError:
                            sg.PopupError("O campo Horário deve ser seguir a formatação HH:mm, utilize apenas números")
                            window.Element('dateTime').SetFocus(True)
                            continue
                        if hour > 23 or hour < 0 or minuts > 59 or minuts < 0:
                            sg.PopupError("Horário inválido")
                            window.Element('dateTime').SetFocus(True)
                            continue
                        if values['image'] == "":
                            sg.PopupError("O campo imagem é obrigatório")
                            window.Element('image').SetFocus(True)
                            continue
                        self.addSession(values['name'], price, values['type'][0], values['dateTime'], values['image'])
                        window.Element('dateTime').Update('')

                    window.Element('name').Update('')
                    window.Element('price').Update('')
                    window.Element('image').Update('')

                    sg.Popup("Produto cadastro com sucesso")
                except Exception as error:
                    sg.PopupError(error.args)
            

