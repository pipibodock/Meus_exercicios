class Quadrado:

    def __init__(self):
        self._set_lado()

    def mudavalor(self):
        print('o lado do seu quadrado é: {}.'.format(self.lado))
        novo_tamanho = input('deseja mudar o lado tamanho do lado do seu quadrado? [s/n] > ')
        if novo_tamanho == 's':
            self._set_lado()

    def _set_lado(self):
        self.lado = int(input('informe o lado do seu quadrado: '))

    def calculaarea(self):
        print('o lado do seu quadrado é: {}.'.format(self.lado))
        area = (self.lado * self.lado)
        print('a área do seu quadrado é {}.'.format(area))

quadrado = Quadrado()
quadrado.mudavalor()
quadrado.calculaarea()
