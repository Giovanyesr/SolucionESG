import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado


class TestEcuacionSegundoGrado(unittest.TestCase):
    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

    def tearDown(self):
        self.calculoRaices = None

    def test_calculoESG_diccionariodosNumeros_retornaSolucion(self):
        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperada1": 1.43, "RaizEsperada2": 0.23},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperada1": -1.00, "RaizEsperada2": -1.00},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperada1": 1.0, "RaizEsperada2": 1.00},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperada1": 4.2, "RaizEsperada2": -4.24},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperada1": 0.0, "RaizEsperada2": -4.00},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperada1": -2.0, "RaizEsperada2": -2.00},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperada1": -1.0, "RaizEsperada2": -2.00},
        )

        for item in items:
            with self.subTest(item["Case"]):
                resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.calculoESG(item["a"], item["b"], item["c"])
                self.assertAlmostEqual(item["RaizEsperada1"], resultadoActualRaiz1, delta=0.05)
                self.assertAlmostEqual(item["RaizEsperada2"], resultadoActualRaiz2, delta=0.05)

if __name__ == "__main__":
    unittest.main()

