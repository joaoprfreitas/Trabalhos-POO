import PySimpleGUI as sg
from Util import *
import re

class PaymentScreen():
    def __init__(self, totalValue):
        'Define o layout da página de pagamentos'

        sg.theme(Util.theme())

        self.layout = [
            [sg.Text('Insira as informações de pagamento', justification='center', font=Util.getTitleFont())],
            [sg.Text("\n", font = Util.getFont)],
            [sg.Text("Total: R${:.2f}".format(totalValue), font = Util.getFont)],
            [sg.Text("\n", font = Util.getFont)],
            [sg.Text('Nome', font=Util.getFont()),
             sg.Text('Sem caracteres especiais', font=Util.getFontPlaceholder())],
            [sg.InputText(key='name')],

            [sg.Text('Numero do cartão', font=Util.getFont()),
             sg.Text('(xxxxxxxxxxxxxxxx)', font=Util.getFontPlaceholder())],
            [sg.InputText(key='card')],

            [sg.Text('CPF', font=Util.getFont()),
             sg.Text('(xxxxxxxxxxx)', font=Util.getFontPlaceholder())],
            [sg.InputText(key='cpf')],

            [sg.Text('CVV', font=Util.getFont()),
             sg.Text('(xxx)', font=Util.getFontPlaceholder())],
            [sg.InputText(key='cvv')],

            [sg.Text('Validade', font=Util.getFont()),
             sg.Text('(mm/yy)', font=Util.getFontPlaceholder())],
            [sg.InputText(key='expiring-date')],

            [sg.Checkbox('Estou ciente e aceito os termos de Uso.', key='accepted')],

            [sg.Button('Voltar', size=(10, 1), font=Util.getFont(), button_color=Util.getButtonColor()),
             sg.Button('Pagar', size=(10, 1), font=Util.getFont(), button_color=Util.getButtonColor())]
        ]

        self.screen = sg.Window('Pagamento', self.layout, size=Util.screenSize(), element_justification='center')

    def getFields(self):
        'Retorna os campos preenchidos pelo usuário'
        return self.values

    def validateFields(self):
        'Valida os campos preenchidos pelo usuário'

        regexName = '^[a-zA-Z ]+$'
        regexCard = '^[0-9]{16}$'
        regexCPF = '^[0-9]{11}$'
        regexCVV = '^[0-9]{3}$'
        regexDate = '^[0-9]{2}/[0-9]{2}$'

        if self.values['name'] == '':
            sg.PopupError('O campo nome é obrigatório')
            return False
        if not re.match(regexName, self.values['name']):
            sg.PopupError('O campo nome deve conter apenas letras')
            return False
        if self.values['card'] == '':
            sg.PopupError('O campo numero do cartão é obrigatório')
            return False
        if not re.match(regexCard, self.values['card']):
            sg.PopupError('O campo numero do cartão está em formato incorreto (16 dígitos)')
            return False
        if self.values['cpf'] == '':
            sg.PopupError('O campo CPF é obrigatório')
            return False
        if not re.match(regexCPF, self.values['cpf']):
            sg.PopupError('O campo CPF está em formato incorreto (11 dígitos)')
            return False
        if self.values['cvv'] == '':
            sg.PopupError('O campo CVV é obrigatório')
            return False
        if not re.match(regexCVV, self.values['cvv']):
            sg.PopupError('O campo CVV está em formato incorreto (3 dígitos)')
            return False
        if self.values['expiring-date'] == '':
            sg.PopupError('O campo Validade é obrigatório')
            return False
        if not re.match(regexDate, self.values['expiring-date']):
            sg.PopupError('O campo Validade está em formato incorreto (mm/yy)')
            return False
        if not self.values['accepted']:
            sg.PopupError('Você deve aceitar os termos de uso')
            return False

        return True

    def getInfos(self):
        'Retorna as informações do pagamento'
        return self.values

    def createScreen(self):
        'Inicia a tela de pagamento, retornando True se o pagamento for realizado com sucesso ou False se o usuário cancelar o pagamento'

        while True:
            self.button, self.values = self.screen.read()
            if self.button == sg.WIN_CLOSED:
                return None
            elif self.button == 'Pagar':
                if self.validateFields():
                    self.screen.close()
                    return True
            elif self.button == 'Voltar':
                self.screen.close()
                return False
