# How do you find the largest and smallest number in an unsorted integer array?

def largest_and_smallest(*args):
    args = list(args)
    maior = args[0]
    menor = args[0]
    for i in args:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    return '{} / {}'.format(maior, menor)

assert(largest_and_smallest(2, 3, 4, 7, 9, 10, 29, 100) == '100 / 2')
assert(largest_and_smallest(-2, -3, -4, 7, 9, 23, 54, -10, -29, -100) == '54 / -100')
