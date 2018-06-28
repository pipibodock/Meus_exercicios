def soma_coisas(*args):
    bolso = 0
    for arg in args:
        bolso += arg
    return bolso


def soma_coisa(arg1, arg2):
    resultado = arg1 + arg2
    return resultado

print(soma_coisa(2, 3))

def entende_o_objeto(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

entende_o_objeto(nome='fellipe', idade=29)


def alguma_coisa(**kwargs):
    referencias = {
        'nome':'fellipe',
        'idade': 29,
        'endereço': 'mundo',
}

    referencias.update(kwargs)
    print(referencias)

alguma_coisa(nome='alguem', idade=2, endereço='casa')
