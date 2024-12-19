from typing import List, Optional, Iterable, Deque
from dataclasses import dataclass
from collections import deque
from icecream import ic
import unittest

ic.disable()

class BinaryTree:
    @dataclass
    class Node:
        value: int
        left: Optional['BinaryTree.Node'] = None
        right: Optional['BinaryTree.Node'] = None

    def __init__(self, array: List[Optional[int]]):
        self.array = array
        self.root: Optional[BinaryTree.Node] = None
        self._build_tree()
        ic(self.root)


    def _build_tree(self) -> None:
        if not self.array or self.array[0] is None:
            return None
        
        # Create node instances
        nodes: List[object] = [BinaryTree.Node(x) if x is not None else None for x in self.array]

        # Set root
        self.root = nodes[0]

        for i, node in enumerate(nodes):
            if node is None:
                continue

            left_index: int = (i + 1) * 2 - 1
            right_index: int = (i + 1) * 2

            if left_index < len(nodes):
                node.left = nodes[left_index]
            
            if right_index < len(nodes):
                node.right = nodes[right_index]

    def traverse_level_order_bfs(self) -> List[int]:
        if not self.root:
            return []
        
        result: List[int] = []
        queue: Deque = deque([self.root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
        
        return result
    
class TestBinaryTreeBFS(unittest.TestCase):
    def test_empty_tree(self):
        tree = BinaryTree([])
        actual = tree.traverse_level_order_bfs()
        expected = []
        self.assertEqual(actual, expected)

    def test_single_node_tree(self):
        tree = BinaryTree([1])
        actual: List[int] = tree.traverse_level_order_bfs()
        expected: List[int] = [1]
        self.assertEqual(actual, expected)

    def test_full_tree(self):
        tree = BinaryTree([1, 2, 3, 4, 5, 6, 7])
        actual: List[int] = tree.traverse_level_order_bfs()
        expected: List[int] = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(actual, expected)

    def test_tree_with_nulls(self):
        tree = BinaryTree([1, 2, 3, None, 5, None, 7])
        actual: List[int] = tree.traverse_level_order_bfs()
        expected: List[int] = [1, 2, 3, 5, 7]
        self.assertEqual(actual, expected)

    def test_tree_with_deep_nulls(self):
        tree = BinaryTree([1, None, 2, None, None, None, 3])
        actual: List[int] = tree.traverse_level_order_bfs()
        expected: List[int] = [1, 2, 3]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()