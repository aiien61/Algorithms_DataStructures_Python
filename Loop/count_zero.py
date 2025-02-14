"""Given an integer n, find how many consecutive zeros in the digits of n
e.g. n = 903, return 1
e.g. n = 9000608, return 3
e.g. n = 91, return 0
"""
import unittest

def count_zero(n: int):
    divisor: int = 10
    count: int = 0
    max_count: int = 0
    while True:
        n, remainder = divmod(n, divisor)
        if remainder == 0:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0

        if n == 0:
            break

    return max_count


class TestCountZero(unittest.TestCase):
    def test_no_zeros(self):
        actual: int = count_zero(91)
        expected: int = 0
        self.assertEqual(actual, expected)

    def test_single_zero(self):
        actual: int = count_zero(903)
        expected: int = 1
        self.assertEqual(actual, expected)

    def test_multiple_consecutive_zeros(self):
        actual: int = count_zero(9000608)
        expected: int = 3
        self.assertEqual(actual, expected)

    def test_trailing_zeros(self):
        actual: int = count_zero(10000)
        expected: int = 4
        self.assertEqual(actual, expected)

    def test_leading_zeros(self):
        actual: int = count_zero(0)
        expected: int = 1
        self.assertEqual(actual, expected)

    def test_all_zeros(self):
        actual: int = count_zero(0000)
        expected: int = 1
        self.assertEqual(actual, expected)

    def test_large_number(self):
        actual: int = count_zero(908007006000)
        expected: int = 3
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()