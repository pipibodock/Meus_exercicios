import csv

data = [['1', 'coisa', 'animal', 'macaco'], ['2', 'vaca', 'doido']]
with open('arquivo.csv', 'w') as arquivo:
    escrevedor = csv.writer(arquivo)
    for i in range(len(data)):
        escrevedor.writerow(data[i])
