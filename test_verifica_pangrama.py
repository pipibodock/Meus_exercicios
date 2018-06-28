import unittest
from verificar_pangrama import verifica_pangrama

class VerificaPangramaTests(unittest.TestCase):

    def teste_metodo_de_teste(self):
        frase = "Zebras caolhas de Java querem mandar fax para moça gigante de New York"
        frase_eh_pangrama = verifica_pangrama(frase)

        self.assertTrue(frase_eh_pangrama)

    def teste_metodo_que_nao_eh_pangrama(self):
        frase = "Alguma coisa aqui"
        frase_eh_pangrama = verifica_pangrama(frase)

        self.assertFalse(frase_eh_pangrama)
