n = float(input('quantos reais vc tem? R$ '))
y = float(input('qual o valor atual do dollar?: $ '))
def cambio(**kwargs):
    cambiado = kwargs.get('real') // kwargs.get('dollar')
    return 'voce pode comprar {} dolars.'.format(cambiado)

print(cambio(real=n, dollar=y))
