valor = str(input())
valor = valor.split(".")
valor_notas = int(valor[0])
valor_moedas = int(valor[1])
notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]
resultado = []
for n in notas:
    resultado.append(valor_notas//n)
    valor_notas = valor_notas - (valor_notas//n) * n

if valor_notas == 1:
    valor_moedas += 100


for n in moedas:
    resultado.append(valor_moedas//n)
    valor_moedas = valor_moedas - (valor_moedas//n) * n

print("NOTAS:\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00\nMOEDAS:\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01".format(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11]))
