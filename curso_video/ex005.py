n = float(input('digite um número: '))

def anterior_e_sucessor(arg):
    arg = int(arg)
    return 'anterior {} e sucessor {}.'.format((arg - 1), (arg + 1))

print(anterior_e_sucessor(n))
