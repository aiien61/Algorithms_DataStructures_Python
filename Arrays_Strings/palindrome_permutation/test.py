import unittest
from main import Solution
class Test(unittest.TestCase):
    
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True)
    ]


    def test_is_palindrome_permutation_by_hash(self):
        sol = Solution()
        for text, expected in self.test_cases:
            actual = sol.is_palindrome_permutation_by_hash(text)
            self.assertEqual(actual, expected)

    def test_is_palindrome_permutation_by_pythonic(self):
        sol = Solution()
        for text, expected in self.test_cases:
            actual = sol.is_palindrome_permutationi_by_pythonic(text)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
