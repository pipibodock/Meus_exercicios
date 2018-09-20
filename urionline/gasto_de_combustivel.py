# Exercicio sugerido no site de exercicios de maratona de programação
# urionline / nivel: fácil

def calcula_gasto():
    km = int(input("distancia em km: "))
    gasolina = float(input("litros de combustível: "))
    consumo = km / gasolina
    mensagem = "O consumo foi de {:.3f} km/l".format(consumo)
    return mensagem

print(calcula_gasto())


