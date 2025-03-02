"""Implementation of 2-3-4 Tree"""
from typing import List, Set, Optional
from icecream import ic
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
        if len(self.keys) == 3:
            return self.keys[1]
        return None
    
    @property
    def left(self) -> Optional["Node"]:
        if self.children:
            return self.children[0]
        return None
    
    @property
    def right(self) -> Optional["Node"]:
        if len(self.children) > 1:
            return self.children[-1]
        return None
    
    @property
    def middle(self) -> Optional["Node"]:
        if len(self.children) == 3:
            return self.children[1]
        return None
    
    @property
    def middle_left(self) -> Optional["Node"]:
        if len(self.children) == 4:
            return self.children[1]
        return None
    
    @property
    def middle_right(self) -> Optional["Node"]:
        if len(self.children) == 4:
            return self.children[2]
        return None
    
    def append_key(self, key: int) -> bool:
        self.keys.append(key)
        self.keys.sort()
        return True
    
    def is_end_node(self) -> bool:
        return False if self.children else True
    
    def __repr__(self):
        return f"Node(keys={self.keys}, parent={self.parent}, children={self.children})"


class TwoThreeFourTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, key_to_insert: int) -> None:
        if self.root is None:
            self.root = Node(keys=[key_to_insert])
        else:
            self._rebalance(self.root, key_to_insert)
            self._insert_helper(self.root, key_to_insert)
        return None
    
    def _rebalance(self, node: Node, key_to_insert: int) -> None:
        if node.is_end_node():
            if len(node.keys) == 3:
                self._split(node)
            return None
        
        if len(node.keys) == 1:
            next_node = node.left if key_to_insert < node.first_key else node.right
        elif len(node.keys) == 2:
            match key_to_insert:
                case key_to_insert if key_to_insert < node.first_key:
                    next_node = node.left
                case key_to_insert if key_to_insert < node.last_key:
                    next_node = node.middle
                case _:
                    next_node = node.right
        else:
            match key_to_insert:
                case key_to_insert if key_to_insert < node.first_key:
                    next_node = node.left
                case key_to_insert if key_to_insert < node.middle_key:
                    next_node = node.middle_left
                case key_to_insert if key_to_insert < node.last_key:
                    next_node = node.middle_right
                case _:
                    next_node = node.right
        
        return self._rebalance(next_node, key_to_insert)
    
    def _insert_helper(self, node: Node, key_to_insert: int) -> None:
        if node.is_end_node():
            node.append_key(key_to_insert)
            return None
        
        # Recursively isnert into the appropriate child
        if len(node.keys) == 1:
            next_node = node.left if key_to_insert < node.first_key else node.right
        elif len(node.keys) == 2:
            match key_to_insert:
                case key_to_insert if key_to_insert < node.first_key:
                    next_node = node.left
                case key_to_insert if key_to_insert < node.last_key:
                    next_node = node.middle
                case _:
                    next_node = node.right
        else:
            match key_to_insert:
                case key_to_insert if key_to_insert < node.first_key:
                    next_node = node.left
                case key_to_insert if key_to_insert < node.middle_key:
                    next_node = node.middle_left
                case key_to_insert if key_to_insert < node.last_key:
                    next_node = node.middle_right
                case _:
                    next_node = node.right
        
        return self._insert_helper(next_node, key_to_insert)
    
    def _split(self, node: Node):
        if node.parent and len(node.parent.keys) == 3:
            self._split(node.parent)

        left, right = Node([node.first_key]), Node([node.last_key])

        if not node.is_end_node():
            left.children.extend([node.left, node.middle_left])
            right.children.extend([node.middle_right, node.right])
            for child in left.children + right.children:
                child.parent = left if child in left.children else right
        
        if node.parent:
            pos = node.parent.children.index(node) if node.parent.children else 0
            node.parent.children[pos: pos] = [left, right]
            left.parent, right.parent = node.parent, node.parent

            node.parent.children.remove(node)
            node.parent.append_key(node.middle_key)
        else:
            self.root = Node(keys=[node.middle_key])
            self.root.children.extend([left, right])
            left.parent, right.parent = self.root, self.root

    def search(self, target: int) -> Optional[Node]:
        return self._search_helper(self.root, target) if self.root else None
    
    def _search_helper(self, node: Node, target: int) -> Optional[Node]:
        if target in node.keys:
            return node
        
        if node.is_end_node():
            return None
        
        if len(node.keys) == 1:
            next_node = node.left if target < node.first_key else node.right
        elif len(node.keys) == 2:
            match target:
                case target if target < node.first_key:
                    next_node = node.left
                case target if target < node.last_key:
                    next_node = node.middle
                case _:
                    next_node = node.right
        else:
            match target:
                case target if target < node.first_key:
                    next_node = node.left
                case target if target < node.middle_key:
                    next_node = node.middle_left
                case target if target < node.last_key:
                    next_node = node.middle_right
                case _:
                    next_node = node.right
        
        return self._search_helper(next_node, target)

    def is_balanced(self) -> bool:
        return self._levelorder(self.root)

    def _levelorder(self, node: Node):
        children_depth: Set[int] = set(self._get_depth(child) for child in node.children)
        if len(children_depth) > 1:
            return False
        
        for child in node.children:
            if not self._levelorder(child):
                return False
        return True
    
    def _get_depth(self, node: Node) -> int:
        if not node.children:
            return 0

        depth: int = 1 + max(self._get_depth(child) for child in node.children)
        return depth
        
class TestTwoThreeFourTree(unittest.TestCase):
    def test_insert_single_element(self):
        tree234 = TwoThreeFourTree()
        tree234.insert(10)
        actual: List[int] = tree234.root.keys
        expected: List[int] = [10]
        self.assertEqual(actual, expected)

    def test_insert_multiple_elements(self):
        tree234 = TwoThreeFourTree()
        tree234.insert(10)
        tree234.insert(20)
        tree234.insert(30)
        tree234.insert(100)
        
        actual: List[int] = tree234.root.keys
        expected: List[int] = [20]
        self.assertEqual(actual, expected)

        actual: List[int] = tree234.root.left.keys
        expected: List[int] = [10]
        self.assertEqual(actual, expected)

        actual: List[int] = tree234.root.right.keys
        expected: List[int] = [30, 100]
        self.assertEqual(actual, expected)

    def test_insert_causes_split(self):
        tree234 = TwoThreeFourTree()
        tree234.insert(10)
        tree234.insert(20)
        tree234.insert(30)
        tree234.insert(40)
        tree234.insert(50)
        actual: List[int] = tree234.root.keys
        expected: List[int] = [20]
        self.assertEqual(actual, expected)

        actual: List[int] = tree234.root.left.keys
        expected: List[int] = [10]
        self.assertEqual(actual, expected)

        actual: List[int] = tree234.root.right.keys
        expected: List[int] = [30, 40, 50]
        self.assertEqual(actual, expected)

    def test_search_existing_key(self):
        tree234 = TwoThreeFourTree()
        tree234.insert(10)
        tree234.insert(20)
        tree234.insert(30)
        
        actual: bool = tree234.search(20) is None
        expected: bool = False
        self.assertEqual(actual, expected)

        actual: bool = 20 in tree234.search(20).keys
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_search_nonexisting_key(self):
        tree234 = TwoThreeFourTree()
        tree234.insert(10)
        tree234.insert(20)
        tree234.insert(30)

        actual: bool = tree234.search(25) is None
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_balanced_after_insertion(self):
        tree234 = TwoThreeFourTree()
        for num in range(10):
            tree234.insert((num + 1) * 10)

        actual: bool = tree234.is_balanced()
        expected: bool = True
        self.assertEqual(actual, expected)

    
if __name__ == "__main__":
    unittest.main()
