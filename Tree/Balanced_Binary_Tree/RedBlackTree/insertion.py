from enum import Enum
from typing import List, Optional
from dataclasses import dataclass
import unittest

class Color(Enum):
    RED = "Red"
    BLACK = "Black"

@dataclass
class Node:
    key: Optional[int] = None
    color: Color = Color.RED
    parent: Optional["Node"] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    

class RedBlackTree:
    def __init__(self):
        self.nil: Node = Node(color=Color.BLACK)
        self.root: Optional[Node] = self.nil
    
def insert(T: RedBlackTree, key: int) -> None:
    new_node: Node = Node(key=key, parent=T.nil, left=T.nil, right=T.nil)
    
    node: Node = T.root
    p: Node = T.nil
    while node != T.nil:
        p = node
        if key < node.key:
            node = node.left
        elif key > node.key:
            node = node.right
        else:
            return None

    new_node.parent = p
    if p == T.nil:
        T.root = new_node
    elif new_node.key < p.key:
        p.left = new_node
    else:
        p.right = new_node

    fixup(T, new_node)
    return None
    
def fixup(T: RedBlackTree, new_leaf: Node) -> None:
    z: Node = new_leaf
    while z.parent.color == Color.RED:
        x: Node = z.parent
        if x.parent.left == x:
            y: Node = x.parent.right
            if y.color == Color.RED:
                x.parent.color = Color.RED
                x.color = Color.BLACK
                y.color = Color.BLACK
                z = x.parent
            elif y.color == Color.BLACK:
                if x.right == z:
                    x = left_rotate(T, x)
                    z = x.left
                x.parent.color = Color.RED
                x.color = Color.BLACK
                z = right_rotate(T, x.parent)
        elif x.parent.right == x:
            y = x.parent.left
            if y.color == Color.RED:
                x.parent.color = Color.RED
                x.color = Color.BLACK
                y.color = Color.BLACK
                z = x.parent
            elif y.color == Color.BLACK:
                if x.left == z:
                    x = right_rotate(T, x)
                    z = x.right
                x.parent.color = Color.RED
                x.color = Color.BLACK
                z = left_rotate(T, x.parent)

    T.root.color = Color.BLACK
    return None
            

def left_rotate(T: RedBlackTree, x: Node) -> Node:
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
    elif x.parent.left == x:
        x.parent.left = y
    else:
        x.parent.right = y
    
    x.parent = y
    y.left = x
    return y

def right_rotate(T: RedBlackTree, x: Node) -> Node:
    """right rotate x to y to be the new root of the tree
        |
        x
       / \
      y   r
     / \
    a   b
    """
    y: Node = x.left
    x.left = y.right

    if y.right != T.nil:
        y.right.parent = x

    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x.parent.left == x:
        x.parent.left = y
    else:
        x.parent.right = y
    
    x.parent = y
    y.right = x
    return y

class TestRedBlackTree(unittest.TestCase):
    def test_empty_rb(self):
        rb = RedBlackTree()
        actual: Node = rb.root
        expected: Node = rb.nil
        self.assertEqual(actual, expected)

        actual: Color = rb.root.color
        expected: Color = Color.BLACK
        self.assertEqual(actual, expected)

    def test_insert_root(self):
        rb = RedBlackTree()

        insert(rb, 10)
        actual: int = rb.root.key
        expected: int = 10
        self.assertEqual(actual, expected)

        actual: Color = rb.root.color
        expected: Color = Color.BLACK
        self.assertEqual(actual, expected)

    def test_insert_left_right_children(self):
        rb = RedBlackTree()

        insert(rb, 10)
        insert(rb, 5)
        insert(rb, 15)

        actual: List[int] = [rb.root.left.key, rb.root.right.key]
        expected: List[int] = [5, 15]
        self.assertEqual(actual, expected)

    def test_insert_balancing(self):
        rb = RedBlackTree()
        keys: List[int] = [10, 5, 15, 1, 7, 12, 20]
        for key in keys:
            insert(rb, key)
        
        actual: Color = rb.root.color
        expected: Color = Color.BLACK
        self.assertEqual(actual, expected)

        def validate_rb(node: Node):
            if node == rb.nil:
                return 1
            
            if node.color == Color.RED:
                self.assertEqual(node.left.color, Color.BLACK)
                self.assertEqual(node.right.color, Color.BLACK)
            
            left_bh: int = validate_rb(node.left)
            right_bh: int = validate_rb(node.right)
            self.assertEqual(left_bh, right_bh)

            return left_bh + (1 if node.color == Color.BLACK else 0)
        
        validate_rb(rb.root)

    def test_duplicate_insert(self):
        rb = RedBlackTree()
        insert(rb, 10)
        before_insert = rb.root
        insert(rb, 10)
        self.assertIs(rb.root, before_insert)

if __name__ == "__main__":
    unittest.main()    
