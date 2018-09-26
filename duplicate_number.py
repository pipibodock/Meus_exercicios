# How do you find the duplicate number on a given integer array? 

lista = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
lista2 = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]

def search_duplicate(lista):
    verificador = None
    for i in lista:
        if i == verificador:
            print(i)
            return i
            break
        verificador = i

assert(search_duplicate(lista) == 6)
assert(search_duplicate(lista2) == 0)
assert(search_duplicate(lista3) == 11)
