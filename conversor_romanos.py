from unittest import TestCase

def conversor(numero):
    mensagem = 'digite um numero em inteiro e diferente de zero'
    pares = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]
    resultado = ''
    if numero == 0:
        return mensagem
    try:
        numero = int(numero)
    except ValueError:
        return mensagem

    for inteiro, romano in pares:
        resultado = resultado + (numero//inteiro)*romano
        numero = numero - (numero//inteiro)*inteiro
    return resultado


class ConversorTestCase(TestCase):

    def test_aceita_parametro(self):
        numero = conversor(20)

    def test_conversor_nao_aceita_string(self):
        numero = conversor('vinte')
        mensagem = 'digite um numero em inteiro e diferente de zero'
        self.assertEqual(numero, mensagem)

    def test_nao_converte_zero(self):
        numero = conversor(0)
        mensagem = 'digite um numero em inteiro e diferente de zero'
        self.assertEqual(numero, mensagem)

    def test_retorna_numero_um_em_romanos(self):
        numero = conversor(1)
        self.assertEqual(numero, 'I')
        
    def test_retorna_numero_um_em_romanos(self):
        numero = conversor(1)
        self.assertEqual(numero, 'I')

    def test_retorna_numero_5_em_romanos(self):
        numero = conversor(5)
        self.assertEqual(numero, 'V')

    def test_retorna_numero_10_em_romanos(self):
        numero = conversor(10)
        self.assertEqual(numero, 'X')

    def test_retorna_numero_50_em_romanos(self):
        numero = conversor(50)
        self.assertEqual(numero, 'L')

    def test_retorna_numero_100_em_romanos(self):
        numero = conversor(100)
        self.assertEqual(numero, 'C')

    def test_retorna_numero_500_em_romanos(self):
        numero = conversor(500)
        self.assertEqual(numero, 'D')

    def test_retorna_numero_1000_em_romanos(self):
        numero = conversor(1000)
        self.assertEqual(numero, 'M')

    def test_nao_retorna_numeros_repetidos(self):
        numero = conversor(11)
        self.assertEqual(numero, 'XI')

    def test_retorna_numero_em_romanos(self):
        numero = conversor(116)
        self.assertEqual(numero, 'CXVI')

    def test_retorna_numero_quatro_em_romanos(self):
        numero = conversor(4)
        self.assertEqual(numero, 'IV')

    def test_retorna_numero_nove_em_romanos(self):
        numero = conversor(9)
        self.assertEqual(numero, 'IX')

    def test_retorna_numero_quatrocentos_em_romanos(self):
        numero = conversor(400)
        self.assertEqual(numero, 'CD')

    def test_retorna_numero_novecentos_e_quarenta_e_quatro(self):
        numero = conversor(944)
        self.assertEqual(numero, 'CMXLIV')
