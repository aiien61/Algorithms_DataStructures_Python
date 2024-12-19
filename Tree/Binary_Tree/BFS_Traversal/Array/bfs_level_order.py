from typing import List, Deque
from collections import deque
from icecream import ic
import unittest

ic.disable()

class BinaryTree:
    def __init__(self, array: List[int]):
        self.array = array
        self.root_index: int = None if not array else 0

    def traverse_level_order_bfs(self) -> None:
        # result of level order
        result: List[int] = []
        ic(self.root_index)

        # condition to cease
        if self.root_index is None:
            return result

        # initiate a container to store and hand out tree nodes in level order
        queue: Deque = deque([self.root_index])
        ic(queue)

        # condition to stop the loop
        while queue:
            # pull out the first element from the container to do something
            node_i: int = queue.popleft()
            ic(node_i)
            if self.array[node_i]:
                result.append(self.array[node_i])

            # push the left child of the node into the container
            left_child_index: int = (node_i + 1) * 2 - 1
            if left_child_index < len(self.array):
                queue.append(left_child_index)

            # push the right child of the node into the container
            right_child_index: int = (node_i + 1) * 2
            if right_child_index < len(self.array):
                queue.append(right_child_index)
        
        return result


class TestBinaryTreeArray(unittest.TestCase):
    def test_empty_tree(self):
        bt = BinaryTree([])
        expected: list = []
        actual: list = bt.traverse_level_order_bfs()
        self.assertEqual(expected, actual)

    def test_single_node_tree(self):
        bt = BinaryTree([1])
        expected: List[int] = [1]
        actual: List[int] = bt.traverse_level_order_bfs()
        self.assertEqual(expected, actual)

    def test_complete_tree(self):
        bt = BinaryTree([1, 2, 3, 4, 5, 6, 7])
        expected: List[int] = [1, 2, 3, 4, 5, 6, 7]
        actual: List[int] = bt.traverse_level_order_bfs()
        self.assertEqual(expected, actual)

    def test_incomplete_tree(self):
        bt = BinaryTree([1, 2, 3, None, 5, 6])
        expected: List[int] = [1, 2, 3, 5, 6]
        actual: List[int] = bt.traverse_level_order_bfs()
        self.assertEqual(expected, actual)

    def test_tree_with_all_none(self):
        bt = BinaryTree([None, None, None])
        expected: list = []
        actual: list = bt.traverse_level_order_bfs()
        self.assertEqual(expected, actual)

    def test_tree_with_only_left_subtree(self):
        bt = BinaryTree([1 ,2, None, 4, None])
        expected: list = [1, 2, 4]
        actual: list = bt.traverse_level_order_bfs()
        self.assertEqual(expected, actual)

    def test_tree_with_only_right_subtree(self):
        bt = BinaryTree([1, None, 3, None, None, None, 7])
        expected: list = [1, 3, 7]
        actual: list = bt.traverse_level_order_bfs()
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
