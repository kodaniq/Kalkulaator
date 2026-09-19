import unittest

from kalkulaator import calculate


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(5, "+", 3), 8)

    def test_subtraction(self):
        self.assertEqual(calculate(5, "-", 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculate(5, "*", 3), 15)

    def test_division(self):
        self.assertEqual(calculate(6, "/", 3), 2)

    def test_power(self):
        self.assertEqual(calculate(2, "**", 3), 8)

    def test_modulo(self):
        self.assertEqual(calculate(10, "%", 3), 1)

    def test_square_root(self):
        self.assertEqual(calculate(9, "sqrt"), 3)

    def test_decimal_numbers(self):
        self.assertEqual(calculate(2.5, "+", 1.5), 4)

    def test_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "nulliga ei saa jagada"):
            calculate(5, "/", 0)

    def test_modulo_by_zero(self):
        with self.assertRaisesRegex(ValueError, "nulliga ei saa jääki arvutada"):
            calculate(5, "%", 0)

    def test_negative_square_root(self):
        with self.assertRaisesRegex(ValueError, "negatiivsest arvust"):
            calculate(-9, "sqrt")

    def test_unknown_operator(self):
        with self.assertRaisesRegex(ValueError, "sellist tehet ei ole"):
            calculate(5, "banana", 3)


if __name__ == "__main__":
    unittest.main()
