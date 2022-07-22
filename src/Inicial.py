import PySimpleGUI as sg
from Util import *
 
class Inicial():
    'Cria a tela home do sistema'

    def __init__(self):
        'Define o layout da tela'
        
        sg.theme(Util.theme())
        botaoAdmin = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAEuSURBVFiF7ZZNTsJAGIYfUZawAs6gHIfIDWRnuAPErUq4Cmxwq1sLRrfegVJ3EuqiHdI0dPrNOMNPwpu8SRedPs9M/wZOMC3gAZgDP2kDYAg0fcO7wAqICxoCHZ/wjQauuvEh0UI/810rIbodFaFAH6gZCNeBe4PzS7NAPnvVwKVAZCEQSS4svQWxmS+QPIzOBL4tBERjpAJTC4GJxZjCmL6GS6DhUgDglgN+iLISoQa+9AlXaZL8eN5JXrUoPR7gYdnPaQNPwCdmX8MoHfMI3NiAq8AYWBtAi7oGRuk1xfAXB+B8Z1KJsQe46nMZvI2bZS/qL3CdBeb/BT3gsszyH7kC7nQnfOFv9qofOgGbjYdpwyzwIicQ6+wcZsuV7ge85SxwdAJve2C+7oEhzx9PygahyZ3/VAAAAABJRU5ErkJggg=='
        cor = sg.theme_background_color()

        layout = [
            [sg.Push(), sg.Button(image_data=botaoAdmin, border_width=0, button_color=(cor,cor), key='Admin Dashboard')],
            [sg.Image('../img/logo2.png', subsample=4)],
            [sg.Text("Garanta aqui seus ingressos!", font = Util.getFont())],
            [sg.Text("Prossiga para continuarmos.", font = Util.getFont())],
            [sg.VPush()],
            [sg.Button('Próximo', key='Proximo', font=Util.bigButtonFont(), button_color=Util.getButtonColor())],
            [sg.VPush()],
            [sg.VPush()]
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
            