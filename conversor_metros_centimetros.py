metros = input('entre com o comprimento em Metros: ')
metros = metros.replace(',', '.')
metros = float(metros)
centimetros = metros * 100
print('a sua metragem em centimetros é de: ', centimetros)
