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
        new_node = Node(value) if not isinstance(value, Node) else value

        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
def build_tree(values: List[int]) -> BinarySearchTree:
    bst = BinarySearchTree()
    for value in values:
        if value is not None:
            bst.insert(value)
    return bst

def traverse_preorder(root: Node) -> None:
    if root is None:
        return None
    
    # do something before traversal when pre-order
    print(root.value, end=' ')

    traverse_preorder(root.right)
    traverse_preorder(root.left)
    return None

if __name__ == '__main__':
    tree = build_tree([5, 2, 6, 1, 4, None, 7, None, None, 3, None, None, None, None, None])
    print('pre-order:', end=' ')
    traverse_preorder(tree.root)
