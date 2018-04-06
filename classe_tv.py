import unittest

class TV:

    def __init__(self, volume=0):
        self.volume = volume

    def muda_canal(self, canal):
        self.canal = max(min(canal, 80), 1)
        print(self.canal)

    def abaixa_volume(self):
        self._seta_volume(-1)
        return self

    def aumenta_volume(self):
        self._seta_volume(+1)
        return self
        
    def _seta_volume(self, volume):
        self.volume = max(0, self.volume + volume)

    def imprime_volume(self):
        print(self.volume)

class TestTV(unittest.TestCase):
    def setUp(self):
        self.tv = TV()

    def test_aumenta_volume_uma_vez(self):
        self.tv.aumenta_volume()
        self.assertEqual(self.tv.volume, 1)

    def test_volume_nunca_diminui_para_menos_de_zero(self):
        self.tv.aumenta_volume()
        self.tv.abaixa_volume()
        self.tv.abaixa_volume()
        self.assertEqual(self.tv.volume, 0)

if __name__ == '__main__':
    unittest.main()
