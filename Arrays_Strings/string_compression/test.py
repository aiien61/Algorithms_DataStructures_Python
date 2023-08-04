import unittest
from main import Solution


class Test(unittest.TestCase):

    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef")
    ]


    def test_compress_string_by_brute_force(self):
        sol = Solution()
        for text, expected in self.test_cases:
            actual = sol.compress_string_by_brute_force(text)
            self.assertEqual(actual, expected)

    
    def test_compress_string(self):
        sol = Solution()
        for text, expected in self.test_cases:
            actual = sol.compress_string(text)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
