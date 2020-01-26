import unittest

from calculator.core.calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def test_add(self):
        a = 1234
        b = 2345
        res = Calculator.add(a, b)
        self.assertTrue(res == a + b)
