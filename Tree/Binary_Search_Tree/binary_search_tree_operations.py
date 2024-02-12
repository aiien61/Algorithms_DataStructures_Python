import os, sys
sys.path.append(os.pardir)

import numpy as np
from typing import Iterable
from dataclasses import dataclass

from utils.treeviewer import plot_tree_graph


class BinaryTreeList:
    def __init__(self, array: Iterable):
        self.array = array
        self.root = None
        self._build_tree()

    @dataclass
    class Node:
        data: int
        times: int = 1
        left: object = None
        right: object = None

    def _build_tree(self) -> None:
        for value in self.array:
            if value is not None:
                self.insert(value)
        return None
    
    def insert(self, value: int) -> None:
        node = self._get_insert_position(self.root, value)
        if self.root is None:
            self.root = node
        return None
    
    def _get_insert_position(self, node: object, value: int) -> object:
        if node is None:
            return self.Node(value)

        if value == node.data:
            node.times += 1
        elif value < node.data:
            pole_node = self._get_insert_position(node.left, value)
            if node.left is None:
                node.left = pole_node
        elif value > node.data:
            pole_node = self._get_insert_position(node.right, value)
            if node.right is None:
                node.right = pole_node
        return node
    
    def delete(self, value: int) -> None:
        if self.root is None:
            return None
        new_child_node = self._get_delete_position(self.root, value)
        if self.root != new_child_node:
            self.root = new_child_node
    
    def _get_delete_position(self, node: object, value: int) -> object:
        """Return """
        if node is None:
            return None
        
        node_to_replace = node

        if value == node.data:
            # X X
            if (node.left is None) and (node.right is None):
                node_to_replace = None
            # left X
            elif (node.left is not None) and (node.right is None):
                node_to_replace = node.left
            # X right
            elif (node.left is None) and (node.right is not None):
                node_to_replace = node.right
            # left right
            else:
                min_in_right = self.get_min(node.right)
                self.swap_node_data(node, min_in_right)
                new_child_node = self._get_delete_position(node.right, value)
                if node.right != new_child_node:
                    node.right = new_child_node
        elif value < node.data:
            new_child_node = self._get_delete_position(node.left, value)
            if node.left != new_child_node:
                node.left = new_child_node
        elif value > node.data:
            new_child_node = self._get_delete_position(node.right, value)
            if node.right != new_child_node:
                node.right = new_child_node

        return node_to_replace

    @staticmethod
    def relink(parent_node, child_node, new_node) -> None:
        if parent_node.left == child_node:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        return None
    
    @staticmethod
    def get_min(root) -> object:
        node = root
        while node.left is not None:
            node = node.left
        return node
    
    @staticmethod
    def get_max(root) -> object:
        node = root
        while node.right is not None:
            node = node.right
        return node
    
    @staticmethod
    def swap_node_data(node_x, node_y) -> None:
        node_x.data, node_y.data = node_y.data, node_x.data
        return None


if __name__ == "__main__":
    numbers = np.array([5, 2, None, 7, 4, 8, 1, 9, 3, 7, 10, 2])
    bst = BinaryTreeList(numbers)
    plot_tree_graph(bst.root)
    bst.delete(5)
    plot_tree_graph(bst.root, "delete_root.png")
