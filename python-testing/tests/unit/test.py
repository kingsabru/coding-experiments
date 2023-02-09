from fractions import Fraction
import unittest

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from my_sum import sum


class TestSum(unittest.TestCase):

    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6, "Test must be equal to 6")

    # failing a test
    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1, "Test must be equal to 1")

    # handling expected error
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            _ = sum(data)


if __name__ == "__main__":
    unittest.main()
