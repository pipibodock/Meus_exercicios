# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044
from unittest import TestCase

def multiplos(var1, var2):
    multiplos, multiplos2 = var1 % var2, var2 % var1
    if multiplos == 0 or multiplos2 == 0:
        mensagem = 'Sao multiplos'
    else:
        mensagem = 'Nao sao multiplos'
    return mensagem

class MultiplosTestCase(TestCase):

    def test_chama_multiplos(self):
        exercicio = multiplos(6, 24)
        self.assertEqual(exercicio, 'Sao multiplos')

    def test_chama_multiplos_oito(self):
        exercicio = multiplos(24, 8)
        self.assertEqual(exercicio, 'Sao multiplos')

    def test_chama_multiplos_vinte_e_quatro(self):
        exercicio = multiplos(8, 24)
        self.assertEqual(exercicio, 'Sao multiplos')

    def test_chama_nao_multiplos(self):
        exercicio = multiplos(6, 25)
        self.assertEqual(exercicio, 'Nao sao multiplos')

    def test_chama_nao_multiplos_vinte_e_cinco(self):
        exercicio = multiplos(25, 6)
        self.assertEqual(exercicio, 'Nao sao multiplos')

