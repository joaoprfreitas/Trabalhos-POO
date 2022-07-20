import PySimpleGUI as sg
from Util import *
 
class Inicial():
    'Cria a tela home do sistema'
    def __init__(self):
        'Define o layout da tela'
        sg.theme(Util.theme())

        layout = [
            [sg.HSep()],
            [sg.Text("\n", font = Util.getFont)],
            [sg.Text("CINEMARK\n", font = Util.getTitleFont())],
            [sg.HSep()],
            [sg.Text("\n", font = Util.getFont)],
            [sg.Text("Garanta aqui seus ingressos!", font = Util.getFont)],
            [sg.Text("Prossiga para continuarmos.", font = Util.getFont)],
            [sg.Text("\n", font = Util.getFont)],
            [sg.HSep()],
            [sg.Frame('Cliente', [
                                  [sg.T(s=100)],
                                  [sg.Button('Proximo', key='Proximo', font=Util.bigButtonFont(), button_color=Util.getButtonColor())]
                                 ], element_justification='center')],
            [sg.Text("\n\n", font = Util.getFont)],
            [sg.Frame('Admin', [
                                [sg.T(s=100)],
                                [sg.Button('Admin Dashboard', key='Admin Dashboard', font=Util.getFont(), button_color=Util.getButtonColor())]
                               ], element_justification='center')]
        ]
        
        self.tela = sg.Window('Bem Vindo', layout, size=Util.screenSize(), element_justification='center') 
       
    def TelaInicial(self):
        'Inicia a tela, e retorna True, False ou None para o controle'
        while True:
            eventos, valores = self.tela.read()
            if eventos == sg.WIN_CLOSED:
                return None
            elif eventos == 'Proximo':
                self.tela.close()
                return True
            elif eventos == 'Admin Dashboard':
                self.tela.close()
                return False
            
if __name__ == '__main__':
    ini = Inicial()
    ini.TelaInicial()
    