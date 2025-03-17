from enum import Enum
from dataclasses import dataclass

class Color(Enum):
    RED = "Red"
    BLACK = "Black"

@dataclass
class Node:
    key: int
    color: Color = Color.RED
    left: 'Node' = None
    right: 'Node' = None
    parent: 'Node' = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, Color.BLACK)
        self.root = self.NIL


def rb_transplant(T: RedBlackTree, u: Node, v: Node):
    if u.p == T.NIL:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p


def get_min(z: Node) -> Node:
    temp: Node = z
    if temp.left:
        temp = temp.left
    return temp


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
    if y.left != T.NIL:
        y.left.parent = x

    y.parent = x.parent
    if x.parent == T.NIL:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y
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

    if y.right != T.NIL:
        y.right.parent = x

    y.parent = x.parent

    if x.parent == T.NIL:
        T.root = y
    elif x.parent.left == x:
        x.parent.left = y
    else:
        x.parent.right = y

    y.right = x
    x.parent = y
    return y

def delete(T: RedBlackTree, z: Node):
    y: Node = z
    y_original_color: Color = y.color
    if z.left == T.NIL:
        x = z.right
        rb_transplant(T, z, z.right)
    elif z.right == T.NIL:
        x = z.left
        rb_transplant(T, z, z.left)
    else:
        y = get_min(z.right)
        y_original_color = y.color
        x = y.right
        if y != z.right:
            rb_transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        else:
            x.p = y
        rb_transplant(T, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    if y_original_color == Color.BLACK:
        deletion_fixup(T, x)


def deletion_fixup(T: RedBlackTree, node: Node):
    while node != T.root and node.color == Color.BLACK:
        if node == node.parent.left:
            sibling = node.parent.right
            if sibling.color == Color.RED:
                sibling.color = Color.BLACK
                node.parent.color = Color.RED
                _ = left_rotate(T, node.parent)
                sibling = node.parent.right
            if sibling.left.color == Color.BLACK and sibling.right.color == Color.BLACK:
                sibling.color = Color.RED
                node = node.parent
            else:
                if sibling.right.color == Color.BLACK:
                    sibling.left.color = Color.BLACK
                    sibling.color = Color.RED
                    _ = right_rotate(T, sibling)
                    sibling = node.parent.right
                sibling.color = node.parent.color
                node.parent.color = Color.BLACK
                sibling.right.color = Color.BLACK
                _ = left_rotate(T, node.parent)
                node = T.root
        else:
            sibling = node.parent.left
            if sibling.color == Color.RED:
                sibling.color = Color.BLACK
                node.parent.color = Color.RED
                _ = right_rotate(T, node.parent)
                sibling = node.parent.left
            if sibling.right.color == Color.BLACK and sibling.left.color == Color.BLACK:
                sibling.color = Color.RED
                node = node.parent
            else:
                if sibling.left.color == Color.BLACK:
                    sibling.right.color = Color.BLACK
                    sibling.color = Color.RED
                    _ = left_rotate(T, sibling)
                    sibling = node.parent.left
                sibling.color = node.parent.color
                node.parent.color = Color.BLACK
                sibling.left.color = Color.BLACK
                _ = right_rotate(T, node.parent)
                node = T.root
    
    node.color = Color.BLACK
