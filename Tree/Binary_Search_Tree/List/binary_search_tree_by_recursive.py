from dataclasses import dataclass
from icecream import ic
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
        if not self.root:
            self.root = Node(value)
            return True
        return True if self.__insert(self.root, value) else False

    def __insert(self, node: Node, value: int) -> Node:
        if node is None:
            return Node(value)
        
        if value == node.value:
            print(f"Value {value} already exists. Can't insert")
            return None

        if value < node.value:
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)
        return node
    
    def contains(self, value: int) -> bool:
        return self.__contains(self.root, value)
    
    def __contains(self, node: Node, value: int) -> bool:
        if node is None:
            return False

        if value == node.value:
            return True
        
        if value < node.value:
            return self.__contains(node.left, value)
        else:
            return self.__contains(node.right, value)

    def search(self, value: int) -> Node:
        return self.__search(self.root, value)
    
    def __search(self, node: Node, value: int) -> Node:
        if node is None:
            return None
        
        if value == node.value:
            return node
        
        if value < node.value:
            return self.__search(node.left, value)
        else:
            return self.__search(node.right, value)
        
    def delete(self, value: int) -> bool:
        if not self.contains(value):
            return False

        self.root = self.__delete(self.root, value)
        return True

    def __delete(self, node: Node, value: int) -> Node:
        if node is None:
            return None

        if value == node.value:
            match (node.left, node.right):
                case (None, None):
                    return None
                case (None, Node):
                    return node.right
                case (Node, None): 
                    return node.left
                case _:
                    sub_tree_max: int = self.get_max(node.left)
                    node.value = sub_tree_max
                    node.left = self.__delete(node.left, sub_tree_max)
                    return node

        if value < node.value:
            node.left = self.__delete(node.left, value)
        else:
            node.right = self.__delete(node.right, value)
        return node
    
    def get_min(self, node: Node) -> int:
        """Avoid using recursion, use loop instead"""
        while node.left is not None:
            node = node.left
        return node.value
    
    def get_max(self, node: Node) -> int:
        """Avoid using recursion, use loop instead"""
        while node.right is not None:
            node = node.right
        return node.value
    
    def inorder(self) -> List[int]:
        result: List[int] = []
        self.__inorder(self.root, result)
        return result
    
    def __inorder(self, node, result: List[int]):
        if node:
            self.__inorder(node.left, result)
            result.append(node.value)
            self.__inorder(node.right, result)
        


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

    def test_delete_when_found(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected_response: bool = True
        actual_response: bool = bst.delete(20)

        expected_list: List[int] = [3, 5, 7, 10, 15, 30]
        actual_list: List[int] = bst.inorder()

        self.assertEqual(expected_response, actual_response)
        self.assertEqual(expected_list, actual_list)

    def test_delete_when_not_found(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected_response: bool = False
        actual_response: bool = bst.delete(0)

        expected_list: List[int] = [3, 5, 7, 10, 15, 20, 30]
        actual_list: List[int] = bst.inorder()

        self.assertEqual(expected_response, actual_response)
        self.assertEqual(expected_list, actual_list)

    def test_get_min(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected: int = 3
        actual: int = bst.get_min(bst.root)
        self.assertEqual(expected, actual)

    def test_get_max(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected: int = 30
        actual: int = bst.get_max(bst.root)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
