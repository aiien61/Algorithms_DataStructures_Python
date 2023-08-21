import random
import unittest
from main import Solution, Singly_Linked_List
from toolz import pipe


class Test(unittest.TestCase):
    sol = Solution()

    test_cases = [[None, None, True],
                  [None, None, False]]
    
    data = [[[1, 2, 3, 4, 5, 6], [10, 11, 12]],
            [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]]
    
    def init_cases(self):
        for i in range(len(self.test_cases)):
            args = []
            for j in range(len(self.data[i])):
                self.test_cases[i][j] = pipe(
                    self.data[i][j],
                    self.sol.initialize_llist
                )
                if self.test_cases[i][-1]:
                    position = random.randint(0, len(self.data[i][j])-1)
                else:
                    position = -1
                args.append((self.test_cases[i][j], position))

            self.sol.generate_intersection(*args)
        return None            


    def test_intersection(self):
        self.init_cases()
        for llist_a, llist_b, expected in self.test_cases:
            actual = self.sol.intersection(llist_a, llist_b)
            if expected:
                self.assertTrue(actual)
            else:
                self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
