import os, sys
sys.path.append(os.pardir)
from Binary_Search_Tree.binary_search_tree_operations import BinaryTreeList, BinaryTreeArray

import numpy as np
import unittest


def is_valid_list_bst(tree_node: object) -> bool:
    if tree_node is None:
        return True
    return _is_valid_list_bst(tree_node)


def _is_valid_list_bst(tree_node: object) -> bool:
    if tree_node is None:
        return True

    if tree_node.right is not None:
        right_min = BinaryTreeList.get_min(tree_node.right)
        if tree_node.data >= right_min.data:
            return False
        
        right_result = _is_valid_list_bst(tree_node.right)
        if right_result == False:
            return False

    if tree_node.left is not None:
        left_max = BinaryTreeList.get_max(tree_node.left)
        if tree_node.data <= left_max.data:
            return False
        
        left_result = _is_valid_list_bst(tree_node.left)
        if left_result == False:
            return False

    return True


def is_valid_array_bst(tree_array: np.ndarray, tree_node_index: int) -> bool:
    return _is_valid_array_bst(tree_array, tree_node_index)


def _is_valid_array_bst(tree_array: np.ndarray, tree_node_index: int) -> bool:
    try:
        node_data = tree_array[tree_node_index]
        if np.isnan(node_data):
            return True
    except IndexError:
        return True

    right_index = (tree_node_index + 1) * 2 - 1 + 1
    if right_index < tree_array.size:
        right_min = BinaryTreeArray.get_min(tree_array, right_index)
        if node_data >= right_min:
            return False
        
        right_result = _is_valid_array_bst(tree_array, right_index)
        if right_result == False:
            return False
    
    left_index = (tree_node_index + 1) * 2 - 1
    if left_index < tree_array.size:
        left_max = BinaryTreeArray.get_min(tree_array, left_index)
        if node_data <= left_max:
            return False
        
        left_result = _is_valid_array_bst(tree_array, left_index)
        if left_result == False:
            return False
    
    return True

class Test(unittest.TestCase):
    data = np.array([5, 2, None, 7, 4, 8, 1, 9, 3, 7, 10, 2])

    def test_list_bst_validation(self):
        bst = BinaryTreeList(self.data)
        is_valid = is_valid_list_bst(bst.root)
        self.assertTrue(is_valid)
    
    def test_array_bst_validation(self):
        bst = BinaryTreeArray(self.data)
        is_valid = is_valid_array_bst(bst.tree, 0)
        self.assertTrue(is_valid)


if __name__ == "__main__":
    unittest.main()