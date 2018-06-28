
import unittest
from classe_bola import Bola

class VerificaClasseBolaTests(unittest.TestCase):

    def setUp(self):
        self.bola = Bola('azul', 20, 'plastico')

    def test_atributo_cor(self):
        self.bola.cor

        self.assertEqual(self.bola.cor, 'azul')

    def test_atributo_circunferencia(self):
        self.bola.circunferencia

        self.assertEqual(self.bola.circunferencia, 20)

    def test_atributo_material(self):
        self.bola.material

        self.assertEqual(self.bola.material, 'plastico')

    def test_metodo_troca_cor(self):
        self.bola.trocacor('roxo')
        self.assertEqual(self.bola.cor, 'roxo')
