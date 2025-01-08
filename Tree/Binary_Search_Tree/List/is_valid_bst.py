from dataclasses import dataclass
from numbers import Number
import unittest


@dataclass
class Node:
    value: Number
    left: 'Node' = None
    right: 'Node' = None

class Solution:
    def is_valid_bst(self, root: Node) -> bool:
        if not root:
            return True
        return self.__is_valid_bst(root)
    
    def __is_valid_bst(self, node: Node) -> bool:
        if not node:
            return True
        
        if node.left:
            max_left: Node = self.__get_max(node.left)
            if node.value <= max_left.value:
                return False
        
        if node.right:
            min_right: Node = self.__get_min(node.right)
            if node.value >= min_right.value:
                return False

        return self.__is_valid_bst(node.left) and self.__is_valid_bst(node.right)
    
    def __get_max(self, node: Node) -> Node:
        temp = node
        while temp.right:
            temp = temp.right
        return temp
    
    def __get_min(self, node: Node) -> Node:
        temp = node
        while temp.left:
            temp = temp.left
        return temp


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_bst_when_simple_tree(self):
        root = Node(2)
        root.left = Node(1)
        root.right = Node(3)
        actual: bool = self.solution.is_valid_bst(root)
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_invalid_bst(self):
        root = Node(5)
        root.left = Node(1)
        root.right = Node(4)
        root.left.left = Node(3)
        root.right.right = Node(6)
        actual: bool = self.solution.is_valid_bst(root)
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_empty_bst(self):
        root = None
        actual: bool = self.solution.is_valid_bst(root)
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_valid_bst_when_single_node(self):
        root = Node(1)
        actual: bool = self.solution.is_valid_bst(root)
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_valid_bst_when_complex_tree(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.right.left = Node(11)
        root.right.right = Node(20)
        actual: bool = self.solution.is_valid_bst(root)
        expected: bool = True
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
