# Link para a fonte do problema:
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

def cordenada_ponto(x, y):
    if x == 0 and y == 0:
        msg = 'origem'
    elif x == 0 and y != 0:
        msg = 'Eixo Y'
    elif y == 0 and x != 0:
        msg = 'Eixo X'
    elif x > 0 and y > 0:
        msg = 'Q1'
    elif x < 0 and y < 0:
        msg = 'Q3'
    elif x > 0 and y < 0:
        msg = 'Q4'
    elif x < 0 and y > 0:
        msg = 'Q3'
    return msg

assert(cordenada_ponto(4.5, -2.2) == 'Q4')
assert(cordenada_ponto(0.1, 0.1) == 'Q1')
assert(cordenada_ponto(0.0, 0.0) == 'origem')
assert(cordenada_ponto(0.0, 1.0) == 'Eixo Y')
assert(cordenada_ponto(0.0, -2.0) == 'Eixo Y')
assert(cordenada_ponto(2.0, 0.0) == 'Eixo X')
assert(cordenada_ponto(-20.0, 0.0) == 'Eixo X')
