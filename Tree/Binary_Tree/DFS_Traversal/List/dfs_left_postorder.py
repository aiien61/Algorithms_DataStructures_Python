from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> bool:
        if not isinstance(value, Node):
            new_node = Node(value)

        if not self.root:
            self.root = new_node
            return True

        temp_node = self.root
        while True:
            if new_node.value == temp_node.value:
                return False
            if new_node.value < temp_node.value:
                if temp_node.left is None:
                    temp_node.left = new_node
                    return True
                else:
                    temp_node = temp_node.left
            elif new_node.value > temp_node.value:
                if temp_node.right is None:
                    temp_node.right = new_node
                    return True
                else:
                    temp_node = temp_node.right


def build_tree(values: List[int]) -> BinarySearchTree:
    bst = BinarySearchTree()
    for value in values:
        if value is not None:
            bst.insert(value)
    return bst


def traverse_postorder(root: Node) -> None:
    if root is None:
        return None

    traverse_postorder(root.left)
    traverse_postorder(root.right)

    # do something after traversal if post-order
    print(root.value, end=' ')
    return None


if __name__ == '__main__':
    tree = build_tree([5, 2, 6, 1, 4, None, 7, None, None,
                      3, None, None, None, None, None])
    print('post-order:', end=' ')
    traverse_postorder(tree.root)
