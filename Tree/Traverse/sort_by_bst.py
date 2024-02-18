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
            if self.left:
                node = BSTNode(value)
                node.left = self.left
                self.left = node
            else:
                self.left = BSTNode(value)
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


    def delete(self, value: int) -> None:
        if value == self.value:
            if self.left is None:
                self = self.right
            elif self.right is None:
                self = self.left
            else:
                left_max_node = self.left.get_max()
                self.value = left_max_node.value
                left_max_node.delete(left_max_node.value)
        elif value < self.value:
            if self.left:
                self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right.delete(value)

        return None
    

    def get_max(self) -> object:
        if self.right is None:
            return self
        return self.right.get_max()
    
    def get_min(self) -> object:
        if self.left is None:
            return self
        return self.left.get_min()


class BST:
    def __init__(self, array: Iterable):
        self.root = BSTNode()
        self._build_tree(array)

    def _build_tree(self, array: Iterable) -> None:
        for value in array:
            self.root.insert(value)
        return None
    
    def traverse_inorder(self, order_by: str) -> None:
        if order_by == "right":
            self._traverse_inorder_dfsright(self.root)
        elif order_by == "left":
            self._traverse_inorder_dfsleft(self.root)
        return None
    
    def _traverse_inorder_dfsright(self, root: BSTNode):
        if not root:
            return None
        
        self._traverse_inorder_dfsright(root.right)
        print(root.value, end=" ")
        self._traverse_inorder_dfsright(root.left)
        return None
    
    def _traverse_inorder_dfsleft(self, root: BSTNode):
        if not root:
            return None

        self._traverse_inorder_dfsleft(root.left)
        print(root.value, end=" ")
        self._traverse_inorder_dfsleft(root.right)
        return None


def tree_sort_ascending(unsorted_array: Iterable) -> None:
    bst = BST(unsorted_array)
    bst.traverse_inorder(order_by="left")
    print()
    return None


def tree_sort_descending(unsorted_array: Iterable) -> None:
    bst = BST(unsorted_array)
    bst.traverse_inorder(order_by="right")
    print()
    return None

    
if __name__ == "__main__":
    unsorted_array = [5, 6, 7, 2, 1, 6, 2]
    print(unsorted_array)
    print("tree sort by dfs left:", end=" ")
    tree_sort_ascending(unsorted_array)
    print("tree sort by dfs right:", end=" ")
    tree_sort_descending(unsorted_array)
