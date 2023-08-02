import unittest
from main import Solution

class Test(unittest.TestCase):

    test_cases = [
        ("Mr John Smith        ", 13, "Mr%20John%20Smith"),
        ('Mr John Smith', 13, "Mr%20John%20Smith")
    ]

    def test_urlify_by_array(self):
        sol = Solution()
        for chars, true_length, expected in self.test_cases:
            actual = sol.urlify_by_array(chars, true_length)
            self.assertEqual(actual, expected)

    def test_urlify_by_pythonic(self):
        sol = Solution()
        for chars, true_length, expected in self.test_cases:
            actual = sol.urlify_by_pythonic(chars, true_length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
