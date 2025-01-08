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
        self.root = None
    
    def insert(self, value: int) -> bool:
        if not self.root:
            self.root = Node(value)
            return True
        
        return self.__insert_helper(self.root, value)
    
    def __insert_helper(self, node: Node, value: int) -> bool:
        if value == node.value:
            return False
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
                return True
            return self.__insert_helper(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
                return True
            return self.__insert_helper(node.right, value)
        
    def contains(self, value: int) -> bool:
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
        
    def delete(self, value: int) -> bool:
        if not self.contains(value):
            return False

        self.root = self.__delete_helper(self.root, value)
        return True

    def __delete_helper(self, node: Node, value: int) -> Node:
        if not node:
            return None

        if value == node.value:
            match (node.left, node.right):
                case (None, None): return None
                case (None, Node): return node.right
                case (Node, None): return node.left
                case _:
                    sub_tree_max: int = self.get_max(node.left).value
                    node.value = sub_tree_max
                    node.left = self.__delete_helper(node.left, sub_tree_max)
                    return node
        elif value < node.value:
            node.left = self.__delete_helper(node.left, value)
        else:
            node.right = self.__delete_helper(node.right, value)
        return node
            
    def get_max(self, node: Node) -> Node:
        temp = node
        while temp.right:
            temp = temp.right
        return temp
    
    def get_min(self, node: Node) -> Node:
        temp = node
        while temp.left:
            temp = temp.left
        return temp
    
    def inorder(self) -> List[int]:
        result: List[int] = []
        self.__inorder_helper(self.root, result)
        return result
    
    def __inorder_helper(self, node: Node, container: List[int]) -> None:
        if node:
            self.__inorder_helper(node.left, container)
            container.append(node.value)
            self.__inorder_helper(node.right, container)

    
def inorder(bst: BinarySearchTree) -> List[int]:
    result: List[int] = []
    while bst.root:
        min_value = bst.get_min(bst.root).value
        result.append(min_value)
        bst.delete(min_value)
    return result
    

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

    def test_get_max(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected: int = 30
        actual: int = bst.get_max(bst.root).value
        self.assertEqual(expected, actual)

    def test_get_min(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected: int = 3
        actual: int = bst.get_min(bst.root).value
        self.assertEqual(expected, actual)

    def test_inorder(self):
        bst = BinarySearchTree()
        for value in [10, 5, 20, 3, 7, 15, 30]:
            bst.insert(value)

        expected: List[int] = bst.inorder()
        actual: List[int] = inorder(bst)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
