import PySimpleGUI as sg
from Util import *

class TelaPagamento():
    def __init__(self):
        self.layout = [
            [sg.Text('Nome', key='name')],
            [sg.InputText()],
            [sg.Text('Numero do cartão', key='card')],
            [sg.InputText()],
            [sg.Text('CPF', key='cpf')],
            [sg.InputText()],
            [sg.Text('CVV', key='cvv')],
            [sg.InputText()],
            [sg.Text('Validade', key='expiring-date')],
            [sg.InputText()],
            [],
            [sg.Checkbox('Estou ciente e aceito os termos de Uso.', key='accepted')],
            [sg.Button('Pagar')]
        ]
        self.janela = sg.Window('Pagamento', self.layout, size=Util.screenSize())

        self.button, self.values = self.janela.read()

    def iniciar(self):
        print(self.values)


if __name__ == '__main__':
    pagamento = TelaPagamento();
    pagamento.iniciar();