from typing import List


class BinarySearchTree:
    def __init__(self, values: List[int]):
        self.array: List[int] = values

    # DFS left post-order
    def traverse_postorder(self):
        if len(self.array) <= 0:
            return None

        i_root: int = 0
        if self.array[i_root] is None:
            return None

        self._traverse_postorder(i_root)

    def _traverse_postorder(self, index: int):
        # condition to cease
        if index >= len(self.array):
            return None

        # go to the left child
        self._traverse_postorder((index + 1) * 2 - 1)

        # go to the right child
        self._traverse_postorder((index + 1) * 2)

        # do soemthing in after traversal when post-order
        if self.array[index] is not None:
            print(self.array[index], end=" ")


if __name__ == '__main__':
    bst = BinarySearchTree([5, 2, 6, 1, 4, None, 7, None, None, 3, None, None, None, None, None])
    bst.traverse_postorder()
