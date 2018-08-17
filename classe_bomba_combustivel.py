import unittest

class BombaCombustivel:

    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        self.quantidade_combustivel = self.quantidade_combustivel - litros
        return litros

    def abastecer_por_litro(self, litros):
        valor = litros * self.valor_litro
        self.quantidade_combustivel = self.quantidade_combustivel - litros
        return valor

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        return self.valor_litro

    def alterar_combustivel(self, combustivel):
        self.tipo_combustivel = combustivel
        return self.tipo_combustivel

    def alterar_quantidade_combustivel(self, quantidade):
        self.quantidade_combustivel = quantidade
        return self.quantidade_combustivel


class Verifica_classe_bomba_combustivel(unittest.TestCase):

    def setUp(self):
        self.bomba = BombaCombustivel('gasolina', 3, 100)

    def test_abastece_por_valor(self):
        litros = self.bomba.abastecer_por_valor(12)

        self.assertEqual(litros, 4)
        self.assertEqual(self.bomba.quantidade_combustivel, 96)

    def test_abastece_por_litro(self):
        valor = self.bomba.abastecer_por_litro(10)

        self.assertEqual(valor, 30)
        self.assertEqual(self.bomba.quantidade_combustivel, 90)

    def test_altera_valor_do_combustivel(self):
        self.bomba.alterar_valor(5)

        self.assertEqual(self.bomba.valor_litro, 5)

    def test_alterar_combustivel(self):
        self.bomba.alterar_combustivel('alcool')

        self.assertEqual(self.bomba.tipo_combustivel, 'alcool')

    def test_alterar_quantidade_combustivel(self):
        self.bomba.alterar_quantidade_combustivel(200)

        self.assertEqual(self.bomba.quantidade_combustivel, 200)
