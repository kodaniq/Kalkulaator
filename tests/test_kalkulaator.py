import math
import unittest

from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from kalkulaator import calculate, clear_screen, command_suggestion, handle_command, parse_expression, show_help, show_history, undo


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

    def test_decimal_comma(self):
        self.assertEqual(parse_expression("2,5 + 1,5", None), 4)

    def test_decimal_comma_in_function(self):
        self.assertAlmostEqual(parse_expression("sin(30,5)", None), math.sin(math.radians(30.5)))

    def test_decimal_comma_with_implicit_multiplication(self):
        self.assertAlmostEqual(parse_expression("2,5pi", None), 2.5 * math.pi)

    def test_multiplication_symbol(self):
        self.assertEqual(parse_expression("5 × 3", None), 15)

    def test_division_symbol(self):
        self.assertEqual(parse_expression("10 ÷ 2", None), 5)

    def test_original_multiplication_and_division_still_work(self):
        self.assertEqual(parse_expression("5 * 3 + 10 / 2", None), 20)

    def test_unicode_symbols_in_expression(self):
        self.assertEqual(parse_expression("2 × (3 + 4) ÷ 2", None), 7)

    def test_caret_power(self):
        self.assertEqual(parse_expression("2 ^ 10", None), 1024)

    def test_postfix_percentage(self):
        self.assertEqual(parse_expression("200 * 15%", None), 30)

    def test_add_percentage_relative_to_base(self):
        self.assertEqual(parse_expression("200 + 15%", None), 230)

    def test_subtract_percentage_relative_to_base(self):
        self.assertEqual(parse_expression("200 - 15%", None), 170)

    def test_decimal_relative_percentage(self):
        self.assertEqual(parse_expression("200 + 12,5%", None), 225)

    def test_ans_relative_percentage(self):
        self.assertEqual(parse_expression("ans + 25%", 80), 100)

    def test_percentage_of_ans(self):
        self.assertEqual(parse_expression("ans * 25%", 80), 20)

    def test_modulo_still_works(self):
        self.assertEqual(parse_expression("10 % 3", None), 1)

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

    def test_implicit_multiplication_with_constant(self):
        self.assertAlmostEqual(parse_expression("2pi", None), 2 * math.pi)

    def test_implicit_multiplication_with_parentheses(self):
        self.assertEqual(parse_expression("2(3 + 4)", None), 14)

    def test_implicit_multiplication_with_function(self):
        self.assertEqual(parse_expression("3sqrt(9)", None), 9)

    def test_implicit_multiplication_between_parentheses(self):
        self.assertEqual(parse_expression("(2 + 3)(4 + 5)", None), 45)

    def test_implicit_multiplication_after_parentheses(self):
        self.assertAlmostEqual(parse_expression("(1 + 1)pi", None), 2 * math.pi)

    def test_implicit_multiplication_with_ans(self):
        self.assertEqual(parse_expression("2ans", 7), 14)

    def test_unknown_name_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "tundmatu nimi"):
            parse_expression("banana + 1", None)

    def test_constant_typo_suggests_pi(self):
        with self.assertRaisesRegex(ValueError, r"tundmatu nimi 'pii'.*Kas mõtlesid 'pi'"):
            parse_expression("pii * 2", None)

    def test_function_typo_suggests_sqrt(self):
        with self.assertRaisesRegex(ValueError, r"tundmatu funktsioon 'sqr'.*Kas mõtlesid 'sqrt'"):
            parse_expression("sqr(9)", None)

    def test_unrelated_name_has_no_suggestion(self):
        with self.assertRaisesRegex(ValueError, r"^tundmatu nimi 'banana'\.$"):
            parse_expression("banana + 1", None)

    def test_wrong_function_argument_count(self):
        with self.assertRaisesRegex(ValueError, "vajab täpselt ühte argumenti"):
            parse_expression("sqrt(9, 16)", None)

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

    def test_missing_closing_parenthesis_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, r"sulgev \) on puudu"):
            parse_expression("(5 + 3", None)

    def test_missing_function_parenthesis_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, r"sulgev \) on puudu"):
            parse_expression("sqrt(", None)

    def test_extra_closing_parenthesis_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, r"üleliigne \)"):
            parse_expression("5 + 3)", None)

    def test_double_operator_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, r"ootamatu \* pärast \+"):
            parse_expression("5 + * 3", None)

    def test_generic_syntax_error_shows_position(self):
        with self.assertRaisesRegex(ValueError, r"positsiooni \d+ juures"):
            parse_expression("5 +", None)


class CommandTests(unittest.TestCase):
    def test_history_typo_suggestion(self):
        self.assertEqual(command_suggestion("histroy"), "history")

    def test_undo_typo_suggestion(self):
        self.assertEqual(command_suggestion("udno"), "undo")

    def test_clear_history_typo_suggestion(self):
        self.assertEqual(command_suggestion("cler history"), "clear history")

    def test_normal_expression_has_no_command_suggestion(self):
        self.assertIsNone(command_suggestion("5 + 3"))

    def test_unrelated_word_has_no_command_suggestion(self):
        self.assertIsNone(command_suggestion("banana"))

    @patch("kalkulaator.os.system")
    def test_clear_screen_uses_platform_command(self, mock_system):
        clear_screen()
        expected = "cls" if __import__("os").name == "nt" else "clear"
        mock_system.assert_called_once_with(expected)

    @patch("kalkulaator.clear_screen")
    def test_clear_does_not_delete_history(self, mock_clear_screen):
        history = [("2 + 2", 4)]
        handle_command("clear", history)
        self.assertEqual(history, [("2 + 2", 4)])
        mock_clear_screen.assert_called_once()

    def test_clear_history_deletes_history(self):
        history = [("2 + 2", 4)]
        handle_command("clear history", history)
        self.assertEqual(history, [])

    def test_undo_removes_last_calculation_and_restores_ans(self):
        history = [("10 + 5", 15), ("20 * 3", 60)]
        self.assertEqual(undo(history), 15)
        self.assertEqual(history, [("10 + 5", 15)])

    def test_undo_last_calculation_clears_ans(self):
        history = [("10 + 5", 15)]
        self.assertIsNone(undo(history))
        self.assertEqual(history, [])

    def test_undo_empty_history(self):
        history = []
        self.assertIsNone(undo(history))
        self.assertEqual(history, [])

    def test_history_formats_structured_entries(self):
        history = [("5 + 3", 8), ("10 / 4", 2.5)]
        output = StringIO()
        with redirect_stdout(output):
            show_history(history)
        self.assertIn("1. 5 + 3 = 8", output.getvalue())
        self.assertIn("2. 10 / 4 = 2.5", output.getvalue())


class HelpTests(unittest.TestCase):
    def get_help_output(self, topic=None):
        output = StringIO()
        with redirect_stdout(output):
            show_help(topic)
        return output.getvalue()

    def test_specific_function_help(self):
        output = self.get_help_output("sqrt")
        self.assertIn("sqrt(x)", output)
        self.assertIn("sqrt(144)", output)

    def test_percentage_help(self):
        output = self.get_help_output("%")
        self.assertIn("200 * 15%", output)
        self.assertIn("10 % 3", output)

    def test_ans_help(self):
        output = self.get_help_output("ans")
        self.assertIn("eelmise arvutuse tulemus", output)

    def test_help_typo_suggestion(self):
        output = self.get_help_output("sqr")
        self.assertIn("Kas mõtlesid 'sqrt'?", output)

    def test_unknown_help_topic_without_bad_suggestion(self):
        output = self.get_help_output("banana")
        self.assertIn("Tundmatu abiteema 'banana'.", output)
        self.assertNotIn("Kas mõtlesid", output)


if __name__ == "__main__":
    unittest.main()
