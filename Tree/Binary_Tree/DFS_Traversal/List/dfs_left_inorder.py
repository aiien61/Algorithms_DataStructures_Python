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


def traverse_inorder(root: Node) -> None:
    if root is None:
        return None

    traverse_inorder(root.left)
    
    # do something in between left and right traversal operation if in-order
    print(root.value, end=' ')
    
    traverse_inorder(root.right)
    return None


if __name__ == '__main__':
    tree = build_tree([5, 2, 6, 1, 4, None, 7, None, None,
                      3, None, None, None, None, None])
    print('in-order:', end=' ')
    traverse_inorder(tree.root)
