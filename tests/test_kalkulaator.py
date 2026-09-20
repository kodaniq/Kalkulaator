import math
import unittest

from kalkulaator import calculate, parse_expression


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

    def test_absolute_value(self):
        self.assertEqual(calculate(-12, "abs"), 12)

    def test_sine_uses_degrees(self):
        self.assertAlmostEqual(calculate(90, "sin"), 1.0)

    def test_cosine_uses_degrees(self):
        self.assertAlmostEqual(calculate(180, "cos"), -1.0)

    def test_tangent_uses_degrees(self):
        self.assertAlmostEqual(calculate(45, "tan"), 1.0)

    def test_base_10_logarithm(self):
        self.assertEqual(calculate(100, "log"), 2.0)

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

    def test_invalid_logarithm(self):
        with self.assertRaisesRegex(ValueError, "ainult positiivsest"):
            calculate(0, "log")

    def test_unknown_operator(self):
        with self.assertRaisesRegex(ValueError, "sellist tehet ei ole"):
            calculate(5, "banana", 3)


class ExpressionParserTests(unittest.TestCase):
    def test_operator_precedence(self):
        self.assertEqual(parse_expression("2 + 3 * 4", None), 14)

    def test_parentheses(self):
        self.assertEqual(parse_expression("(2 + 3) * 4", None), 20)

    def test_ans(self):
        self.assertEqual(parse_expression("ans / 2 + 7", 12), 13)

    def test_ans_without_previous_result(self):
        with self.assertRaisesRegex(ValueError, "eelmist vastust"):
            parse_expression("ans + 1", None)

    def test_function_with_parentheses(self):
        self.assertEqual(parse_expression("sqrt(144)", None), 12)

    def test_function_without_parentheses(self):
        self.assertEqual(parse_expression("sqrt 144", None), 12)

    def test_pi_constant(self):
        self.assertAlmostEqual(parse_expression("pi", None), math.pi)

    def test_e_constant(self):
        self.assertAlmostEqual(parse_expression("e", None), math.e)

    def test_constants_inside_expression(self):
        self.assertAlmostEqual(parse_expression("2 * pi + e", None), 2 * math.pi + math.e)

    def test_unknown_name_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "tundmatu nimi"):
            parse_expression("banana + 1", None)

    def test_attribute_access_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "mittetoetatud süntaksit"):
            parse_expression("(1).__class__", None)

    def test_import_call_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_expression("__import__('os')", None)

    def test_list_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "mittetoetatud süntaksit"):
            parse_expression("[1, 2, 3]", None)

    def test_division_by_zero_in_expression(self):
        with self.assertRaisesRegex(ValueError, "nulliga"):
            parse_expression("10 / (5 - 5)", None)


if __name__ == "__main__":
    unittest.main()
