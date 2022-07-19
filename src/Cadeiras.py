import PySimpleGUI as sg
from Util import Util
import math as m

class Cadeiras:

    def atualizarLayout(self):
        
        self.layout = []

        for i in range(self.total):

            letra = chr(ord('A')+i)
            linha = [sg.Text(letra, font='Consolas')]

            for j in range(self.total):
                linha.append(sg.Button(key='CAD{},{}'.format(i, j), image_data=self.arrayCadeiras[self.matriz_estados[i][j]], image_subsample=3, border_width=0, mouseover_colors='yellow'))

            linha.insert(4, sg.Push())
            linha.insert(self.total-1, sg.Push())
            self.layout.append(linha)
        
        self.layout.append([sg.Text('Legenda: branco - disponível, vermelho - selecionado, preto - indisponível', font=Util.getFont()), sg.Push(), sg.Text('Total selecionado: 0', size=18, font=Util.getFont(), key='-TOTAL-')])
        self.layout.append([sg.Button('Confirmar', key='-CONFIRMAR_BTT-', button_color='red')])

    def __init__(self):

        sg.theme(Util.theme())

        self.arrayCadeiras = [b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAM1BMVEU+PjsAAAAAAAAHBwYAAAAAAAAAAAAAAAAAAAAEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAABQJ24hAAAAEHRSTlMBxLgLaF7zPVEQfhnTnbDiq4ZQCwAAAeFJREFUeNrtmsuuqzAMRU3eb/j/r72qS3WlMzgExyhw6jVA6oBkYe+kKAIEQRAE4VFkH47xPsIl5FCLc9shbi018DtEs2z9uMVqYMWr7RyuZWAkrNtpir9gfleWQ8onJyubgd/nV8bnqHXU+rdL9mmPS8lM8X+Pt5rYfUd6KzeeJCYcbPGEplmWAhRCpHaDJcI4BtNnSbdtAYbRitbNiMmpDB1YiU9imBZCwBVAGMe7V+s8TwQUYT3F8hIIPIuwksNj5wkACpivr4AITBeQEIrAdAEJoQhMF5AQisB0gUeHUL8YrsA+zFmyqerNOiZQFNKqzYCcOmBAxgT+U4zunh9vZRVAaqTNTw8hzQBjx18BxJw4E1PGInVMoFnENNd9XGBw/vRJjB0TSLBjXO9BR8Pnj8AsABV/9mYnwYEAcaDWe7hkgL0CgShg2ATuUQENj2vBQAhv2QIJoYRwegskhN8UQlYBZQkUrhCS4aoAGaYQ/rEKEAVcIeA4d8JM4J77wDfthPJ3PL0FDw+hSh8afgtiCJQfA/ULXIQI7CF8SAWKYqcQ9gHNeQkEAU7uIqDh2ysgAtMFJIQi0C2A3ymzXs6FcF3YKfd4IXmAANTtQhIc45W7jJahg+gvQ4MgCIIg3I9/br+oxg2HUYwAAAAASUVORK5CYII=', b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAUVBMVEUAAABBQT0AAAAAAAABAQEAAAAAAAAAAAAAAAAAAADuFR8AAAAVAADSEhpMTExCQkLPEhoXFxfi4uL///+/DxYJCQlTAwSLBw04AQLHx8c5OTn4NLk0AAAACnRSTlMABOIfFc+7XT59hxcJ+QAAAuxJREFUeNrtm92SmzAMhWOwDaxxQ1Lzs/v+D1ows3EZT+xYEu001bkwNxnpYH0oGRRfNom/t/wr+QF63UT+U0LWIElBkV+2nVYVSEp3rcQV4SIbNRqERtVIDAStNmjpFn7/TWV29SCZXVUDhWDP30+zG6y1gy1cBjdP/e4AlP/S+vyT+0DITd5BCymC9PWfP5CaPQcSAEET8uMdNJfi/FJt+/9BoK0KSpZCINpx5c9RGHAriWNbDGEXNoBiC7pCCITQgQAKCnQphB4BR2PAJSB4aquuVgQGGgPDCkFVF0LgDVgaA9YbKMt/hoESCIIBuhIU5A8MUO5AUX7iEjCEDCFDyBAyhAwhQ8gQMoQMIUPIEDKEDCFDGErwEgSiXtVuBqheUm0G2i3qGlxk8l9kp6tNo1kdLLNF3/689NvkwgfVncwVodbmoMUh734xB+k6nV9GI5LFou4/5A8OUhB2hwGJQb8wn+N4XQoCof2I4nvq4ccNC8bAEsfTIgFhXR1f0DqDexhtH8WLemKy/w09rh3ZfouX7ImJ/hcCgBRuINUTM/0vGMDvQDCQgPDPGEhAeL4BhpAhZAgZQoYQAqGzqwbQ4iggNEsP1mLwECKFhxApPIQ+BlBmExpCMzkohG4yFBA6zF8XuBO+RSfkr2OGkCFkCP8/CF34SnVoCKN4eQjN4ScFFsIoXhbCSMgSREpDeL6BPITm9pvQBqJ4eQhvn/eHPm9YCKN4eQhv958P3W9YCKN4KQjpDdjIQB7CuAT7u2bQ4qISACA0PUIGAOG5ykGozOlSMjExEc2TEz2jKdb45OxPkx6byTrWPsQzX9eX9WW+B3WRZH52HGtn4/rjZV0DbJEAp82gBghPu9WJEnhf4RpKUFPlzzye43XNO4ZreNyoTtvl+sOW+HE9GKDKL6AGqCAAlOA9ISx5DCkhBBkghxDQiqkhLBQ9hGWihlAqUywl8RCGpVFVoVSDyx//TiiUJD98XqL3O/x+4vILq0asD505CzEAAAAASUVORK5CYII=',b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAARVBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADc6ur3AAAAFnRSTlMAG+SQIt+Ye+5PXLPXbD0yoajG9gyEeQcA8QAAApBJREFUeNrt2tuSoyAQgGFA5SCKBrTf/1FXkknIYSfibhN2a/q/Sk1NDZ89qZQS2Le51YsAf50epFnY8dysAatgDxMWpQGzMLfsSHwG7Px05PpnwM8fmIGCEtmFZeY0FGnMBcxQpoGzrKY0gDojUFAqmwewUKqOs4y4h1JplwXooFgmB9AKuEYAAhCAAAQgAAEIQAACEIAABCDADwXwQccCbFUBsOmcG30dQIpLwCv4Zl1Vyw61WMBqMEvWivwW7o7lMJ1Heuv3Gq78cMu6CPKAUx+vxg63vOLspfZxtS6iT3hbpFP3tHW9+w9XeAAbtz/3tq57eKrBA8zbn2rgqX5nAPiA9yMw4dMAME8DKA54OwITPg8I5m4AJygPeDcCp2sAgrsBTlADAKc0gCqA9P2BhDoAmNNNWB2AaFmshyqA9Hks6wEk21r8ZwDN+JL1y/k2+COA4NhL48AjoKsH6CoDVPeTJgCKmz7WMub6mOHyo4DBXRYarwcEBifEDkAKlJovgDgM4C1K/A8BmEXAFB9NxAUgtpd22geYBqH1MgFh3NZ6ASi3ZXS3AzAaMJJnAGixpaFxzl5fvwFow5gTgFIY768lhABfvQHonrFpAKSEY6zXkNoF6M3cekDLbwuNOh8QRuyzJPOyCUIGIK1vAbWRRUEmQN3dJmG+DZjaA6Qnlj4AcnN6BN0BBJN+EzExpWfQ9wDPyxyoG+NaPgMg49sF8JNsS2YA1u1nK+BnI2DNAKiSAEUAAhCAAAT4XwA94LceAfATYOfbfMAW7xuJWTO2LB9QJgIQgAAEIMD3AFEPIM4Aaa318JW3PStYf7+StZI/Hx/QEyvcpB++sCIAAQhAAAL8MwCn0z5t2bh/PEDyC7g6gJ5VJ8zJAAAAAElFTkSuQmCC'
        ]

        self.vazia = 0
        self.selecionada = 1
        self.ocupada = 2

        self.total = 10
        self.matriz_estados = [[self.vazia for i in range(self.total)] for j in range(self.total)]

        self.atualizarLayout()

    def createScreen(self):
        
        self.atualizarLayout()
        window = sg.Window(title='Selecione suas cadeiras!', layout=self.layout, element_justification='c', size=Util.screenSize())
        total = 0

        while True:
            event, values = window.read()
            print(event)

            if event == sg.WIN_CLOSED or event == '-CONFIRMAR-BTT-':
                break

            elif event[:3] == 'CAD':
                
                linha = int(event[3:event.find(',')])
                coluna = int(event[event.find(',')+1:])

                if self.matriz_estados[linha][coluna] == self.vazia or self.matriz_estados[linha][coluna] == self.selecionada:

                    self.matriz_estados[linha][coluna] = not self.matriz_estados[linha][coluna]
                    total += 2 * self.matriz_estados[linha][coluna] - 1
                    window[event].update(image_data=self.arrayCadeiras[self.matriz_estados[linha][coluna]], image_subsample=3)
                    window['-TOTAL-'].update('Total selecionado: {}'.format(total))

            print(total)

        window.close()
        return total

    def confirmar(self, situacao : bool):
        for i in range(self.total):
            for j in range(self.total):
                elemento = self.matriz_estados[i][j]

                self.matriz_estados[i][j] = self.vazia if situacao == False else self.ocupada

        self.atualizarLayout()

if __name__ == '__main__':
    cadeiras = Cadeiras()
    cadeiras.createScreen()
