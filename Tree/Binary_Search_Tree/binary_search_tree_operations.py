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
    
    def search(self, value: int) -> object:
        node = self.root
        while node is not None:
            if value == node.data:
                return node
            elif value < node.data:
                node = node.left
            elif value > node.data:
                node = node.right
        
        if node is None:
            return None
        else:
            return node

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
    

class BinaryTreeArray:
    def __init__(self, array: np.ndarray):
        self.array = array
        self.tree = np.full(array.size, np.nan)
        self._build_tree(array)

    def _build_tree(self, array: np.ndarray):
        for value in array:
            if (value is None) or (np.isnan(value)):
                continue
            self.insert(value)
        return None
    
    def insert(self, value: int):
        i = 0
        while True:
            try:
                node = self.tree[i]
            except IndexError:
                self.tree = self.expand_array(self.tree)
                node = self.tree[i]

            if np.isnan(node):
                self.tree[i] = value
                break
            elif value < node:
                i = (i + 1) * 2 - 1
            elif value > node:
                i = (i + 1) * 2 - 1 + 1
            else:
                break
        return None
    
    def search(self, value: int) -> int:
        i = 0
        while not np.isnan(self.tree[i]):
            if value == self.tree[i]:
                return self.tree[i], i
            elif value < self.tree[i]:
                i = (i + 1) * 2 - 1
            elif value > self.tree[i]:
                i = (i + 1) * 2 - 1 + 1

            if i >= self.tree.size:
                break
        
        raise ValueError("Not Found")
    
    @staticmethod
    def expand_array(array: np.ndarray) -> np.ndarray:
        new_array = np.full(array.size * 3, np.nan)
        new_array[: array.size] = array
        return new_array
    
    def __repr__(self):
        return str(self.tree)


if __name__ == "__main__":
    # # Binary Search Tree (Linked List)
    # numbers = np.array([5, 2, 6, 1, 4, 7, 3])
    # bst = BinaryTreeList(numbers)
    # plot_tree_graph(bst.root)

    # # search
    # node = bst.search(6)
    # print(node)

    # node = bst.search(10)
    # print(node)

    # # deletion
    # bst.delete(6)
    # plot_tree_graph(bst.root, "delete_middle_with_right.png")
    # bst.delete(7)
    # plot_tree_graph(bst.root, "delete_tail.png")
    # bst.delete(4)
    # plot_tree_graph(bst.root, "delete_middle_with_left.png")
    # bst.delete(2)
    # plot_tree_graph(bst.root, "delete_middle_with_both_left_right.png")
    # bst.delete(5)
    # plot_tree_graph(bst.root, "delete_root.png")

    # Binary Search Tree (Array)
    numbers = np.array([5, 2, None, 7, 4, 8, 1, 9, 3, 7, 10, 2])
    bst = BinaryTreeArray(numbers)
    print(bst)

    tree_args = {"tree_root_index": 0, "tree_array": bst.tree}
    plot_tree_graph(tree_structure="array", to_file="arraytree.png", **tree_args)

    # search
    print(f"search result: {bst.search(10)}")
    print(f"search result: {bst.search(9)}")
    try:
        print(f"search result: {bst.search(11)}")
    except ValueError:
        print('Not Found')
