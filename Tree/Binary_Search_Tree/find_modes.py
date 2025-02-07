from dataclasses import dataclass
from typing import List
import unittest

@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None


class Solution:
    def find_modes(self, root: Node) -> List[int]:
        self.modes: List[int] = []
        self.count_max: int = 0
        self.count_now: int = 0
        self.prev_val: int = None
    
        def inorder(node: Node) -> None:
            if not node:
                return None

            inorder(node.left)

            if self.prev_val is None:
                self.prev_val = node.value
                self.count_now = 1
            elif self.prev_val != node.value:
                self.prev_val = node.value
                self.count_now = 1
            else:
                self.count_now += 1

            if self.count_now > self.count_max:
                self.count_max = self.count_now
                self.modes = [node.value]
            elif self.count_now == self.count_max:
                self.modes.append(node.value)

            inorder(node.right)
        
        inorder(root)
        return self.modes

class TestFindModes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_single_mode(self):
        root: Node = Node(1)
        root.left = Node(0)
        root.right = Node(2)
        root.right.left = Node(2)
        actual: List[int] = self.solution.find_modes(root)
        expected: List[int] = [2]
        self.assertEqual(actual, expected)
    
    def test_multiple_modes(self):
        root: Node = Node(1)
        root.left = Node(0)
        root.left.right = Node(0)
        root.right = Node(2)
        root.right.left = Node(2)
        actual: List[int] = self.solution.find_modes(root)
        expected: List[int] = [0, 2]
        self.assertEqual(actual, expected)

    def test_empty_tree(self):
        root = None
        actual: List[int] = self.solution.find_modes(root)
        expected: List[int] = []
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()