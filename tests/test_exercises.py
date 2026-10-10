import unittest

from exercises.discount import calculate_discount
from exercises.numbers import analyze_numbers, even_or_odd, find_even
from exercises.strings import count_sheep, greet, string_to_array


class TestNumberExercises(unittest.TestCase):
    def test_analyze_numbers(self):
        self.assertEqual(analyze_numbers([12, 5, 8, 21, 4, 17, 8]), (21, 4))

    def test_analyze_numbers_with_negative_values(self):
        self.assertEqual(analyze_numbers([-3, -10, 2]), (2, -10))

    def test_find_even(self):
        self.assertEqual(find_even([3, 4, 7, 10, 12, 18]), [4, 10, 12, 18])

    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(2), "Even")
        self.assertEqual(even_or_odd(7), "Odd")


class TestDiscountExercise(unittest.TestCase):
    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(1000, 20), 800.0)


class TestStringExercises(unittest.TestCase):
    def test_string_to_array(self):
        self.assertEqual(string_to_array("Robin Singh"), ["Robin", "Singh"])

    def test_count_sheep(self):
        self.assertEqual(count_sheep(3), "3 sheep...")

    def test_greet(self):
        self.assertEqual(greet("Ayesha"), "Hello, Ayesha!")


if __name__ == "__main__":
    unittest.main()

