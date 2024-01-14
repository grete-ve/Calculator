import unittest
from models import Calculator # from models.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 2)
        self.assertEqual(result, 4)

    def test_substract(self):
        result = self.calculator.substract(2, 2)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calculator.divide(4, 2)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(4, 0)
    

if __name__ == '__main__':
    unittest.main()
