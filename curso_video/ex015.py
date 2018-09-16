dias = float(input('dias de uso do carro: '))
km = float(input('km percorridos: '))

def locadora(dias, km):
    preco_dia = dias * 60
    preco_km = km * 0.15
    preco_final = preco_dia + preco_km
    return preco_final

def outra_locadora(arg1, arg2):
    return (dias * 60) + (km * 0.15)

print(locadora(dias, km))
print(outra_locadora(dias, km))
