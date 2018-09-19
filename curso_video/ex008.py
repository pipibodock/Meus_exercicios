
n = float(input('numero: '))
def operadores(var):
    metros = var
    dm = var * 10
    cm = var * 100
    mm = var * 1000
    print('o numero em metros {}, dm {}, cm {}, mm {}'.format(metros, dm, cm, mm))

print(operadores(n))

