salario = float(input('salario: '))
aumento = float(input('aumento: '))

def calcula_aumento(arg1, arg2):
    porcento = arg1 * arg2 / 100
    novo = arg1 + porcento
    return '{:.2f}'.format(novo)

print(calcula_aumento(salario, aumento))
