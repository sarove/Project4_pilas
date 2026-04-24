# -*- coding: utf-8 -*-
"""
Pruebas unitarias para pilas.py

Ejecución:
    python test_pilas.py
    o
    python -m unittest test_pilas.py -v
"""

import unittest
from pilas import (
    Stack, balanceado, decimal_a_binario,
    invertir_cadena, evaluar_postfija,
)


# ==============================================================
# Pruebas de la clase Stack
# ==============================================================
class TestStack(unittest.TestCase):

    def setUp(self):
        self.s = Stack()

    def test_pila_vacia(self):
        self.assertTrue(self.s.is_empty())
        self.assertEqual(self.s.size(), 0)
        self.assertIsNone(self.s.pop())
        self.assertIsNone(self.s.peek())

    def test_push_y_peek(self):
        self.s.push(10)
        self.s.push(20)
        self.assertEqual(self.s.peek(), 20)
        self.assertEqual(self.s.size(), 2)

    def test_pop_orden_lifo(self):
        for n in [1, 2, 3]:
            self.s.push(n)
        self.assertEqual(self.s.pop(), 3)
        self.assertEqual(self.s.pop(), 2)
        self.assertEqual(self.s.pop(), 1)
        self.assertTrue(self.s.is_empty())

    def test_push_tipos_mixtos(self):
        self.s.push(1)
        self.s.push("texto")
        self.s.push([1, 2])
        self.assertEqual(self.s.pop(), [1, 2])
        self.assertEqual(self.s.pop(), "texto")
        self.assertEqual(self.s.pop(), 1)


# ==============================================================
# Pruebas de balanceado()
# ==============================================================
class TestBalanceado(unittest.TestCase):

    def test_balanceado_simple(self):
        self.assertTrue(balanceado("(a+b)*[c-d]"))
        self.assertTrue(balanceado("{[()]}"))
        self.assertTrue(balanceado("(((a)))"))

    def test_no_balanceado(self):
        self.assertFalse(balanceado("(a+b*[c-d]"))
        self.assertFalse(balanceado("{[(])}"))
        self.assertFalse(balanceado(")("))
        self.assertFalse(balanceado("((("))

    def test_cadena_vacia(self):
        self.assertTrue(balanceado(""))

    def test_sin_simbolos(self):
        self.assertTrue(balanceado("abcdef"))

    def test_solo_cierre(self):
        self.assertFalse(balanceado(")"))
        self.assertFalse(balanceado("]"))


# ==============================================================
# Pruebas de decimal_a_binario()
# ==============================================================
class TestDecimalABinario(unittest.TestCase):

    def test_cero(self):
        self.assertEqual(decimal_a_binario(0), "0")

    def test_casos_conocidos(self):
        self.assertEqual(decimal_a_binario(1), "1")
        self.assertEqual(decimal_a_binario(2), "10")
        self.assertEqual(decimal_a_binario(5), "101")
        self.assertEqual(decimal_a_binario(13), "1101")
        self.assertEqual(decimal_a_binario(255), "11111111")

    def test_potencias_de_dos(self):
        self.assertEqual(decimal_a_binario(8), "1000")
        self.assertEqual(decimal_a_binario(16), "10000")
        self.assertEqual(decimal_a_binario(128), "10000000")

    def test_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            decimal_a_binario(-5)


# ==============================================================
# Pruebas de las aplicaciones adicionales
# ==============================================================
class TestInvertirCadena(unittest.TestCase):

    def test_palabra(self):
        self.assertEqual(invertir_cadena("hola"), "aloh")

    def test_vacia(self):
        self.assertEqual(invertir_cadena(""), "")

    def test_palindromo(self):
        self.assertEqual(invertir_cadena("oso"), "oso")


class TestEvaluarPostfija(unittest.TestCase):

    def test_suma_simple(self):
        self.assertEqual(evaluar_postfija("3 4 +"), 7)

    def test_compleja(self):
        # Equivale a (5 + (1+2)*4) - 3 = 14
        self.assertEqual(evaluar_postfija("5 1 2 + 4 * + 3 -"), 14)

    def test_division(self):
        self.assertEqual(evaluar_postfija("10 2 /"), 5)

    def test_mal_formada(self):
        with self.assertRaises(ValueError):
            evaluar_postfija("+ 3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
