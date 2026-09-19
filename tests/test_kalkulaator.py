import subprocess
import sys
import unittest


def run_calculator(user_input):
    result = subprocess.run(
        [sys.executable, "kalkulaator.py"],
        input=user_input,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        output = run_calculator("5\n+\n3\nq\n")
        self.assertIn("Vastus: 8.0", output)

    def test_subtraction(self):
        output = run_calculator("5\n-\n3\nq\n")
        self.assertIn("Vastus: 2.0", output)

    def test_multiplication(self):
        output = run_calculator("5\n*\n3\nq\n")
        self.assertIn("Vastus: 15.0", output)

    def test_division(self):
        output = run_calculator("6\n/\n3\nq\n")
        self.assertIn("Vastus: 2.0", output)

    def test_power(self):
        output = run_calculator("2\n**\n3\nq\n")
        self.assertIn("Vastus: 8.0", output)

    def test_modulo(self):
        output = run_calculator("10\n%\n3\nq\n")
        self.assertIn("Vastus: 1.0", output)

    def test_square_root(self):
        output = run_calculator("9\nsqrt\nq\n")
        self.assertIn("Vastus: 3.0", output)

    def test_division_by_zero(self):
        output = run_calculator("5\n/\n0\nq\n")
        self.assertIn("Error: nulliga ei saa jagada.", output)

    def test_negative_square_root(self):
        output = run_calculator("-9\nsqrt\nq\n")
        self.assertIn("Error: negatiivsest arvust ei saa ruutjuurt võtta.", output)

    def test_invalid_number(self):
        output = run_calculator("tere\nq\n")
        self.assertIn("Error: palun sisesta arv.", output)


if __name__ == "__main__":
    unittest.main()
