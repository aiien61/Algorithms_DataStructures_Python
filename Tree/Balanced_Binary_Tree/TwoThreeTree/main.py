"""Implementation of 2-3 Tree"""
from typing import List, Tuple, Optional
import unittest

class Node:
    def __init__(self, keys: List[int]=None, parent=None):
        self.keys = [] if keys is None else keys
        self.parent: "Node" = parent
        self.children: List["Node"] = []
    
    @property
    def first_key(self) -> int:
        return self.keys[0]
    
    @property
    def last_key(self) -> int:
        return self.keys[-1]
    
    @property
    def middle_key(self) -> Optional[int]:
        if len(self.keys) < 3:
            return None
        return self.keys[1]
    
    @property
    def left(self) -> Optional["Node"]:
        if not self.children:
            return None
        return self.children[0]
    
    @property
    def right(self) -> Optional["Node"]:
        if len(self.children) < 2:
            return None
        return self.children[-1]
    
    @property
    def middle(self) -> Optional["Node"]:
        if len(self.children) < 3:
            return None
        return self.children[1]
    
    def append_key(self, num: int) -> bool:
        self.keys.append(num)
        self.keys = sorted(self.keys)
        return True
    
    def is_end_node(self) -> bool:
        match (self.left, self.middle, self.right):
            case (None, None, None): return True
            case _: return False

    def __repr__(self):
        return f"Node(keys={self.keys}, parent={self.parent}, children={self.children})"


class TwoThreeTree:
    def __init__(self):
        self.root: Node = None
    
    def insert(self, key: int) -> None:
        """
        Aims: 
        1. all leaves at the same level
        2. no any child node of non-leaf nodes is none 
        """
        if not self.root:
            self.root = Node(keys=[key])
            return None
        
        return self._insert_helper(self.root, key)

    def _insert_helper(self, node: Node, key: int) -> None:
        if key in node.keys:
            return None

        if node.is_end_node():
            node.append_key(key)
            if node.middle_key is not None:
                node, left, right = self._split(node)
                self._merge_with_parent(node, left, right)
            return None
        
        next_node: Node = self._sink_down(node, key)
        return self._insert_helper(next_node, key)
    
    def _split(self, node: Node) -> Tuple[Node]:
        left = Node(keys=[node.keys.pop(0)], parent=node.parent)
        right = Node(keys=[node.keys.pop(-1)], parent=node.parent)

        # non-leaf node
        if node.children:
            left.children.append(node.children.pop(0))
            left.children.append(node.children.pop(0))
            right.children.append(node.children.pop(0))
            right.children.append(node.children.pop(0))
            for child in left.children:
                child.parent = left
            for child in right.children:
                child.parent = right

        return node, left, right
    
    def _merge_with_parent(self, node: Node, left: Node, right: Node) -> None:
        if node.parent:
            parent = node.parent
            parent.append_key(node.keys.pop())
            parent.children.remove(node)
            parent.children.extend([left, right])
            parent.children.sort(key=lambda n: n.first_key)
            if len(parent.keys) == 3:
                self._merge_with_parent(*self._split(parent))
        else:
            self.root = Node()
            self.root.append_key(node.keys.pop())
            self.root.children.extend([left, right])
            left.parent = self.root
            right.parent = self.root

        return None

    def _sink_down(self, node: Node, key: int) -> Node:
        next_node: Node = node
        if len(node.keys) == 1:
            match key:
                case key if key < node.first_key: next_node = node.left
                case key if key > node.first_key: next_node = node.right
        elif len(node.keys) == 2:
            match key:
                case key if key < node.first_key: next_node = node.left
                case key if key > node.last_key: next_node = node.right
                case _: next_node = node.middle
        
        return next_node

    def search(self, target: int) -> Optional[Node]:
        if not self.root:
            return None
        return self._search_helper(self.root, target)

    def _search_helper(self, node: Node, target: int) -> Optional[Node]:
        if target in node.keys:
            return node
        
        # types of end node include 1-key node, 2-key node, and 3-key node
        if node.is_end_node():
            return None
        
        # when the node has only 1 key
        if len(node.keys) == 1:
            node = node.left if target < node.first_key else node.right
            return self._search_helper(node, target)
        
        # when the node has only 2 keys
        match target:
            case target if target < node.first_key: 
                node = node.left
            case target if target > node.last_key:
                node = node.right
            case _:
                node = node.middle
        return self._search_helper(node, target)
    
    def preorder(self) -> List[int]:
        result: List[int] = []
        self._preorder_helper(self.root, result)
        return result
    
    def _preorder_helper(self, node: Node, container: List[int]) -> None:
        if not node:
            return None
        
        if len(node.keys) > 0:
            container.append(node.keys[0])

        if node.left:
            self._preorder_helper(node.left, container)

        if len(node.keys) > 1:
            container.append(node.keys[1])
        
        if node.middle:
            self._preorder_helper(node.middle, container)

        if len(node.keys) > 2:
            container.append(node.keys[2])

        if node.right:
            self._preorder_helper(node.right, container)
        
        return None


class TestTwoThreeTree(unittest.TestCase):
    def test_insert_when_two_key_nodes(self):
        nums: List[int] = [39, 28, 17, 13, 11]
        tree = TwoThreeTree()
        for num in nums:
            tree.insert(num)

        actual: List[int] = tree.preorder()
        expected: List[int] = [13, 11, 28, 17, 39]
        self.assertEqual(actual, expected)

    def test_insert_when_one_key_nodes(self):
        nums: List[int] = [39, 28, 17, 13, 11, 3, 4]
        tree = TwoThreeTree()
        for num in nums:
            tree.insert(num)

        actual: List[int] = tree.preorder()
        expected: List[int] = [13, 4, 3, 11, 28, 17, 39]
        self.assertEqual(actual, expected)

    def test_insert_when_merge_from_right(self):
        nums: List[int] = [39, 28, 17, 50, 60, 65, 70]
        tree = TwoThreeTree()
        for num in nums:
            tree.insert(num)

        actual: List[int] = tree.preorder()
        expected: List[int] = [50, 28, 17, 39, 65, 60, 70]
        self.assertEqual(actual, expected)

    def test_search_when_found(self):
        nums: List[int] = [39, 28, 17, 13, 11, 3, 4]
        tree = TwoThreeTree()
        for num in nums:
            tree.insert(num)

        actual: bool = 17 in tree.search(17).keys
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_search_when_not_found(self):
        nums: List[int] = [39, 28, 17, 13, 11, 3, 4]
        tree = TwoThreeTree()
        for num in nums:
            tree.insert(num)

        actual = tree.search(100)
        expected = None
        self.assertEqual(actual, expected)

    def test_insert_order_numbers(self):
        nums: List[int] = [10, 20, 30, 40, 50, 60, 70, 80]
        tree = TwoThreeTree()
        for num in nums:
            tree.insert(num)

        actual: List[int] = tree.preorder()
        expected: List[int] = [40, 20, 10, 30, 60, 50, 70, 80]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
