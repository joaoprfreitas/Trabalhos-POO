import PySimpleGUI as sg
from Util import *
 
class Inicial():  
    def __init__(self):
        sg.theme(Util.theme())

        layout = [
            [sg.Text("\n\n\n\n\n\n\n\n\n", font = Util.getFont)],
            [sg.Text("Bem vindo ao CineVision\n", font = Util.getFont)],
            [sg.Text("Estou aqui para lhe auxiliar a comprar seus ingressos e\n", font = Util.getFont)],
            [sg.Text("os lanches para a hora do filme!\n", font = Util.getFont)],
            [sg.Button('Proximo', size=(10, 1), font=Util.getFont())]            
        ]
        self.tela = sg.Window('Bem Vindo', layout, size=Util.screenSize(), element_justification='center') 
       
    def TelaInicial(self):    
        while True:
            eventos, valores = self.tela.read()
            if eventos == sg.WIN_CLOSED:
                return None
            elif eventos == 'Proximo':
                return True
            
if __name__ == '__main__':
    ini = Inicial()
    ini.TelaInicial()
    