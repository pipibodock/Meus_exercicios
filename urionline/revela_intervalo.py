def intervalo(arg):
    if arg < 0:
        msg = 'Fora de Intervalo'
    elif arg <= 25:
        msg = 'Intervalo [0, 25]'
    elif arg > 25 and arg <= 50:
        msg = 'Intervalo (25, 50]'
    elif arg > 50 and arg <= 75:
        msg = 'Intervalo (50, 75]'
    elif arg > 75 and arg <= 100:
        msg = 'Intervalo (75, 100]'
    else:
        msg = 'Fora de Intervalo'
    return msg

assert(intervalo(25.01) == 'Intervalo (25, 50]')
assert(intervalo(25.00) == 'Intervalo [0, 25]')
assert(intervalo(100.00) == 'Intervalo (75, 100]')
assert(intervalo(-25.02) == 'Fora de Intervalo')
