class Solution:
    """Compare two trees"""

    class TreeNode:
        def __init__(self, value: int):
            self.value = value
            self.left = None
            self.right = None
        
    def is_same_tree(self, tree_root_p: object, tree_root_q: object) -> bool:
        if (tree_root_p is None) and (tree_root_q is None):
            return True
        
        if (tree_root_p is not None) and (tree_root_q is None):
            return False
        
        if (tree_root_p is None) and (tree_root_q is not None):
            return False
        
        is_same = True

        if tree_root_p.value != tree_root_q.value:
            return False
        else:
            is_same = self.is_same_tree(tree_root_p.left, tree_root_q.left)
            if not is_same:
                return is_same
            is_same = self.is_same_tree(tree_root_p.right, tree_root_q.right)
            if not is_same:
                return is_same

        return is_same


if __name__ == "__main__":
    a = Solution().TreeNode(1)
    b = Solution().TreeNode(2)
    c = Solution().TreeNode(1)
    a.left = b
    a.right = c

    x = Solution().TreeNode(1)
    y = Solution().TreeNode(2)
    z = Solution().TreeNode(1)
    x.left = y
    x.right = z

    print(Solution().is_same_tree(a, x))
