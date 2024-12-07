# test_modulo_sequencia.py

import unittest
from modulo_sequencia import sequencia_dos_anciaos

class TestSequenciaDosAnciaos(unittest.TestCase):
    def test_caso_1(self):
        self.assertEqual(sequencia_dos_anciaos(5, 2, 3), 13)

    def test_caso_2(self):
        self.assertEqual(sequencia_dos_anciaos(6, 1, 1), 8)

    def test_caso_3(self):
        self.assertEqual(sequencia_dos_anciaos(3, 5, 7), 12)

    def test_caso_4(self):
        self.assertEqual(sequencia_dos_anciaos(1, 10, 20), 10)

    def test_caso_5(self):
        self.assertEqual(sequencia_dos_anciaos(2, 10, 20), 20)

    def test_caso_6(self):
        self.assertEqual(sequencia_dos_anciaos(7, 3, 4), 47)

    def test_caso_7(self):
        self.assertEqual(sequencia_dos_anciaos(10, 2, 2), 110)

if __name__ == "__main__":
    unittest.main()
