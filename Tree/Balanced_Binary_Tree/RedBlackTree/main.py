from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List
from rich import print
import unittest

class Color(Enum):
    BLACK = "Black"
    RED = "Red"

@dataclass
class Node:
    key: Optional[int]
    parent: Optional["Node"] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    color: Color = Color.RED


class RedBlackTree:
    def __init__(self):
        self.NIL: Node = Node(None)
        self.NIL.color = Color.BLACK
        self.root: Node = self.NIL

    def left_rotate(self, x: Node) -> None:
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

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        x.parent = y
        y.left = x
        return None

    def right_rotate(self, x: Node) -> None:
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

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

        x.parent = y
        y.right = x
        return None

    def transplant(self, u: Node, v: Node) -> None:
        if u.parent is None:
            self.root = v
            
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        
        v.parent = u.parent
        return None

    def search(self, key: int) -> Node:
        node: Node = self.root
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def contains(self, key: int) -> bool:
        if self.search(key) == self.NIL:
            return False
        return True
    
    def get_min(self, node: Node) -> Node:
        while node.left != self.NIL:
            node = node.left
        return node
    
    def inorder_traversal(self, node: Node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(f"{node.key} ({node.color.value})", end=" ")
            self.inorder_traversal(node.right)

    def print_tree(self) -> None:
        self.inorder_traversal(self.root)
        print()

    def insert(self, key: int) -> bool:
        new_node: Node = Node(key=key, left=self.NIL, right=self.NIL)

        temp: Node = self.root
        parent: Optional[Node] = None
        while temp != self.NIL:
            parent = temp
            if key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right
            else:
                return False
        
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self.insert_fixup(new_node)
        return True

    def insert_fixup(self, node: Node):
        """Fix up red-black tree structure after isnertion
        x: parent of the inserted child
        y: sibling of x
        z: inserted new child to x
        
        e.g.
            .
           / \
          y   x
               \
                z
        """
        
        z: Node = node
        while z.parent is not None and z.parent.color == Color.RED:
            x: Node = z.parent

            if x.parent.left == x:
                y: Node = x.parent.right
                match y.color:
                    case Color.RED:
                        x.parent.color = Color.RED
                        x.color = Color.BLACK
                        y.color = Color.BLACK
                        z = x.parent

                    case Color.BLACK:
                        if x.right == z:
                            """
                              .
                             / \
                            x   y
                             \   
                              z
                            """
                            z = z.parent
                            self.left_rotate(z)
                        
                        """
                            .
                           / \
                          x   y
                         /  
                        z
                        """
                        z.parent.color = Color.BLACK
                        z.parent.parent.color = Color.RED
                        self.right_rotate(z.parent.parent)
            
            elif x.parent.right == x:
                y = x.parent.left

                match y.color:
                    case Color.RED:
                        x.parent.color = Color.RED
                        x.color = Color.BLACK
                        y.color = Color.BLACK
                        z = x.parent
                    
                    case Color.BLACK:
                        if x.left == z:
                            """
                              .
                             / \
                            y   x
                               /
                              z
                            """
                            z = z.parent
                            self.right_rotate(z)
                        
                        """
                          .
                         / \
                        y   x
                             \
                              z
                        """
                        z.parent.color = Color.BLACK
                        z.parent.parent.color = Color.RED
                        self.left_rotate(z.parent.parent)
        
        self.root.color = Color.BLACK
        return None

    def delete(self, key: int) -> bool:
        """Delete the node with the target key from the red-black tree"""

        z: Node = self.search(key)
        if z == self.NIL:
            return False
        
        y: Node = z
        y_original_color: Color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.get_min(z.right)
            y_original_color = y.color
            x = y.right
            if y != z.right:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == Color.BLACK:
            self.delete_fixup(x)

        return True

    def delete_fixup(self, x: Node) -> None:
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.left_rotate(x.parent)
                    sibling = x.parent.right
                
                if sibling.left.color == Color.BLACK and sibling.right.color == Color.BLACK:
                    sibling.color = Color.RED
                    x = x.parent
                else:
                    if sibling.right.color == Color.BLACK:
                        sibling.left.color = Color.BLACK
                        sibling.color = Color.RED
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    
                    sibling.color = x.parent.color
                    x.parent.color = Color.BLACK
                    sibling.right.color = Color.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            
            else:
                sibling = x.parent.left
                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                
                if sibling.right.color == Color.BLACK and sibling.left.color == Color.BLACK:
                    sibling.color = Color.RED
                    x = x.parent
                else:
                    if sibling.left.color == Color.BLACK:
                        sibling.right.color = Color.BLACK
                        sibling.color = Color.RED
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    
                    sibling.color = x.parent.color
                    x.parent.color = Color.BLACK
                    sibling.left.color = Color.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        
        x.color = Color.BLACK
        return None


class TestRedBlackTree(unittest.TestCase):
    def test_insert(self):
        """Test inserting elements into the trees."""
        rb: RedBlackTree = RedBlackTree()
        keys: List[int] = [50, 37, 25, 18, 22, 31, 34, 33]
        for key in keys:
            expected: bool = True
            actual: bool = rb.insert(key)
            self.assertEqual(expected, actual)
        
        for key in keys:
            expected: bool = True
            actual: bool = rb.contains(key)
            self.assertEqual(expected, actual)

    def test_root_is_black(self):
        """Ensure the root is always black after insertions"""
        rb: RedBlackTree = RedBlackTree()
        rb.insert(10)
        rb.insert(20)
        actual: Color = rb.root.color
        expected: Color = Color.BLACK
        self.assertEqual(actual, expected)

    def test_no_consecutive_red_nodes(self):
        """Check that no two consecutive red nodes exist in the tree"""
        rb: RedBlackTree = RedBlackTree()
        keys: List[int] = [50, 37, 25, 18, 22, 31, 34, 33]
        for key in keys:
            rb.insert(key)

        def check_no_red_violation(node):
            if node == rb.NIL:
                return True
            
            if node.color == Color.RED:
                self.assertEqual(node.left.color, Color.BLACK)
                self.assertEqual(node.right.color, Color.BLACK)

            check_no_red_violation(node.left)
            check_no_red_violation(node.right)
        
        check_no_red_violation(rb.root)

    def test_delete(self):
        """Test deleting elements and maintaining red black tree properties"""
        rb: RedBlackTree = RedBlackTree()
        keys: List[int] = [50, 37, 25, 18, 22, 31, 34, 33]
        for key in keys:
            rb.insert(key)

        actual: bool = rb.contains(25)
        expected: bool = True
        self.assertEqual(actual, expected)

        rb.delete(25)

        actual: bool = rb.contains(25)
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_deleting_root(self):
        """Test deleting the root and ensuring tree remains balanced"""
        rb: RedBlackTree = RedBlackTree()
        rb.insert(20)
        rb.insert(10)
        rb.insert(30)

        # delete root
        rb.delete(20)

        actual: bool = rb.contains(20)
        expected: bool = False
        self.assertEqual(actual, expected)

        actual: bool = rb.contains(10)
        expected: bool = True
        self.assertEqual(actual, expected)

        actual: bool = rb.contains(30)
        expected: bool = True
        self.assertEqual(actual, expected)


class TestDrive:
    @staticmethod
    def main(*args, **kwargs):
        rb: RedBlackTree = RedBlackTree()

        # Insert keys
        keys: List[int] = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6]
        for key in keys:
            rb.insert(key)

        print("Initial tree:")
        print(rb.root.key, rb.root.color)
        rb.print_tree()

        # Delete some keys
        print("\nDeleting 10:")
        rb.delete(10)
        print(rb.root.key, rb.root.color)
        rb.print_tree()

        print("\nDeleting 7:")
        rb.delete(7)
        print(rb.root.key, rb.root.color)
        rb.print_tree()

        print("\nDeleting 22:")
        rb.delete(22)
        print(rb.root.key, rb.root.color)
        rb.print_tree()


if __name__ == "__main__":
    # unittest.main()
    TestDrive.main()
