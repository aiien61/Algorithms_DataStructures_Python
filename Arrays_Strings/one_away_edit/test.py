import unittest
from main import Solution


class Test(unittest.TestCase):

    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insertion
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replacement
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replacement
        ("pale", "bake", False),
        # insertion and replacement
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insertion shouldn't match
        ("ale", "elas", False),
    ]
    
    def test_is_one_away_edit(self):
        sol = Solution()
        for str1, str2, expected in self.test_cases:
            actual = sol.is_one_away_edit(str1, str2)
            self.assertEqual(actual, expected)
