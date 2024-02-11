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
                self.add(value)
        return None
    
    def add(self, value: int) -> None:
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._add_from(self.root, value)
        return None
    
    def _add_from(self, node: object, value: int) -> None:
        if value == node.data:
            node.times += 1
        elif value < node.data:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._add_from(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._add_from(node.right, value)
        return None

if __name__ == "__main__":
    numbers = np.array([5, 2, None, 7, 4, 8, 1, 9, 3, 7, 10, 2])
    bst = BinaryTreeList(numbers)
    plot_tree_graph(bst.root)
