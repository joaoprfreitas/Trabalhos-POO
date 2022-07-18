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
                linha.append(sg.Button(key='CAD{},{}'.format(i, j), image_data=self.arrayCadeiras[self.vazia], image_subsample=3, border_width=0, mouseover_colors='yellow'))

            linha.insert(4, sg.Push())
            linha.insert(9, sg.Push())
            self.layout.append(linha)
        
        self.layout.append([sg.Text('Legenda: branco - disponível, vermelho - selecionado, preto - indisponível', font=Util.getFont()), sg.Push(), sg.Text('Total selecionado: 0', size=18, font=Util.getFont(), key='-TOTAL-')])
        self.layout.append([sg.Button('Confirmar', key='-CONFIRMAR_BTT-', button_color='red')])

    def __init__(self):

        sg.theme(Util.theme())

        self.arrayCadeiras = [b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAA8UExURT09OgAAAEJCPgAAAAAAAAcHBgAAAAAAAAAAAAAAAAAAAAQEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAEdwTPQUmOsAAAAUdFJOUwT/AcS3C2hePfNREH7TGZ2wveIA5eGHnwAAAu5JREFUeNrt2wtvpCAQAGBWBUEBH/P//+tVHl7tbo/XmL1NZtLQNO3iVD5ER2UdQMfe2LA3b79j794+e/P2jwzeOwiMEBJCQvhhCHPi+LM7EH4Nl5VTOqScS0Y2FyF0dlqMUo9kqN0s04yNEGbRP/JD9SPvMBGCHB5loVaLiXDaH8VhJGAhhHP7yvTJMNHJLgEHIciw/U1IO3P+9fWvxkoduBiLghCs728Xc+YMB6t9yitHQahdZ73Mn9znoI3QjrCzpoDUDzb93I4QhNM3Fi5b/mOPCZoR8iF3NK/N7OQs7Qjt7v+T4mVWhInQinByM8BC6TLbyeN4oGQrQj+WAy9f5ucDr0oiSCEENwmXrvxcg29+IjYijAlUnGs5vQJaEYYEys+1/PQZmxHqvNn0YnBDAq0Io4HyE/6QwNsQnnuAEBJCQkgICSEhJISE8DMRHt+Oq33OGhGK0A2DMoRWLMPmYm9DaHwv6zJayEcYCwxn1CP8VjMSPBehfSqJ1SO89DJDFsLn7Tcg/JFBDsJQkrl+shrhNUQGwlgTG8ToYmlDuPpexKpCuSCJsPO1Fc1D7XtsQ6hDN0yo14WOJ4RsdSXB6CUmUItQx/nPlsuPvyP0l/X6/MXYhlCfi4rraO2SCH1xSZy7amxDqE9rrtazsiTCmMClRFOP8O+uDAkkEZ4JfN9zLQgv1a6VJxGeQ4CMMO6BJMKYADrCmAAhJISEkBB+KEIoD4aJcBsrwiAirA8khC0JoCBsSQAFYVMCGAiVqQiFeSS0FbFhHgnD0zklDS3HtBx//HIMl8vzltUwRBnCQcdwV+u9qAi3Gm7XjrIR3hXZCO9LIBPhbQnkIrxvD2QiNAN6mLIjITuCIzZd5ZEQr6k8EuI1lcsxWlO9HGM11csx2gPUhJAQEsJChDz5AHNpU4Zw79HDFCG88Xzgvz8n9DeX7gqdvm0HclO3xWq7jHvHs7wtXrz38fJ9Frirobft6G07etuOEBJCQvii+QNliOtOMZIBQQAAAABJRU5ErkJggg==',
        b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAABgUExURe4VHwAAAEFBPesVHxUAANISGgAAAAAAAExMTEJCQs8SGgEBAQAAABcXF+Li4v///78PFgEBAVMDBAAAAAAAAIsHDQAAAAAAAAAAADk5OcfHxwkJCQAAAMTExDgBAkdwTPnT8H8AAAAgdFJOU///BP///+Ie////IiD/////Ff+7z/9dPn3////5//8AelUuBAAAA45JREFUeNrtm+uWoyAMgPFWtlW7UK8z09X3f8sR1LaDipDQ7ekccs7gn06SwkdCiSH9IOELB/Ji+8IBg08BxcQJYvCpkNNB0sx24KGBE2TvA7xpi/IAkrJoG7739Yh+6nldXgOEXMuaYyBsigAtRQOGsK8Pk5IYJNM/H2oohKP9+FKxU5Ik4s9qOLHqEo8egCDsG2n/wiIiJIIMEbtIDxoIhFyufxXBTE8DiSrJAQdAWEv7BGU/mj2oe2sIeSnmP8LaHwaxCiW3hTBshv0fMwf2CRtIvDbWELZyAhzYH6egtYQwDIuRALx9QgQFhS2EEgHmxD5hOgg2IOzpEATikwv7ETkNEByoJYTSgcSJfZKMDthBODngwv7oQNbbRcLRASf2xyVILSFMZwYcTMK0BHYQZhMDLhYh8RB6CD2EHkIPoYfQQ+gh9BB6CD2EHkIPoYfwLSGkT4CwN4QwpDSl4qI4Zi7uKUkkLgoPjaiiDMrDHQh73hay3CHqFHFXYSeBJFUnrsyvUmnR8j0IU6VE0THkFV2nlC9SPYR8USLpEhR/3aKAQrUQtj8KJMF0YQ6fhGqpr9VBKC9oL2yueshyQ4cgMeqW+opQA6HYfMHDqotLVkw4EhtQ1TdtyHUI1fgnYhgmHAkHVH1KTCTa+DcqwAVhVZ8SE4k2Cc8OYIKwqk9JzESbhCcFqCCs6lMSM9EmYXUNIRCq+pTE7CH0EHoIPYRvASF5MYQsgbzAIQfmAsKgi8EiDkRoCLGChtCFAygIwa8RTadgNITiVAuEUJ6C8RAyeCRkgY+EPh37dOwh9BB6CN8SQnZPqcwFhIq+XQgD5UiBhVDVtwuh7kgFgVCVXQhXHEBBuOLAzj1h/iAu7gkVfbsQ5p/nm/zL8RCq+nYhzM9/b3LO8RCq+nYhXHMAXCzYcEAL4eOUfebyt+EJ+uuQxUt91hAGMUICAITPFi2EtHy+A8o71j8rJmG90dEDaLW5bvT+1PqyHU8ppZkyZLLb4+NoLB+yryNbUZVyk9rxQiQbxz/GcrzDttcBRox6wkAOUIfddlS3BNLiw3NeAuqw2y7VbM+vwfLx6/7cyHqYbrv1c8JNjuOU356zA5lRyx8xakykEAdSI7wsILRfgt8Gof02dAwhLBA5hNA2FP8vCDfTrnMIAQ44g5CXoLzvDMKwr607f4e8H7qDcOOcoBu4YfO3GYSQDvDf1fz+xOEbQ42q/1Y9OsAAAAAASUVORK5CYII=',
        b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAACXBIWXMAAIfGAACHxgEZv0K8AAAAUVBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABHcEx5KfpKAAAAG3RSTlP/5CIc35gD/I97kk/us1wybNcXPaH2qAzGhACTfL0WAAADJklEQVR42u3bbZOqIBQAYNSESPAFZUX//w+9QFnOBhvdPeTcued8cradeEISzoHIGgk6LqbQ5LfBxFA38xoPEmt+EgQqtPyBEAbMHK55T5jKtwBqYgQ4TPcGYJ4IfJgyGUA5ywAgck4FjCJH+4T1iQA6kTyAoUoDdHk6wEafBuC52ieSpgCozAY4VSkAZbIBxJgCqE7ZAKxJAZQFAhCAAAQgAAEIQAACEIAABCAAAf87oBqEC30YgHY+xj5DoSIJsDmoqgHLhdpcloWXbwBcwRSuWjRcq9WvilSzqm6hKGTFkg2uUEwf7z4HAYqb4R7S1ZNmoGHAWvdp5OPdDVdPAFoasr/nJ4umX0AdYJvr9rUvxh6laxK74RwM4AuUPFa63gDt9yF/gQNMFnD51iv+tuwAzyM+L+DRBTdAoz8N2B6LJPaVzw3YuoBEOiA/QDcPwBxoKTvg1gUk9sjLDmB63ADBhvL3APmiN0Dwmf8BgN8/sABak2MA/gViZ4HiKEBR+h5oyVEA0npAfRygdoDIrA8NYOf+KaSZLUANHwHowJZZb1cKJLZN9hHAqToWwI8GfLQHGFdN68J+90d/0aj6kwAyjCe7EmPuGMHkLuwfiuIFoC5A4nwDXJ+4HuCzlZeAVZUg4ZKAvwMAhgV0LjUproDCJT/da0BzBoil8oCiGW0s1zHA3XUjXgzCtYFJDuvrXCDceBDkPI5yu/4BIOyScQQqluh+/1m01vckKA4QdqLsBqjsvLAPoTbUm1GAsOYSsERi7DDoRTpA93StQEs007zSXqcCXPtKEsgDXW7sBwRhAOM0slD95TB4PqQWBriMpQUv07kJ4SkFDQJczjbDn2YqukAOGgQYledAXR84JRUE1G6lkKFO6t73+wo8CFjs/y0ZAP4o25IA4DkBHAEIQAACEPCvANoM5+uX9Q2A+gJv/7pJkwpYVXupIePSl+tbgFyBAAQgAAEICAKK4wC+TqhqKeWWtTIj25yAVpptpje22Vr5bTtK7wsA0QVPmsAF3X5Jxlrf8LZ9vwNkjh1gf34AAQhAAAIQsNVmTZUbcNuHYNsPUP8A460yaY2HQhUAAAAASUVORK5CYII='
        ]

        self.vazia = 0
        self.selecionada = 1
        self.ocupada = 2

        self.total = 10
        self.matriz_estados = [[self.vazia for i in range(self.total)] for j in range(self.total)]

        self.atualizarLayout()

    def createScreen(self):
        
        window = sg.Window(title='Selecione suas cadeiras!', layout=self.layout, element_justification='c', size=Util.screenSize())
        total = 0

        while True:
            event, values = window.read()
            print(event)

            if event == sg.WIN_CLOSED:
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

    def confirmar(self):

        for i in range(self.total):
            for j in range(self.total):
                elemento = self.matriz_estados[i][j]

                if elemento == self.selecionada:
                    self.matriz_estados[i][j] = self.ocupada

        self.atualizarLayout()



if __name__ == '__main__':
    cadeiras = Cadeiras()
    cadeiras.createScreen()
