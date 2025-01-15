from dataclasses import dataclass
from typing import List
from icecream import ic
import unittest

@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, value: int) -> None:
        self.root = self._insert(self.root, value)
        return None
    
    def _insert(self, node: Node, value: int) -> Node:
        if node is None:
            return Node(value)

        if value == node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                new_left_node = Node(value)
                new_left_node.left = node.left
                node.left = new_left_node

        elif value < node.value:
            node.left = self._insert(node.left, value)
        
        else:
            node.right = self._insert(node.right, value)

        return node
        
    def _traverse_inorder_dfs_left(self, node: Node, container: List[int]) -> None:
        if node is None:
            return None
        self._traverse_inorder_dfs_left(node.left, container)
        container.append(node.value)
        self._traverse_inorder_dfs_left(node.right, container)
        return None
    
    def _traverse_inorder_dfs_right(self, node: Node, container: List[int]) -> None:
        if node is None:
            return None
        self._traverse_inorder_dfs_right(node.right, container)
        container.append(node.value)
        self._traverse_inorder_dfs_right(node.left, container)
        return None
    
    def tree_sort(self, ascending: bool) -> List[int]:
        result: List[int] = []
        if ascending:
            self._traverse_inorder_dfs_left(self.root, result)
        else:
            self._traverse_inorder_dfs_right(self.root, result)
        return result


class TestTreeSort(unittest.TestCase):
    def test_tree_sort_ascending(self):
        numbers: List[int] = [5, 6, 7, 2, 1, 6, 2]  # duplicates
        bst = BinarySearchTree()
        for n in numbers:
            bst.insert(n)
        
        actual: List[int] = bst.tree_sort(ascending=True)
        expected: List[int] = sorted(numbers)
        self.assertTrue(actual, expected)

    def test_tree_sort_descending(self):
        numbers: List[int] = [5, 6, 7, 2, 1, 6, 2]  # duplicates
        bst = BinarySearchTree()
        for n in numbers:
            bst.insert(n)

        actual: List[int] = bst.tree_sort(ascending=False)
        expected: List[int] = sorted(numbers, reverse=True)
        self.assertTrue(actual, expected)

    
if __name__ == "__main__":
    unittest.main()
