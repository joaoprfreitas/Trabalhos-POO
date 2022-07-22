import PySimpleGUI as sg
from Util import Util

class Login:
    'Responsável pela tela de login'
    
    def __init__(self):
        'Cria o layout da tela de login'
        sg.theme(Util.theme())
        self.fonte = Util.getFont()

        imagem = b'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'
        cor = sg.theme_background_color()

        self.__layout = [[sg.Button(image_data=imagem, button_color=(cor, cor), border_width=0, image_subsample=20, key='-BTT-VOLTAR-'), sg.Push(), sg.Push(), sg.Text(text='   Tela de Login', font=self.fonte), sg.Push(), sg.Push(), sg.Push()],
                         [sg.Text(text='Usuário:', font=self.fonte), sg.Push(), sg.Input(key='-USUARIO-', do_not_clear=False, background_color='white')],
                         [sg.Text(text='Senha:', font=self.fonte), sg.Push(), sg.Input(key='-SENHA-', password_char='*', do_not_clear=False, background_color='white')],
                         [sg.Button('Logar', key='-LOGIN-', font=self.fonte, button_color=Util.getButtonColor())]]

    def popupError(self):
        'Define o layout do popup de Erro'
        sg.Window(title='ERRO', layout=[[sg.Text(text='Usuário ou senha inseridos incorretamente!', font=self.fonte)],
                                        [sg.Text(text='Tente novamente.', font=self.fonte)],
                                        [sg.Button(button_text='OK', button_color='red', font=self.fonte)]], element_justification='c').read(close=True)

    def popupSucesso(self):
        'Define o layout do popup de Sucesso'
        sg.Window(title='SUCESSO', layout = [[sg.Text(text='Login realizado com sucesso!', font=self.fonte)],
                                             [sg.Button('OK', font=self.fonte, button_color='green')]],
                                             element_justification='c', modal=True).read(close=True)

    def createScreen(self):
        'Inicia a tela de Login, e retorna True, False ou None para o controle'
        window = sg.Window('Login', self.__layout)
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                return None

            elif event == '-LOGIN-':
                usuario = values['-USUARIO-']
                senha = values['-SENHA-']
                    
                if (usuario == 'admin' and senha == 'admin'):
                    self.popupSucesso()
                    window.close()
                    return True

                else:
                    self.popupError()

            elif event == '-BTT-VOLTAR-':
                window.close()
                return False
