from dataclasses import dataclass
from typing import List
import unittest

@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None

class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, value: int) -> bool:
        if self.root is None:
            self.root = Node(value)
            return True
        temp: Node = self.root
        while temp is not None:
            if value == temp.value:
                return False

            if value < temp.value:
                if temp.left is None:
                    temp.left = Node(value)
                    return True
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = Node(value)
                    return True
                temp = temp.right

    def contains(self, value: int) -> bool:
        temp: Node = self.root
        while temp is not None:
            if value == temp.value:
                return True
            temp = temp.left if value < temp.value else temp.right
        return False

    def inorder(self) -> List[int]:
        result: List[int] = []
        self.__inorder(self.root, result)
        return result
    
    def __inorder(self, node: Node, container: List[int]) -> None:
        if node:
            self.__inorder(node.left, container)
            container.append(node.value)
            self.__inorder(node.right, container)
        return None
    
    def search(self, value: int) -> Node:
        temp: Node = self.root
        while temp is not None:
            if value == temp.value:
                return temp
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return None


class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(20)
        bst.insert(3)
        bst.insert(7)
        expected: List[int] = [3, 5, 7, 10, 20]
        actual: List[int] = bst.inorder()
        self.assertEqual(expected, actual)

    def test_contains_when_found(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected: bool = True
        actual: bool = bst.contains(15)
        self.assertEqual(expected, actual)

    def test_contains_when_not_found(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected: bool = False
        actual: bool = bst.contains(100)
        self.assertEqual(expected, actual)

    def test_search_when_found(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected: int = 15
        actual: int = bst.search(15).value
        self.assertEqual(expected, actual)

    def test_search_when_not_found(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected = None
        actual = bst.search(100)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
