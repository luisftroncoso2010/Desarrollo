# Tes unitarios con unittest
import unittest
# Importamos el modulo calcular_media
from testing_eldp import calcular_media


# Creamoa la clase test, de unittest
class TestCalcularMedia(unittest.TestCase):
    def test_1(self):
        resultado = calcular_media([10, 10, 10])
        self.assertEqual(resultado, 10)

    def test_2(self):
        resultado = calcular_media([5, 3, 4])
        # Verifica que los valores de a y b son iguales
        self.assertEqual(resultado, 4)


if __name__ == '__main__':
    unittest.main()
