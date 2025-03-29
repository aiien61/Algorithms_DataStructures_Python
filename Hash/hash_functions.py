"""Implements some commonly used hash functions"""

import unittest

# Division method
def hash_division(input_value: int) -> int:
    modulo_number: int = 1_000_000_007
    return input_value % modulo_number

# Multiplication method
def hash_multiplication(input_value: int) -> int:
    range_limit: int = 1_000_000_007
    random_number: float = 0.618033  # 近似於黃金比例
    fraction: int = (input_value * random_number) % 1
    return int(fraction * range_limit)

# Mid-Square method
def hash_midsquare(input_value: int) -> int:
    input_value_squared: int = input_value * input_value
    hashed_output: int = (input_value_squared % 1_000_000) // 1_000
    return hashed_output

# Hash string
def hash_string(s: str) -> int:
    magic_number: int = 31
    modulo_number: int = 1_000_000_007
    hashed_value: int = 0

    for char in s:
        hashed_value *= magic_number
        hashed_value = mod(hashed_value, modulo_number)
        hashed_value += ord(char)
        hashed_value = mod(hashed_value, modulo_number)
    
    return hashed_value

def mod(num: int, mod: int) -> int:
    return (num % mod + mod) % mod


class TestHashFunctions(unittest.TestCase):
    def setUp(self):
        self.input_value: int = 123_456_789_0

    def test_hash_division(self):
        actual: int = hash_division(29)
        expected: int = 29
        self.assertEqual(actual, expected)

        actual: int = hash_division(self.input_value)
        expected: int = 234_567_883
        self.assertEqual(actual, expected)

    
    def test_hash_multiplication(self):
        actual: int = hash_multiplication(self.input_value)
        expected: int = 760_370_021
        self.assertEqual(actual, expected)

    def test_hash_midsquare(self):
        actual: int = hash_midsquare(self.input_value)
        expected: int = 52
        self.assertEqual(actual, expected)

    def test_hash_string(self):
        actual: int = hash_string("mygod")
        expected: int = 104_371_024
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
