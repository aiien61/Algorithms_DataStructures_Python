from dataclasses import dataclass
from typing import List
import unittest

@dataclass
class AVLNode:
    value: int
    left: "AVLNode" = None
    right: "AVLNode" = None

class AVLTree:
    def __init__(self, nums: List[int]=None):
        self.root: AVLNode = None
        if nums:
            self.build_tree(nums)

    def build_tree(self, nums: List[int]) -> None:
        for num in nums:
            self.insert(num)

    def insert(self, value: int) -> bool:
        self.root = self._insert(self.root, value)
        self.root = self._balance(self.root)
        return True

    def _insert(self, node: AVLNode, value: int) -> AVLNode:
        if node is None:
            return AVLNode(value)
        
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        
        return node
    
    def delete(self, value: int) -> bool:
        if self.contains(value):
            self.root = self._delete(self.root, value)
            self.root = self._balance(self.root)
            return True
        return False
        

    def _delete(self, node: AVLNode, value: int):
        if node is None:
            return None
        
        if value == node.value:
            match (node.left, node.right):
                case (None, None): return None
                case (AVLNode, None): return node.left
                case (None, AVLNode): return node.right
                case _:
                    sub_tree_max: int = self._get_max(node.left).value
                    node.value = sub_tree_max
                    node.left = self._delete(node.left, sub_tree_max)
                    return node
        
        if value < node.value:
            node.left = self._delete(node.left, value)
        else:
            node.right = self._delete(node.right, value)
        return node

    def contains(self, value: int) -> bool:
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False
    
    def search(self, value: int) -> AVLNode | None:
        node = self.root
        while node:
            if value == node.value:
                return node
            node = node.left if value < node.value else node.right
        return None

    def _get_max(self, node: AVLNode) -> AVLNode:
        while node.right:
            node = node.right
        return node
    
    def inorder(self) -> List[int]:
        result: List[int] = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node: AVLNode, container: List[int]) -> None:
        if node:
            self._inorder(node.left, container)
            container.append(node.value)
            self._inorder(node.right, container)
        return None
    
    def _balance(self, node: AVLNode) -> AVLNode:
        gap: int = self._get_depth(node.left) - self._get_depth(node.right)
        if abs(gap) < 2:
            return node
 
        # skew to the right
        if gap < -1:
            # skew to the left
            if self._get_depth(node.right.right) < self._get_depth(node.right.left):
                node.right = self._right_rotate(node.right)
            node = self._left_rotate(node)
        # skew to the left
        elif gap > 1:
            # skew to the right
            if self._get_depth(node.left.right) > self._get_depth(node.left.left):
                node.left = self._left_rotate(node.left)
            node = self._right_rotate(node)
        
        return node

    def _left_rotate(self, node: AVLNode) -> AVLNode:
        new_root: AVLNode = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
    
    def _right_rotate(self, node: AVLNode) -> AVLNode:
        new_root: AVLNode = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root
    
    def _get_depth(self, node: AVLNode) -> int:
        if node is None:
            return 0
        return 1 + max(self._get_depth(node.left), self._get_depth(node.right))

class TestAVLTree(unittest.TestCase):
    def test_build_tree(self):
        avl: AVLTree = AVLTree()
        avl.build_tree([10, 20, 30, 40, 50, 25])
        actual: List[int] = avl.inorder()
        expected: List[int] = [10, 20, 25, 30, 40, 50]
        self.assertEqual(actual, expected)
    
    def test_insert(self):
        avl: AVLTree = AVLTree()
        avl.insert(35)
        actual: bool = avl.contains(35)
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_delete_when_tree_has_target_to_delete(self):
        avl: AVLTree = AVLTree([10, 20, 30])
        avl.delete(20)
        actual: bool = avl.contains(20)
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_delete_when_tree_has_no_target_to_delete(self):
        avl: AVLTree = AVLTree([10, 20, 30])
        actual: bool = avl.delete(100)
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_search_when_found(self):
        avl: AVLTree = AVLTree([10, 20, 30])
        self.assertIsNotNone(avl.search(30))

    def test_search_when_not_found(self):
        avl: AVLTree = AVLTree([10, 20, 30])
        self.assertIsNone(avl.search(100))

    def test_inorder(self):
        avl: AVLTree = AVLTree([10, 20, 30, 40, 50, 25])
        actual: List[int] = avl.inorder()
        expected: List[int] = [10, 20, 25, 30, 40, 50]
        self.assertEqual(actual, expected)


    def test_balance_after_insert(self):
        avl: AVLTree = AVLTree([10, 20])
        avl.insert(30)
        depth_left = avl._get_depth(avl.root.left)
        depth_right = avl._get_depth(avl.root.right)
        self.assertTrue(abs(depth_left - depth_right) <= 1)

    def test_balance_after_delete(self):
        avl: AVLTree = AVLTree([20, 10, 30, 60])
        avl.delete(10)
        depth_left = avl._get_depth(avl.root.left)
        depth_right = avl._get_depth(avl.root.right)
        self.assertTrue(abs(depth_left - depth_right) <= 1)

if __name__ == '__main__':
    unittest.main()

