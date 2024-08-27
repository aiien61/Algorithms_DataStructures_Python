import random
import unittest
from dataclasses import dataclass

@dataclass
class TreeNode:
    value: int
    right: 'TreeNode' = None
    left: 'TreeNode' = None


class BSTreeList:
    def __init__(self):
        self.root: 'TreeNode' = None

    def insert(self, value: int) -> bool:
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node

        temp: 'TreeNode' = self.root
        while True:
            if temp.value == value:
                return False
            
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
        return False
    
    def contains(self, value: int) -> bool:
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

class Test(unittest.TestCase):
    def test_insertion_when_only_root(self):
        bst = BSTreeList()
        bst.insert(10)

        expected: int = 10
        actual: int = bst.root.value
        self.assertEqual(expected, actual)

    def test_insertion_when_only_left_child(self):
        bst = BSTreeList()
        bst.insert(10)
        bst.insert(5)

        expected: int = 5
        actual: int = bst.root.left.value
        self.assertEqual(expected, actual)

    def test_insertion_when_only_right_child(self):
        bst = BSTreeList()
        bst.insert(10)
        bst.insert(15)

        expected: int = 15
        actual: int = bst.root.right.value
        self.assertEqual(expected, actual)

    def test_insertion_when_duplicate(self):
        bst = BSTreeList()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        expected: bool = False
        actual: bool = bst.insert(15)
        self.assertEqual(expected, actual)

    def test_contain_when_empty_tree(self):
        bst = BSTreeList()

        expected: bool = False
        actual: bool = bst.contains(10)
        self.assertEqual(expected, actual)

    def test_contain_when_only_root(self):
        bst = BSTreeList()
        bst.insert(10)

        expected: bool = True
        actual: bool = bst.contains(10)
        self.assertEqual(expected, actual)

    def test_contain_when_existing_left_child(self):
        bst = BSTreeList()
        bst.insert(10)
        bst.insert(5)

        expected: bool = True
        actual: bool = bst.contains(5)
        self.assertEqual(expected, actual)

    def test_contain_when_existing_right_child(self):
        bst = BSTreeList()
        bst.insert(10)
        bst.insert(15)

        expected: bool = True
        actual: bool = bst.contains(15)
        self.assertEqual(expected, actual)

    def test_contain_when_non_existing_element(self):
        bst = BSTreeList()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        expected: bool = False
        actual: bool = bst.contains(25)
        self.assertEqual(expected, actual)

    def test_contain_when_large_input(self):
        random.seed(100)

        bst = BSTreeList()
        for _ in range(500):
            bst.insert(random.randint(1, 1000))
        bst.insert(500)
        for _ in range(500):
            bst.insert(random.randint(1, 1000))

        expected: bool = True
        actual: bool = bst.contains(500)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
