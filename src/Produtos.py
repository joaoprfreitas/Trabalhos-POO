import PySimpleGUI as sg
from Util import *
from Item import *
from Estoque import *
 
class Produtos():  
    def __init__(self, productList):
        sg.theme(Util.theme())
        
        self.layoutProdutos = [
            [sg.Text("Produtos disponíveis", font=('Arial', 15, 'bold'))],
            
            [sg.Text("\n", font = Util.getFont)],
        ]

        for product in productList:
            if isinstance(product, Item):
                self.layoutProdutos.append([sg.Text(product.getName(), font = Util.getFont), sg.Input(key=product.getId(), size=(10, 1))])

        self.layoutProdutos.append(sg.Text("\n", font = Util.getFont))
        self.layoutProdutos.append(sg.Text("SubTotal", size=(15,1), key = 'sub', font=Util.getFont), sg.Text(size=(15,1), key='_OUT_'))
        self.layoutProdutos.append(sg.Button("PRÓXIMO", key='PRÓXIMO', font=Util.getFont))        

    def semEstoque(self):
        self.semEstoque = [
            [sg.Text("Produto em falta!\n", font = Util.getFont)]
        ]
        self.outEstoque = sg.Window("Erro", self.semEstoque, size=Util.screenSize(), element_justification='center' )

    def telaProdutos(self):  
        self.tela = sg.Window('Produtos', self.layoutProdutos, size=Util.screenSize(), element_justification='center') 

        subT = 0
        while True:      
            event, values = self.tela.read()
            
            if event == sg.WINDOW_CLOSED:
                self.semEstoque()
                return None
            if event == 'PRÓXIMO':
                #fechar janela     
                self.tela.close()
                return True
            if event == 'coca7':
                for i in Estoque.products:
                    if i.getId == '0':
                        n = int(values['0'])
                        subT = (subT + 7)*n
                        self.tela['_OUT_'].update(subT)
                    else:
                        #Produto em falta
                        break
            if event == 'coca5':
                for i in Estoque.products:
                    if i.getId == '1':
                        n = int(values['1'])
                        subT = (subT + 5)*n
                        self.tela['_OUT_'].update(subT)
                    else:
                        #Produto em falta
                        break
            if event == 'sp4':
                for i in Estoque.products:
                    if i.getId == '2':
                        n = int(values['2'])
                        subT = (subT + 4)*n
                        self.tela['_OUT_'].update(subT)   
                    else:
                        #Produto em falta
                        break                             
            if event == 'pm10':
                for i in Estoque.products:
                    if i.getId == '3':    
                        n = int(values['3'])
                        subT = (subT + 10)*n
                        self.tela['_OUT_'].update(subT)
                    else:
                        break
            if event == 'pg14':
                for i in Estoque.products:
                    if i.getId == '4':
                        n = int(values['4'])
                        subT = (subT + 14)*n
                        self.tela['_OUT_'].update(subT)
                    else:
                        break
            if event == 'd10':
                for i in Estoque.products:
                    if i.getId == '5':
                        n = int(values['5'])
                        subT = (subT + 10)*n
                        self.tela['_OUT_'].update(subT)
                    else:
                        break
            if event == 'r9':
                for i in Estoque.products:
                    if i.getId == '6':        
                        n = int(values['6'])
                        subT = (subT + 9)*n
                        self.tela['_OUT_'].update(subT)
                    else:
                        break
if __name__ == '__main__':
    ini = Produtos()
    ini.telaProdutos()

    