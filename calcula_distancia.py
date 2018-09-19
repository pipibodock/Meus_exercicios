# fonte do exercicio: urionline
import math

def calcula_distancia_com_formula(x1, y1, x2, y2):
    area = ((x2 - x1)**2) + ((y2 - y1)**2)
    area = math.sqrt(area)
    msg = "{:.4f}".format(area)
    return msg

assert(calcula_distancia_com_formula(1.0, 7.0, 5.0, 9.0) == '4.4721')
assert(calcula_distancia_com_formula(-2.5, 0.4, 12.1, 7.3) == '16.1484')
