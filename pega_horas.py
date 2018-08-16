from datetime import datetime
import unittest

class MostraHora:

    def __init__(self):
        self.agora = None 

    def hora_passada(self):
        if not self.agora:
            self.agora = datetime.now()
        return self.agora
    

class TestMostraHora(unittest.TestCase):
    def teste_retorna_hora(self):
        self.assertIsInstance(MostraHora().hora_passada(),
            datetime)
        hora = MostraHora()
        self.assertEqual(
            hora.hora_passada(),
            hora.hora_passada()
        )
        
