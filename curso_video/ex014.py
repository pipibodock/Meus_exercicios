temp = float(input('temperatura em °C: '))

def converte_para_faren(var1):
    far = (1.8 * var1) + 32
    return far

print(converte_para_faren(temp))
