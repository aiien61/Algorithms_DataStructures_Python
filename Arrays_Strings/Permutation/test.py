import unittest
from main import Solution


class Test(unittest.TestCase):
    test_cases = (
        ("dog", "  god", True),
        ('abcd', 'bacd', True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", True),
        ("dog ", "dog", False),
        ("aaab", "bbba", False)
    )

    def test_is_permutation_by_count(self):
        sol = Solution()
        for word1, word2, expected in self.test_cases:
            actual = sol.is_permutation_by_count(word1, word2)
            self.assertEqual(actual, expected)

    def test_is_permutation_by_sort(self):
        sol = Solution()
        for word1, word2, expected in self.test_cases:
            actual = sol.is_permutation_by_sort(word1, word2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
