import PySimpleGUI as sg
from Item import *
from Sessoes import *
from Util import *
from Ingresso import *

class Estoque():
    products = []
    def __init__(self):
        self.addSession("Meu Malvado Favorito 1", 17.50, "Dublado", "12:00", "../img/mf1.png")
        self.addSession("Meu Malvado Favorito 2", 17.50, "Dublado", "15:00", "../img/mf2.png")
        self.addFood("Pipoca grande", 10.30, 100, 'noImage')
        self.addFood("Pipoca média", 7.30, 100, 'noImage')
        self.addFood("Pipoca pequena", 5.30, 100, 'noImage')

    def searchProduct(self, id:int):
        if  type(id) != int:
            raise Exception("Id must be integer")
        item = filter(lambda p: p.id == id, self.products)
        return item

    def getLastId(self):
        size = len(self.products)
        if size == 0:
            return 0
        item = self.products[size -1]
        return item.id

    def getProducstList(self):
        return self.products

    def getLayoutFood(self):
        sg.theme(Util.theme())
        layout = [
            [sg.Text('Cadastro de alimentos',size=(30,2),auto_size_text=True, justification='center', font=Util.getTitleFont())],
            [sg.Text('\n\n\n\n')],
            [sg.Text('Nome', size =(15, 1)), sg.InputText(key='name', size=(50,1))],
            [sg.Text('Preço', size =(15, 1)), sg.InputText(key='price', size=(50,1))],
            [sg.Text('Estoque', size =(15, 1)), sg.InputText(key='store', size=(50,1))],
            [sg.Text('Imagem',size=(15,1)), sg.Input(key='image',size=(41,1)), sg.FileBrowse(file_types=[("Image files", "*.png *.jpeg")], key="-IN-")],
            [sg.Text('\n\n\n')],
            [sg.Button("Cadastrar", key='create'), sg.Button("Parar de cadastrar", key='endCreate'), sg.Button("Voltar", key='returnHome')]
        ]
        return layout

    def getLayoutSession(self):
        sg.theme(Util.theme())
        layout = [
            [sg.Text('Cadastro de sessões', size=(30,2),auto_size_text=True, justification='center', font=Util.getTitleFont())],
            [sg.Text('\n\n\n')],
            [sg.Text('Nome do filme', size =(15, 1)), sg.InputText(key='name', size=(50,1))],
            [sg.Text('Preço', size =(15, 1)), sg.InputText(key='price', size=(50,1))],
            [sg.Text('Tipo', size=(15,1)), sg.Listbox(values=['Dublado', 'Legendado'], key='type', size=(48,2))],
            [sg.Text('Horário', size=(15,1)), sg.InputText(key='dateTime', size=(50,1))],
            [sg.Text('Imagem', size=(15,1)), sg.Input(key='image',size=(41,1)), sg.FileBrowse(file_types=[("Image files", "*.png *.jpeg")], key="-IN-")],
            [sg.Text('\n\n\n')],
            [sg.Button("Cadastrar", key='create'), sg.Button("Parar de cadastrar", key='endCreate'), sg.Button("Voltar", key='returnHome')]
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

    def sell(self, item):
        if isinstance(item, Ingresso):
            movie = list(self.searchProduct(item.getSessao()))[0]
            chairs = movie.getCadeiras()
            chairs.confirmar(True)
        else:
            product = list(self.searchProduct(item.getId()))[0]
            product.sell(item.getAmount())

    def getSessionListLayout(self):
        sg.theme(Util.theme())
        layout = [[sg.Push(), sg.Text('', key='esquerda')]]

        key = 0
        self.listaChaves = []

        for movie in self.products:
            if isinstance(movie, Sessoes):
                colunaTexto = sg.Column([[sg.Text(movie.getName(), font=Util.getFont())],
                                         [sg.Text('\n')],
                                         [sg.Text('Preço: R${:.2f}'.format(movie.getPrice()), font=('Ubuntu', 12, 'bold'))],
                                         [sg.Text('Horário: {}'.format(movie.getHorario()), font=('Ubuntu', 12, 'bold'))]])

                colunaImagem = sg.Column([[sg.Image(movie.getImagePath())]])

                colunaAtual = sg.Column([[colunaImagem, sg.Push(), colunaTexto],
                                         [sg.VPush()]],
                                         visible=True if key==0 else False, key='COL{}'.format(key))

                layout[0].append(colunaAtual)
                self.listaChaves.append((key, movie.getId()))

                key += 1

        self.total = key
        layout[0].extend([sg.Text('            ', key='placeholder'), sg.Button('Próximo\nfilme', key='BTT_DIR', size=(8,2))])
        layout.append([sg.Push(), sg.Button('Confirmar', font=Util.getFont(), key='Confirmar'), sg.Button('Voltar', font=Util.getFont(), key='Voltar'), sg.Push()])
        
        return layout
        

    def createScreenSessionsList(self):
        tela = sg.Window('Sessões Disponíveis', self.getSessionListLayout(), size=Util.screenSize(), element_justification='center', font=Util.getFont()) 
        index = 0

        while True:      
            event, values = tela.read()
            
            if event == sg.WINDOW_CLOSED:
                return None

                # Dispara a tela de cadeiras
            elif event == 'Voltar':
                tela.close()
                return False

            elif event == 'BTT_DIR':

                tela['BTT_DIR'].update(visible=False)
                tela['placeholder'].update(visible=False)
                
                tela['COL{}'.format(self.listaChaves[index][0])].update(visible=False)
                index = (index+1) % len(self.listaChaves)
                tela['COL{}'.format(self.listaChaves[index][0])].update(visible=True)
                
                tela['placeholder'].update(visible=True)
                tela['BTT_DIR'].update(visible=True)

            elif event != None:
                item = list(self.searchProduct(self.listaChaves[index][1]))[0]
                if isinstance(item, Sessoes):
                    tela.close()
                    cadeiras = item.getCadeiras()
                    tickets = cadeiras.createScreen()

                    if tickets == None:
                        return None
                        
                    listTicket = []
                    for ticket in tickets:
                        chair = str(ticket[0]) + str(ticket[1])
                        listTicket.append(Ingresso(item.getName(), chair, item.getId(), item.getPrice()))
                return listTicket, item.getId()


                
    def createScreen(self):
        layout = [
            [sg.Text("O que você deseja cadastrar?", size=(30,2), auto_size_text=True, justification='center', font=Util.getTitleFont())],
            [sg.Text('\n\n\n\n\n')],
            [sg.Button("Voltar", key='return', button_color=Util.getButtonColor(), font=Util.bigButtonFont()),
             sg.Button(button_text='Alimentos', key='food', button_color=Util.getButtonColor(), font=Util.bigButtonFont()),
             sg.Button(button_text='Sessões', button_color=Util.getButtonColor(), key='sessions', font=Util.bigButtonFont())
            ]
        ]
        sg.theme(Util.theme())
        window = sg.Window('Tela de cadastro', layout,size=Util.screenSize(), element_justification='c', font=Util.getFont())
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close':
                window.close()
                return None
            elif event == 'food':
                window.close()
                return 1
            elif event == 'sessions':
                window.close()
                return 2
            elif event == 'return':
                window.close()
                return False    
        
    def createScreenFood(self):
        layout = self.getLayoutFood()
        window = sg.Window('Tela de cadastro', layout,size=Util.screenSize(), element_justification='c')
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close':
                window.close()
                return None
            elif event == 'endCreate':
                window.close()
                return True
            elif event == 'returnHome':
                window.close()
                return False 
            elif event == 'sessions':
                window.close()
                layout = self.getLayoutSession()
                window = sg.Window('Tela de cadastro', layout,size=Util.screenSize(), element_justification='c')
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
                

                    window.Element('name').Update('')
                    window.Element('price').Update('')
                    window.Element('image').Update('')

                    sg.Popup("Produto cadastro com sucesso")
                except Exception as error:
                    sg.PopupError(error.args)

    def createScreenSession(self):
        layout = self.getLayoutSession()
        window = sg.Window('Tela de cadastro', layout,size=Util.screenSize(), element_justification='c')
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close':
                window.close()
                return None
            elif event == 'endCreate':
                window.close()
                return True
            elif event == 'returnHome':
                window.close()
                return False 
            elif event == 'sessions':
                window.close()
                layout = self.getLayoutSession()
                window = sg.Window('Tela de cadastro', layout,size=Util.screenSize(), element_justification='c')
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
            
if __name__ == '__main__':
    estoque = Estoque()
    estoque.createScreenSessionsList()