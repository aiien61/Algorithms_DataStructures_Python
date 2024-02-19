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
            

def find_modes(tree_node: BSTNode) -> Iterable:
    if not tree_node:
        return []

    if tree_node.value is None:
        return []
    
    seen = {}
    counter = _find_modes(tree_node, seen)
    return count_most_common(counter)


def _find_modes(tree_node: BSTNode, seen: Iterable) -> Iterable:
    if not tree_node:
        return None
    
    # traverse to count all values by in-order
    _find_modes(tree_node.left, seen)
    if tree_node.value not in seen:
        seen[tree_node.value] = 1
    else:
        seen[tree_node.value] += 1
    _find_modes(tree_node.right, seen)

    return seen


def count_most_common(counter: dict) -> Iterable:
    max = 0
    modes = []
    for k, v in counter.items():
        if v == max:
            modes.append(k)
        elif v > max:
            modes = [k]
            max = v
    return modes


if __name__ == "__main__":
    nums = [10, 1, 2, 5, 3, 2, 5, 2, 10, 5]
    bst_node = BSTNode()
    bst_node = build_tree(bst_node, nums)
    modes = find_modes(bst_node)
    print(modes)