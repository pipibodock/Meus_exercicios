# fonte: https://www.urionlinejudge.com.br/judge/pt/problems/view/1043

def area_perimetro(var1, var2, var3):
    condicao1 = (var2 - var3) < var1 < (var2 + var3)
    condicao2 = (var3 - var1) < var2 < (var3 + var1)
    condicao3 = (var1 - var2) < var3 < (var1 + var2)
    if condicao1 and condicao2 and condicao3:
        perimetro = var1 + var2 + var3
        msg = 'perimetro: {:.1f}'.format(perimetro)
    else:
        area = ((var1 + var2)/2) * var3
        msg = 'area: {:.1f}'.format(area)
    return msg

assert(area_perimetro(6.0, 4.0, 2.0) == 'area: 10.0')
assert(area_perimetro(6.0, 4.0, 2.1) == 'perimetro: 12.1')

