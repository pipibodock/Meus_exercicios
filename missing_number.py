# How do you find the missing number in a given integer array of 0 to 100?

lista = []
for i in range(0, 101):
    lista.append(i)
lista.pop(47)

def missing_number():
    for i in range(0, 101):
        if lista[i] != i:
            return i
            break

assert(missing_number() == 47)
