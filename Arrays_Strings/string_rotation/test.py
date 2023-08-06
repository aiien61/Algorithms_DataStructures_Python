import unittest
from main import Solution


class Test(unittest.TestCase):
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False)
    ]

    def test_is_string_rotation_by_brute_force(self):
        sol = Solution()
        for s1, s2, expected in self.test_cases:
            actual = sol.is_string_rotation_by_brute_force(s1, s2)
            self.assertEqual(actual, expected)


    def test_is_string_rotation_by_pythonic(self):
        sol = Solution()
        for s1, s2, expected in self.test_cases:
            actual = sol.is_string_rotation_by_pythonic(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
