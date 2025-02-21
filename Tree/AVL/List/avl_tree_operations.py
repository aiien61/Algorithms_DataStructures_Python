"""AVL tree basic operations"""
import os, sys
sys.path.append(os.pardir)
from utils.treeviewer import plot_tree_graph

from typing import Iterable


class BSTNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value: int) -> None:
        if self.value is None:
            self.value = value
            return None

        if value == self.value:
            node = BSTNode(value)
            node.left = self.left
            self.left = node
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        return None


    def delete(self, value: int) -> object:
        if value == self.value:
            if self.left is None:
                self = self.right
            elif self.right is None:
                self = self.left
            else:
                left_max = self._get_max(self.left)
                self.value = left_max.value
                self.left = self.left.delete(left_max.value)
        elif value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        return self


    def search(self, value: int) -> object:
        if value == self.value:
            return self
        elif value < self.value:
            if self.left:
                return self.left.search(value)
        elif value > self.value:
            if self.right:
                return self.right.search(value)
        return None


    def _get_max(self, node: object) -> object:
        if node.right is None:
            return node
        return self._get_max(node.right)


class AVL_Tree:

    def __init__(self, array: Iterable=None):
        self.root = BSTNode()
        if array:
            self.build_tree(array)


    def build_tree(self, array: Iterable) -> None:
        for value in array:
            if value is None:
                continue
            
            self.insert(value)

        return None


    def insert(self, value: int) -> None:
        self.root.insert(value)
        self.root = self._balancing(self.root)
        return None


    def delete(self, value: int) -> None:
        self.root.delete(value)
        self.root = self._balancing(self.root)
        return None


    def _balancing(self, node: BSTNode) -> BSTNode:
        depth_gap = self._get_depth_gap(node)
        if abs(depth_gap) < 2:
            return node
        
        # deeper left
        if depth_gap > 1:
            node.left = self._balancing(node.left)
        # deeper right
        elif depth_gap < -1:
            node.right = self._balancing(node.right)
        
        depth_gap = self._get_depth_gap(node)
        if abs(depth_gap) < 2:
            return node
        
        # main logic
        # deeper left
        if depth_gap > 1:
            subtree_gap = self._get_depth_gap(node.left)
            if subtree_gap > 0:
                # LL
                pass
            elif subtree_gap < 0:
                # LR
                node.left = self._left_rotate(node.left)
            node = self._right_rotate(node)
        # deeper right
        elif depth_gap < -1:
            subtree_gap = self._get_depth_gap(node.right)
            if subtree_gap < 0:
                # RR
                pass
            elif subtree_gap > 0:
                # RL
                node.right = self._right_rotate(node.right)
            node = self._left_rotate(node)
        
        return node

    
    def _left_rotate(self, node: BSTNode) -> object:
        pivot = node.right
        node.right = pivot.left
        pivot.left = node
        return pivot


    def _right_rotate(self, node:BSTNode) -> object:
        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        return pivot


    def _get_depth_gap(self, node: BSTNode) -> int:
        left_depth = self._get_depth(node.left)
        right_depth = self._get_depth(node.right)
        return left_depth - right_depth


    def _get_depth(self, node: BSTNode) -> int:
        if node is None:
            return 0
        depth = 1 + max(self._get_depth(node.left), self._get_depth(node.right))
        return depth


if __name__ == "__main__":
    nums = [100, 80, 60, 50, 20, 70]
    avl_tree = AVL_Tree(nums)
    plot_tree_graph(tree_structure="list",
                    to_file="AVL.png", tree_root=avl_tree.root)

    avl_tree.delete(50)
    plot_tree_graph(tree_structure="list",
                    to_file="AVL_delete_50.png", tree_root=avl_tree.root)
    
    avl_tree.delete(20)
    plot_tree_graph(tree_structure="list",
                    to_file="AVL_delete_20.png", tree_root=avl_tree.root)
    
    # LL
    nums = [5, 4, 3]
    avl_ll = AVL_Tree()
    for i, num in enumerate(nums):
        avl_ll.insert(num)
        file_name = f"AVL_LL_{i+1}.png"
        plot_tree_graph(tree_structure="list",
                        to_file=file_name, tree_root=avl_ll.root)
        
    # LR
    nums = [5, 3, 4]
    avl_lr = AVL_Tree()
    for i, num in enumerate(nums):
        avl_lr.insert(num)
        file_name = f"AVL_LR_{i+1}.png"
        plot_tree_graph(tree_structure='list', 
                        to_file=file_name, tree_root=avl_lr.root)

    # RR
    nums = [3, 4, 5]
    avl_rr = AVL_Tree()
    for i, num in enumerate(nums):
        avl_rr.insert(num)
        file_name = f"AVL_RR_{i+1}.png"
        plot_tree_graph(tree_structure='list',
                        to_file=file_name, tree_root=avl_rr.root)
        
    # RL
    nums = [3, 5, 4]
    avl_rl = AVL_Tree()
    for i, num in enumerate(nums):
        avl_rl.insert(num)
        file_name = f"AVL_RL_{i+1}.png"
        plot_tree_graph(tree_structure='list',
                        to_file=file_name, tree_root=avl_rl.root)
