def converte_decimal_binario(inteiro):
    binario = []
    coisa = ''
    while inteiro > 1:       
        numero = inteiro % 2
        inteiro = inteiro // 2
        binario.append(numero)
    binario.append(inteiro)
    for bit in reversed(binario):
        coisa += str(bit)
    return coisa

def conta_um_consecutivo_de_binario(binario):
    contador = 0
    maximo_de_um = 0
    for bit in binario:
        if bit == '1':
            contador += 1
        else:
            contador = 0
        if contador > maximo_de_um:
            maximo_de_um = contador
        
    return maximo_de_um

assert (converte_decimal_binario(232) == '11101000')
assert (converte_decimal_binario(532) == '1000010100')
assert (conta_um_consecutivo_de_binario('11101000') == 3)
