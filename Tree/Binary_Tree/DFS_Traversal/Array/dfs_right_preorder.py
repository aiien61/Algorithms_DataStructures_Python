from typing import List


class BinarySearchTree:
    def __init__(self, values: List[int]):
        self.array: List[int] = values

    # DFS right pre-order
    def traverse_preorder(self):
        if len(self.array) <= 0:
            return None

        i_root: int = 0
        if self.array[i_root] is None:
            return None

        self._traverse_preorder(i_root)

    def _traverse_preorder(self, index: int):
        # condition to cease
        if index >= len(self.array):
            return None

        # do soemthing before traversal when pre-order
        if self.array[index] is not None:
            print(self.array[index], end=" ")

        # go to the right child
        self._traverse_preorder((index + 1) * 2)
        # go to the left child
        self._traverse_preorder((index + 1) * 2 - 1)


if __name__ == '__main__':
    bst = BinarySearchTree([5, 2, 6, 1, 4, None, 7, None, None, 3, None, None, None, None, None])
    bst.traverse_preorder()
