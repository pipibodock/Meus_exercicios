class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocacor(self, novacor):
        self.cor = novacor
        return self.cor
        
    def mostracor(self):
        print('a cor da sua bola é: {} '.format(self.cor))
        return self.cor

#Bola('azul', 20, 'plastico').mostracor()
#Bola('azul', 20, 'plastico').trocacor()

