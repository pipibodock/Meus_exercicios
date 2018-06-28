# Base e Altura tenha no máximo 10 e Min 2
# print em forma de desenho

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def _seta_lado(self):
        self.base = max(min(self.base, 10), 2)
        self.altura = max(min(self.altura, 10), 2)

    def imagens(self):
        calcula_base = self.base - 2
        espaco_base = calcula_base * '─'
        print('┌' + espaco_base + '┐')

        for i in range(self.altura - 2):
            espaco = self.base - 2
            espaco = espaco * ' '
            print('│' + espaco + '│')

        print('└' + espaco_base + '┘')

retangulo = Retangulo(10, 10)
retangulo.imagens()
