# fonte: urionline
import math

def formula(a, b, c):
    msg = 'impossivel calcular'
    if a == 0:
        return msg
    delta = b**2 - (4 * a * c)
    if delta <= 0:
        return msg
    raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
    return '{:.5f}'.format(raiz1), '{:.5f}'.format(raiz2)

assert(formula(10.0, 20.1, 5.1) == ('-0.29788', '-1.71212'))
assert(formula(0.0, 20.0, 5.0) == 'impossivel calcular')
assert(formula(10.0, 3.0, 5.0) == 'impossivel calcular')
