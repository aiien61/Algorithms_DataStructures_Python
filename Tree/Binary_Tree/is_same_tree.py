""" Check whether two trees are identical by traversal
"""
import unittest

class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value: int = value
        self.left: 'TreeNode' = left
        self.right: 'TreeNode' = right


class Solution:
    @classmethod
    def is_same_tree(cls, p: TreeNode, q: TreeNode):
        if p is None and q is None: return True
        if p is not None and q is None: return False
        if p is None and q is not None: return False

        result: bool = True

        if p.value != q.value:
            result = False
        else:
            result_left: bool = cls.is_same_tree(p.left, q.left)
            result_right: bool = cls.is_same_tree(p.right, q.right)
            if result_left == False or result_right == False:
                result = False
            
        return result

class TestSolution(unittest.TestCase):
    def test_is_same_tree_when_same_trees(self):
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
        expected: bool = True
        actual: bool = Solution.is_same_tree(tree1, tree2)
        self.assertEqual(expected, actual)

    def test_is_same_tree_when_different_structures(self):
        tree1 = TreeNode(1, left=TreeNode(2))
        tree2 = TreeNode(1, left=None, right=TreeNode(2))
        expected: bool = False
        actual: bool = Solution.is_same_tree(tree1, tree2)
        self.assertEqual(expected, actual)

    def test_is_same_tree_when_different_values(self):
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(3), TreeNode(2))
        expected: bool = False
        actual: bool = Solution.is_same_tree(tree1, tree2)
        self.assertEqual(expected, actual)

    def test_is_same_tree_when_empty_trees(self):
        expected: bool = True
        actual: bool = Solution.is_same_tree(None, None)
        self.assertEqual(expected, actual)

    def test_is_same_tree_when_one_empty_tree(self):
        tree1 = TreeNode(1)
        tree2 = None
        expected: bool = False
        actual: bool = Solution.is_same_tree(tree1, tree2)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()