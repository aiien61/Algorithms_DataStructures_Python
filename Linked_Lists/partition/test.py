import unittest
from main import Solution, SinglyLinkedList


class Test(unittest.TestCase):
    sol = Solution()

    test_case_list = SinglyLinkedList([3, 5, 8, 5, 10, 2, 1])
    x = 5
    
    def test_partition_by_append(self):
        result = self.sol.partition_by_append(self.x, self.test_case_list)
        self.assertTrue(self.sol.is_partitioned(self.x, result))

    def test_partition_by_prepend(self):
        result = self.sol.partition_by_prepend(self.x, self.test_case_list)
        self.assertTrue(self.sol.is_partitioned(self.x, result))

    def test_partition(self):
        self.sol.partition(self.x, self.test_case_list)
        self.assertTrue(self.sol.is_partitioned(self.x, self.test_case_list))
        
if __name__ == "__main__":
    unittest.main()
