class Retangulo:

    def __init__(self):
        self._seta_lado()

    def _seta_lado(self):
        self.base = int(input('insira a base do seu retangulo: '))
        self.altura = int(input('insira a altura do seu retangulo: '))
        self._mostra_lado()

    def muda_lado(self):
        novo_lado = input('gostaria de mudar o valor das suas medidas? [s/n] ')
        if novo_lado == 's':
            self._seta_lado()
        self._mostra_lado()
    
    def _mostra_lado(self):
        print('suas medidas são: base {}, altura {}.'.format(self.base, self.altura))

    def calcula_area(self):
        area = self.base * self.altura
        print('A área do seu retangulo é: {}.'.format(area))

    def calcula_perimetro(self):
        perimetro = 2*(self.base + self.altura)
        print('A área do seu retangulo é: {}.'.format(perimetro))

retangulo = Retangulo()
retangulo.calcula_area()
retangulo.calcula_perimetro()
