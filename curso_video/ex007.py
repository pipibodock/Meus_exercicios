def calcula_media(*args):
    soma = 0
    contador = 0
    for arg in args:
        soma += arg
        contador += 1
    return 'a média é {}'.format(soma // contador)

def calcula_media_denovo(*args):
    return 'a média é {}'.format(sum(args) // len(args))

print(calcula_media(1, 2, 3, 4, 5))
print(calcula_media_denovo(10, 10, 10))

