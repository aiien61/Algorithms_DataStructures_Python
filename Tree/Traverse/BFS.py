import numpy as np
from queue import Queue
from dataclasses import dataclass


class BinaryTreeList:
    @dataclass
    class Node:
        value: int
        right: object = None
        left: object = None


    def __init__(self, array: np.ndarray):
        self.array = array
        self.root = None
        self._build_tree(array)
        

    def _build_tree(self, array: np.ndarray):
        nodes = [self.Node(value) if value is not None else None for value in array]
        self.root = nodes[0]

        for i in range(array.size):
            left_i = (i + 1) * 2 - 1
            right_i = (i + 1) * 2

            if (left_i < array.size) and (nodes[left_i] is not None):
                nodes[i].left = nodes[left_i]
            if (right_i < array.size) and (nodes[right_i] is not None):
                nodes[i].right = nodes[right_i]
        return None
    
    def traverse_levelorder(self):
        if self.root is None:
            return None

        queue = Queue(self.array.size)
        queue.put(self.root)

        result = []
        
        while not queue.empty():
            node = queue.get()
            if node is None:
                continue

            result.append(node.value)

            if node.left is not None:
                queue.put(node.left)
            
            if node.right is not None:
                queue.put(node.right)
        
        return result

if __name__ == "__main__":
    values = [
                           5,
                  2,                     6,
             1,        4,         None,       7,
        None, None, 3, None, None, None, None, None
    ]

    tree = BinaryTreeList(np.array(values))
    level_order = tree.traverse_levelorder()
    print(level_order)
