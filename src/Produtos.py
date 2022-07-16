import PySimpleGUI as sg
from Util import *
 
class Produtos():  
    def __init__(self):
        sg.theme(Util.theme())

        produtos = [
            [sg.Text("Produtos disponíveis", font=('Arial', 15, 'bold'))],
            
            [sg.Text("\n", font = Util.getFont)],

            [sg.Text("Coca-Cola - 750ml - R$7,00\n", size=(50,1), font=Util.getFont), sg.InputText(key='0', size=(1,1)), sg.Button("Adicionar", key = 'coca7')],
            
            [sg.Text("Coca-Cola - 350ml - R$5,00\n", size=(50,1), font=Util.getFont), sg.InputText(key='1', size=(1,1)), sg.Button("Adicionar", key='coca5')],
            [sg.Text("Sprite - 350ml - R$4,00\n", size=(50,1), font=Util.getFont), sg.InputText(key='2', size=(1,1)), sg.Button("Adicionar", key='sp4')],
            [sg.Text("Pipoca Média - R$10,00\n", size=(50,1), font=Util.getFont), sg.InputText(key='3', size=(1,1)), sg.Button("Adicionar", key='pm10')],
            [sg.Text("Pipoca Grande - R$14,00\n", size=(50,1), font=Util.getFont), sg.InputText(key='4', size=(1,1)), sg.Button("Adicionar", key='pg14')],
            [sg.Text("Douritos 190g - R$10,00\n", size=(50,1), font=Util.getFont), sg.InputText(key='5', size=(1,1)), sg.Button("Adicionar", key='d10')],
            [sg.Text("Ruffles  185g - R$9,00\n", size=(50,1), key = 'ruf', font=Util.getFont), sg.InputText(key='6', size=(1,1)), sg.Button("Adicionar", key='r9')],            
            [sg.Text("\n", font = Util.getFont)],

            [sg.Text("SubTotal", size=(15,1), key = 'sub', font=Util.getFont), sg.Text(size=(15,1), key='_OUT_')],            
            [sg.Button('PRÓXIMO')]
        ]

        self.tela = sg.Window('Produtos', produtos, size=Util.screenSize(), element_justification='center') 
    def TelaProdutos(self):  
        subT = 0
        while True:      
            event, values = self.tela.read()
            
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'coca7':
                n = int(values['0'])
                subT = (subT + 7)*n
                self.tela['_OUT_'].update(subT)
            if event == 'coca5':
                n = int(values['1'])
                subT = (subT + 5)*n
                self.tela['_OUT_'].update(subT)
            if event == 'sp4':
                n = int(values['2'])
                subT = (subT + 4)*n
                self.tela['_OUT_'].update(subT)                                
            if event == 'pm10':
                n = int(values['3'])
                subT = (subT + 10)*n
                self.tela['_OUT_'].update(subT)
            if event == 'pg14':
                n = int(values['4'])
                subT = (subT + 14)*n
                self.tela['_OUT_'].update(subT)
            if event == 'd10':
                n = int(values['5'])
                subT = (subT + 10)*n
                self.tela['_OUT_'].update(subT)
            if event == 'r9':
                n = int(values['6'])
                subT = (subT + 9)*n
                self.tela['_OUT_'].update(subT)
            
if __name__ == '__main__':
    ini = Produtos()
    ini.TelaProdutos()
    