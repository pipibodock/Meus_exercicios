n = float(input('numero: '))

def operadores_matematicos(arg):
    dobro = arg * 2
    triplo = arg * 3
    raiz = arg**(1/2)
    print('dobre é {}, o triplo {} e a raiz é {}'.format(dobro, triplo, raiz))


operadores_matematicos(n)
