"""
Given that
postorder traversal: 1 3 4 2 7 6 5
inorder traversal: 1 2 3 4 5 6 7

Reverse to original binary tree
"""

from typing import List, Tuple
from icecream import ic


class Solution:
    inorder: List[int] = [26, 6, 30, 21, 9, 5, 17]
    postorder: List[int] = [26, 6, 30, 17, 5, 9, 21]

    # postorder: List[int] = [1, 3, 4, 2, 7, 6, 5]
    # inorder: List[int] = [1, 2, 3, 4, 5, 6, 7]
    
    binary_tree: List[int] = [None]

    @staticmethod
    def divide(nums: List[int], root: int) -> Tuple[list, list]:
        root_i: int = nums.index(root)
        return nums[: root_i], nums[root_i + 1:]

    @staticmethod
    def find_root(nums: List[int]):
        return nums.pop()

    @classmethod
    def make_tree(cls, root_index: int, nums: List[int]):
        root: int = cls.find_root(cls.postorder)

        size: int = len(cls.binary_tree)
        if size <= root_index:
            new_bt: List[int] = [None] * (root_index + 1)
            new_bt[: size] = cls.binary_tree[:]
            cls.binary_tree = new_bt
        cls.binary_tree[root_index] = root

        left, right = cls.divide(nums, root)

        if right:
            cls.make_tree((root_index + 1) * 2, right)

        if left:
            cls.make_tree((root_index + 1) * 2 - 1, left)

        return None

    @classmethod
    def main(cls):
        cls.make_tree(0, cls.inorder)
        return cls.binary_tree


if __name__ == "__main__":
    tree = Solution.main()
    ic(tree)
