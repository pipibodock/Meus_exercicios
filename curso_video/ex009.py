n = int(input('digite um número para ver sua tabuada: '))

def tabuada(var):
    print('------------')
    for i in range(1, 11):
        print(var, 'x', i, '=', var * i)
    print('------------')

print(tabuada(n))
