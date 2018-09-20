def media_ponderada(n1, n2, n3, n4):
    mp = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
    if mp < 5:
        print('Media: {:.1f}'.format(mp))
        print('Aluno Reprovado.')
    elif mp >= 5 and mp < 7:
        print('Media: {:.1f}'.format(mp))
        print('Aluno em exame.')
        nota = input()
        nota = float(nota)
        print('Nota do exame: {:.1f}'.format(nota))
        novo_mp = (mp + nota) / 2
        if novo_mp >= 5:
            print('Aluno aprovado.')
            print('Media final: {:.1f}'.format(novo_mp))
        else:
            print('Aluno reprovado')
            print('Media final: {:.1f}'.format(novo_mp))
    elif mp >= 7:
        print('Media: {:.1f}'.format(mp))
        print('Aluno Aprovado.')

media_ponderada(2.0, 4.0, 7.5, 8.0)
