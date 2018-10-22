# fonte https://www.urionlinejudge.com.br/judge/pt/problems/view/1045
from unittest import TestCase

class TiposTriangulos:

    def __init__(self, ladoA, ladoB, ladoC):
        self.lados = [ladoA, ladoB, ladoC]
        self._ordena_variaveis()
        self.ladoA = self.lados[0]
        self.ladoB = self.lados[1]
        self.ladoC = self.lados[2]

    def nomeia_triangulos(self):
        if self.ladoA >= self.ladoB + self.ladoC:
            mensagem = 'Nao forma triangulo'
        elif self.ladoA**2 == self.ladoB**2 + self.ladoC**2:
            mensagem = 'triangulo retangulo'
        elif self.ladoA**2 > self.ladoB**2 + self.ladoC**2:
            mensagem = 'triangulo obtusangulo'
        elif self.ladoA**2 < self.ladoB**2 + self.ladoC**2:
            mensagem = 'triangulo acutangulo'
        pertinencia = self._pertinencia_de_medidas()
        return '{} / {}'.format(mensagem, pertinencia)

    def _pertinencia_de_medidas(self):
        tipo = None
        if self.ladoA == self.ladoB == self.ladoC:
            tipo = 'triangulo equilatero'
        elif self.ladoA == self.ladoB or self.ladoB == self.ladoC or self.ladoA == self.ladoC:
            tipo = 'triangulo isosceles'
        return tipo

    def _ordena_variaveis(self):
        terminado = False
        while not terminado:
            terminado = True
            for i in range(len(self.lados) - 1):
                if self.lados[i] < self.lados[i + 1]:
                    self.lados[i], self.lados[i + 1] = self.lados[i + 1], self.lados[i]
                    terminado = False
        return self.lados

class TiposTriangulosTestCase(TestCase):

    def test_pode_instanciar(self):
        triangulo = TiposTriangulos(2.0, 4.0, 9.0)
        self.assertIsInstance(triangulo, TiposTriangulos)

    def test_ordena_decrescente_variaveis(self):
        triangulo = TiposTriangulos(2.0, 4.0, 9.0)
        response = triangulo.lados
        self.assertEqual(response, [9.0, 4.0, 2.0]) 

    def test_triangulo_equilatero(self):
        triangulo = TiposTriangulos(2.0, 2.0, 2.0)
        response = triangulo._pertinencia_de_medidas()
        self.assertEqual(response, 'triangulo equilatero')

    def test_triangulo_isosceles(self):
        triangulo = TiposTriangulos(2.0, 2.0, 4.0)
        response = triangulo._pertinencia_de_medidas()
        self.assertEqual(response, 'triangulo isosceles')

    def test_nao_forma_triangulo(self):
        triangulo = TiposTriangulos(5.0, 7.0, 2.0)
        response = triangulo.nomeia_triangulos()
        self.assertIn('Nao forma triangulo', response)

    def test_nomeia_triangulo_retangulo(self):
        triangulo = TiposTriangulos(6.0, 8.0, 10.0)
        response = triangulo.nomeia_triangulos()
        self.assertIn('triangulo retangulo', response)

    def test_nomeia_triangulo_obtusangulo(self):
        triangulo = TiposTriangulos(6.0, 6.0, 10.0)
        response = triangulo.nomeia_triangulos()
        self.assertIn('triangulo obtusangulo', response)

    def test_nomeia_triangulo_acutangulo(self):
        triangulo = TiposTriangulos(7.0, 5.0, 7.0)
        response = triangulo.nomeia_triangulos()
        self.assertIn('triangulo acutangulo', response)

    def test_nomeia_triangulo_acutangulo_e_isoceles(self):
        triangulo = TiposTriangulos(7.0, 5.0, 7.0)
        response = triangulo.nomeia_triangulos()
        self.assertEqual(response, 'triangulo acutangulo / triangulo isosceles')

    def test_nomeia_triangulo_obtusangulo_e_isoceles(self):
        triangulo = TiposTriangulos(6.0, 6.0, 10.0)
        response = triangulo.nomeia_triangulos()
        self.assertEqual(response, 'triangulo obtusangulo / triangulo isosceles')
