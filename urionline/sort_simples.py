# Fonte do exercício:
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

def sort_simples(*args):
    lista = list(args)
    elementos = len(lista) - 1
    organizado = False
    while not organizado:
        organizado = True
        for i in range(elementos):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                organizado = False
    return lista

assert(sort_simples(1, 98, 54, 68, 34, 76, 12) == [1, 12, 34, 54, 68, 76, 98])
    
