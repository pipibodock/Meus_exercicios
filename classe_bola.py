import logging

logging.basicConfig(
    filename='classe_bola.log',
    level=logging.INFO,
    format='%(asctime)s, %(levelname)s:%(message)s',
    datefmt='%d/%m/%Y %H:%M',
)

class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocacor(self, novacor):
        self.cor = novacor
        logging.info('cor da bola foi alterada: nova cor - %s', novacor)
        return self.cor
        
    def mostracor(self):
        print('a cor da sua bola é: {} '.format(self.cor))
        logging.info('classe executada com sucesso')
        return self.cor

Bola('azul', 20, 'plastico').mostracor()
Bola('azul', 20, 'plastico').trocacor('roxo')

