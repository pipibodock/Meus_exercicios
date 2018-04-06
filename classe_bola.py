class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocacor(self):
        novacor = input('Qual a nova cor que deseja colocar na bola?')
        self.cor = novacor
        print('cor agora é {}'.format(self.cor))
        
    def mostracor(self):
        print('a cor da sua bola é: {} '.format(self.cor))

Bola('azul', 20, 'plastico').mostracor()
Bola('azul', 20, 'plastico').trocacor()

