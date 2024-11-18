import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add(self):
        self.assertEqual(self.calc.add(-2, 1),-1 )

    def test_substract(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)
    def test_substract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-2, 1), -2)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-2, -1), 2)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, -2), -5)
    def test_devide(self):
        self.assertEqual(self.calc.divide(0, -1), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(0, 3), 0)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(0, -3), 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()