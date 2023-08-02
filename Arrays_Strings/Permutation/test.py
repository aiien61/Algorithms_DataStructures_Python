import unittest
from main import Solution


class Test(unittest.TestCase):

    test_cases_T = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    test_cases_F = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_is_permutation_by_count(self):
        sol = Solution()
        for str1, str2 in self.test_cases_T:
            result = sol.is_permutation_by_count(str1, str2)
            self.assertTrue(result)
        
        for str1, str2 in self.test_cases_F:
            result = sol.is_permutation_by_count(str1, str2)
            self.assertFalse(result)


    def test_is_permutation_by_sort(self):
        sol = Solution()
        for str1, str2 in self.test_cases_T:
            result = sol.is_permutation_by_sort(str1, str2)
            self.assertTrue(result)

        for str1, str2 in self.test_cases_F:
            result = sol.is_permutation_by_sort(str1, str2)
            self.assertFalse(result)


    def test_is_permutation_by_pythonic(self):
        sol = Solution()
        for str1, str2 in self.test_cases_T:
            result = sol.is_permutation_by_pythonic(str1, str2)
            self.assertTrue(result)

        for str1, str2 in self.test_cases_F:
            result = sol.is_permutation_by_pythonic(str1, str2)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
