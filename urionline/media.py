def calcula_media(*args):
    quantas = len(args)
    soma = 0
    for i in args:
        soma += i
    media = soma / quantas
    print(media)

calcula_media(1, 2, 3, 4)
calcula_media(10, 10, 10)
