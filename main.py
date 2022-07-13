import PySimpleGUI as sg
from Estoque import *



#### Tela de cadastro #####
estoque = Estoque()
layout = estoque.getLayout()
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
        layout = estoque.getLayout()
        window = sg.Window('Tela de cadastro', layout,size=(1080, 1080), location=(0,0))
    if event == 'create':
        name = values[0]
        price = values[1]
        store = values[2]
        estoque.addFood(name, float(price), int(store))
        
window.close()