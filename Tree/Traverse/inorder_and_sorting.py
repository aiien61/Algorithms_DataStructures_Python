import os, sys
sys.path.append(os.pardir)
from utils.treeviewer import plot_tree_graph

import unittest
import numpy as np
from dataclasses import dataclass

class BinarySearchTree:
    @dataclass
    class Node:
        data: int
        times: int = 1
        left: object = None
        right: object = None


    def __init__(self, array: np.ndarray):
        self.array = array
        self.root = None
        self._build_tree()


    def _build_tree(self) -> None:
        for value in self.array:
            if value is None:
                continue
            if np.isnan(value):
                continue
            self.insert(value)
        return None


    def insert(self, value: int) -> None:
        node = self._insert(self.root, value)
        if self.root != node:
            self.root = node
        return None
        

    def _insert(self, root_node: object, value: int) -> object:
        """Return root_node if new node should be linked to it. Otherwise, return new parent node of
        the new node.
        """
        if root_node is None:
            return self.Node(value)
        
        if value == root_node.data:
            root_node.times += 1
            return root_node
        elif value < root_node.data:
            new_node = self._insert(root_node.left, value)
            if root_node.left != new_node:
                root_node.left = new_node        
        elif value > root_node.data:
            new_node = self._insert(root_node.right, value)
            if root_node.right != new_node:
                root_node.right = new_node
        return root_node


    def delete(self, value: int) -> None:
        new_root = self._delete(self.root, value)
        if self.root != new_root:
            self.root = new_root


    def _delete(self, root_node: object, value: int) -> object:
        if root_node is None:
            return None
        
        if value == root_node.data:
            # X X
            if (root_node.left is None) and (root_node.right is None):
                return None
            # left X
            elif (root_node.left is not None) and (root_node.right is None):
                return root_node.left
            # X right
            elif (root_node.left is None) and (root_node.right is not None):
                return root_node.right
            # left right
            elif (root_node.left is not None) and (root_node.right is not None):
                left_max_node = self.get_max(root_node.left)
                self.swap_node_data(root_node, left_max_node)
                new_node_to_link = self._delete(root_node.left, value)
                if root_node.left != new_node_to_link:
                    root_node.left = new_node_to_link

        elif value < root_node.data:
            new_node_to_link = self._delete(root_node.left, value)
            if root_node.left != new_node_to_link:
                root_node.left = new_node_to_link
        elif value > root_node.data:
            new_node_to_link = self._delete(root_node.right, value)
            if root_node.right != new_node_to_link:
                root_node.right = new_node_to_link
        return root_node


    def swap_node_data(self, node1: object, node2: object) -> None:
        value1, value2 = node1.data, node2.data
        node1.data = value2
        node2.data = value1
        return None            


    def get_min(self, root_node: object) -> object:
        if root_node is None:
            return None

        node = root_node
        while node.left is not None:
            node = node.left
        return node


    def get_max(self, root_node: object) -> object:
        if root_node is None:
            return None

        node = root_node
        while node.right is not None:
            node = node.right
        return node


    def traverse(self, order_form: str, order_by: str) -> list:
        result = []
        
        if order_form == "inorder":
            result = self.traverse_inorder(self.root, order_by, result)
        elif order_form == "preorder":
            result = self.traverse_preorder(self.root, order_by, result)
        elif order_form == "postorder":
            result = self.traverse_postorder(self.root, order_by, result)
        
        return result


    def traverse_inorder(self, node: object, order_by: str, stored: list) -> list:
        if node is None:
            return stored

        if order_by == "left":
            self.traverse_inorder(node.left, order_by, stored)
            if node is not None:
                stored.append(node.data)
            self.traverse_inorder(node.right, order_by, stored)
        elif order_by == "right":
            self.traverse_inorder(node.right, order_by, stored)
            if node is not None:
                stored.append(node.data)
            self.traverse_inorder(node.left, order_by, stored)
        
        return stored


class Test(unittest.TestCase):
    unsorted_array = np.array([5, 2, None, 7, 4, 8, 1, 9, 3, 7, 10, 2])
    
    def test_ascending_sort(self):
        bst = BinarySearchTree(self.unsorted_array)
        expected = bst.traverse(order_form="inorder", order_by="left")
        actual = np.full(len(expected), np.nan)
        for i in range(actual.size):
            node = bst.get_min(bst.root)
            actual[i] = node.data
            bst.delete(node.data)
        is_same = np.array_equal(actual, expected)
        self.assertTrue(is_same)

    def test_descending_sort(self):
        bst = BinarySearchTree(self.unsorted_array)
        expected = bst.traverse(order_form="inorder", order_by="right")
        actual = np.full(len(expected), np.nan)
        for i in range(actual.size):
            node = bst.get_max(bst.root)
            actual[i] = node.data
            bst.delete(node.data)
        is_same = np.array_equal(actual, expected)
        self.assertTrue(is_same)


if __name__ == "__main__":
    unittest.main()
    # nums = np.array([5, 2, None, 7, 4, 9, 6, 1, 8, 3, 7, 10, 2])
    # bst = BinarySearchTree(nums)
    # plot_tree_graph(tree_structure="list", to_file="tree.png", tree_root=bst.root)
    
    # traversal = bst.traverse(order_form="inorder", order_by="left")
    # print(traversal)
    
    # sorted_list = []
    # while bst.root is not None:
    #     min_value = bst.get_min(bst.root).data
    #     sorted_list.append(min_value)
    #     bst.delete(min_value)
    # print(sorted_list)

    



    