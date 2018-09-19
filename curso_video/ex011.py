y = float(input('largura da parede: '))
z = float(input('altura da parede: '))
def construcao(**kwargs):
    area = kwargs.get('largura') * kwargs.get('altura')
    tinta = area / 2
    print('com suas medias voce possui uma área de {}m².'.format(area))
    print('precisará de {} litros de tinta para pintar.'.format(tinta))

construcao(largura=y, altura=z)
