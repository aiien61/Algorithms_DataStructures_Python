"""
Given that
preorder traversal: 5 2 1 4 3 6 7 
inorder traversal: 1 2 3 4 5 6 7

Reverse to original binary tree
"""
from typing import List, Tuple
from icecream import ic


class Solution:
    preorder: List[int] = [10, 9, 7, 3, 6, 2, 8, 5, 4, 1]
    inorder: List[int] = [3, 7, 9, 6, 2, 10, 5, 8, 4, 1]

    # preorder: List[int] = [5, 2, 1, 4, 3, 6, 7]
    # inorder: List[int] = [1, 2, 3, 4, 5, 6, 7]
    binary_tree: List[int] = [None]


    @staticmethod
    def divide(nums: List[int], root: int) -> Tuple[list, list]:
        root_i: int = nums.index(root)
        return nums[: root_i], nums[root_i + 1:]

    @staticmethod
    def find_root(nums: List[int]):
        return nums.pop(0)

    @classmethod
    def make_tree(cls, root_index: int, nums: List[int]):
        root: int = cls.find_root(cls.preorder)
        
        size: int = len(cls.binary_tree)
        if size <= root_index:
            new_bt: List[int] = [None] * (root_index + 1)
            new_bt[: size] = cls.binary_tree[:]
            cls.binary_tree = new_bt
        cls.binary_tree[root_index] = root

        left, right = cls.divide(nums, root)

        if left:
            cls.make_tree((root_index + 1) * 2 - 1, left)
        
        if right:
            cls.make_tree((root_index + 1) * 2, right)

        return None

    @classmethod
    def main(cls):
        cls.make_tree(0, cls.inorder)
        return cls.binary_tree


if __name__ == "__main__":
    tree = Solution.main()
    ic(tree)
