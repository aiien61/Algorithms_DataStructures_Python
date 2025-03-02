from typing import List, Optional
from dataclasses import dataclass
from icecream import ic
from enum import Enum

class Color(Enum):
    RED = "Red"
    BLACK = "Black"

@dataclass
class Node:
    key: int = None
    color: Color = Color.RED
    parent: Optional["Node"] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None

class BSTree:
    def __init__(self, keys: List[int]):
        self.nil: Node = Node(color=Color.BLACK)
        self.root: Optional[Node] = self.nil
        self.build_tree(keys)

    def build_tree(self, keys: List[int]) -> None:
        for key in keys:
            self.insert(key)
        return None

    def init_node(self, key: int) -> Node:
        return Node(key=key, parent=self.nil, left=self.nil, right=self.nil)
    
    def insert(self, key: int):
        if self.root == self.nil:
            self.root = self.init_node(key)
            return None
        
        node: Node = self.root
        parent: Node = self.nil
        while node != self.nil:
            parent = node
            node = node.left if key < node.key else node.right
        
        new_node: Node = self.init_node(key)
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        
        new_node.parent = parent
    

def left_rotate(T: BSTree, x: Node) -> Node:
    """left rotate x to y to be the new root of the tree
      |
      x
     / \
    a   y
       / \
      b   r
    """
    y: Node = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    
    y.left = x
    x.parent = y
    return y
    
def test_drive():
    nums: List[int] = [1, 0, 10, 5, 20]
    bst: BSTree = BSTree(keys=nums)
    ic(bst.root)

    bst.root = left_rotate(bst, bst.root)
    ic(bst.root)

if __name__ == "__main__":
    test_drive()