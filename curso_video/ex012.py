n = float(input('preço do produto: R$ '))
porcentagem = float(input('desconto: '))

def descontos(var, **kwargs):
    desconto = kwargs.get('desconto')
    if desconto:
        promocao = (var / 100) * kwargs.get('desconto')
    else:
        promocao = 0
    return var - promocao

print(descontos(n))
print(descontos(n, desconto=porcentagem))
