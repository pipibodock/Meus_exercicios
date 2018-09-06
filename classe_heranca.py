class Animal:
    def __init__(self, nome):
        self.nome = nome
        print('voce criou um animal')

    def andar(self):
        print('o animal andou')


class Mamifero(Animal):
    def __init__(self):
        print('voce criou um mamifero')

    def andar(self):
        print('o animal mamou, e depois..')
        super().andar()

dinossauro = Animal('rex')
dinossauro.andar()
mamador = Mamifero()
mamador.andar()
