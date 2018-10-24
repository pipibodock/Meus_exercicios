# fonte do exercicio:
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

from unittest import TestCase

def calcula_tempo_jogo(inicio, fim):
    if fim <= inicio:
        diferenca = (24 - inicio) + fim
        if diferenca > 24:
            diferenca = 24
    else:
        diferenca = fim - inicio
        if diferenca < 1:
            diferenca = 1
    mensagem = 'O JOGO DUROU {} HORA(S)'
    return mensagem.format(diferenca)


class TempoDeJogoTestCase(TestCase):

    def test_funcao_recebe_variaveis(self):
        duracao = calcula_tempo_jogo(16, 2)

    def test_deve_retornar_diferenca_de_horas(self):
        duracao = calcula_tempo_jogo(16, 2)
        self.assertIn('10', duracao)

    def test_diferenca_deve_ser_min_de_uma_hora(self):
        duracao = calcula_tempo_jogo(16, 16.30)
        self.assertIn('1', duracao)

    def test_diferenca_deve_ser_max_vinte_quatro_horas(self):
        duracao = calcula_tempo_jogo(16, 16)
        self.assertIn('24', duracao)

