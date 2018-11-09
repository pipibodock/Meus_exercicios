# Fonte do exercicio https://www.urionlinejudge.com.br/judge/pt/problems/view/1048
from unittest import TestCase

def calcula_salario(salario):
    salario = float(salario)
    mensagem = 'valor invalido'
    porcentagens = [15, 12, 10, 7, 4]
    if salario < 0:
        return mensagem
    elif salario <= 400.00:
        porcentagem = 15
        reajuste = (salario//100)*porcentagem
    elif salario > 400.00 and salario <= 800.00:
        porcentagem = 12
        reajuste = (salario//100)*porcentagem
    elif salario > 800.00 and salario <= 1200.00:
        porcentagem = 10
        reajuste = (salario//100)*porcentagem
    elif salario > 1200.00 and salario <= 2000.00:
        porcentagem = 7
        reajuste = (salario//100)*porcentagem
    elif salario > 2000.00:
        porcentagem = 4
        reajuste = (salario//100)*porcentagem
    novo_salario = 'novo salario: {:.2f}'.format(salario + reajuste)
    return novo_salario, reajuste, porcentagem

class CalculaSalarioTestCase(TestCase):

    def test_chama_funcao(self):
        calcula_salario(400.00)

    def test_calcula_reajuste_quatrocentos(self):
        response = calcula_salario(400.00)
        self.assertTupleEqual(('novo salario: 460.00', 60.00, 15), response)

    def test_calcula_reajuste_menor_que_zero(self):
        response = calcula_salario(-1)
        self.assertEqual('valor invalido', response)

    def test_calcula_reajuste_igual_zero(self):
        response = calcula_salario(0)
        self.assertTupleEqual(('novo salario: 0.00', 0.0, 15), response)

    def test_calcula_reajuste_quatrocentos_e_um(self):
        response = calcula_salario(400.01)
        self.assertTupleEqual(('novo salario: 448.01', 48.0, 12), response)

    def test_calcula_reajuste_oitocentos_e_um(self):
        response = calcula_salario(800.01)
        self.assertTupleEqual(('novo salario: 880.01', 80.0, 10), response)

    def test_calcula_reajuste_mil_e_duzentos(self):
        response = calcula_salario(1200.00)
        self.assertTupleEqual(('novo salario: 1320.00', 120.0, 10), response)

    def test_calcula_reajuste_dois_mil(self):
        response = calcula_salario(2000.00)
        self.assertTupleEqual(('novo salario: 2140.00', 140.0, 7), response)

    def test_calcula_reajuste_dois_mil_e_um(self):
        response = calcula_salario(2000.01)
        self.assertTupleEqual(('novo salario: 2080.01', 80.0, 4), response)
