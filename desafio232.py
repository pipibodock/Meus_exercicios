#escreva uma função que encontre a primeira ocorrencia de um item em uma lista e me dê a posição dela.

#Não pode usar funcões já existentes do python para isso.

def encontra_posicao(lista, buscado):
    contador = 0
    for i in lista:
        if buscado == i:
            return contador
        contador +=1

lista = [1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9]
print(encontra_posicao(lista, 4))
