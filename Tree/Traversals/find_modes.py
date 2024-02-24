from typing import Iterable


class BSTNode:
    def __init__(self, value: int=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int) -> None:
        if self.value is None:
            self.value = value
            return None
        
        if value == self.value:
            node = BSTNode(value)
            if self.left:
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
    
    def delete(self, value: int) -> None:
        if self.value is None:
            return None

        # search node of value
        if value == self.value:
            if self.left is None:
                self = self.right
            elif self.right is None:
                self = self.left
            else:
                left_max = self.left.get_max()
                self.value = left_max.value
                left_max.delete(left_max.value)
        elif value < self.value:
            if self.left:
                self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right.delete(value)

        return None
    
    def get_max(self) -> object:
        if not self.right:
            return self
        return self.right.get_max()


def build_tree(root: BSTNode, array: Iterable[int]) -> BSTNode:
    if not root:
        root = BSTNode()
    
    for value in array:
        root.insert(value)
    return root
            

class Solution:
    prev_node = None
    count = 0
    max_count = 0
    modes = []        


    @classmethod
    def find_modes(cls, tree_node: BSTNode) -> Iterable:
        if not tree_node:
            return cls.modes
        
        if tree_node.value is None:
            return cls.modes
        
        # traverse to count all values by in-order
        cls.find_modes(tree_node.left)

        if cls.prev_node is None:
            cls.prev_node = tree_node
            cls.count = 1
        else:
            if tree_node.value == cls.prev_node.value:
                cls.count += 1
            else:
                cls.prev_node = tree_node
                cls.count = 1

        if cls.count > cls.max_count:
            cls.modes = [tree_node.value]
            cls.max_count = cls.count

        elif cls.count == cls.max_count:
            cls.modes.append(tree_node.value)

        cls.find_modes(tree_node.right)
        return cls.modes


if __name__ == "__main__":
    nums = [10, 1, 2, 5, 3, 2, 5, 2, 10, 5, 5]
    bst_node = BSTNode()
    bst_node = build_tree(bst_node, nums)
    modes = Solution.find_modes(bst_node)
    print(modes)