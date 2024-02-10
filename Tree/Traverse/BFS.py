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
    

class BinaryTreeArray:
    def __init__(self, array: np.ndarray):
        self.array = array

    def traverse_levelorder(self) -> list:
        queue = Queue(self.array.size)
        root_i = 0
        index_boundary = self.array.size
        queue.put(root_i)

        result = []

        while not queue.empty():
            index = queue.get()
            if self.array[index] is None:
                continue

            result.append(self.array[index])

            left_index = (index + 1) * 2 - 1
            right_index = (index + 1) * 2

            if left_index < index_boundary:
                queue.put(left_index)
            
            if right_index < index_boundary:
                queue.put(right_index)
        
        return result


if __name__ == "__main__":
    values = [
                           5,
                  2,                     6,
             1,        4,         None,       7,
        None, None, 3, None, None, None, None, None
    ]

    list_tree = BinaryTreeList(np.array(values))
    level_order = list_tree.traverse_levelorder()
    print(level_order)

    array_tree = BinaryTreeArray(np.array(values))
    level_order = array_tree.traverse_levelorder()
    print(level_order)


