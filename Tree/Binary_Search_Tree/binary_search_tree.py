import random
import numpy as np
from dataclasses import dataclass

@dataclass
class TreeNode:
    value: int
    right: 'TreeNode' = None
    left: 'TreeNode' = None


# TODO: add methods delete()
class BSTreeList:
    def __init__(self):
        self.root: 'TreeNode' = None

    def insert(self, value: int) -> bool:
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node

        temp: 'TreeNode' = self.root
        while True:
            if temp.value == value:
                return False
            
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
        return False
    
    def contains(self, value: int) -> bool:
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


class BSTreeArray:
    def __init__(self, size: int=1):
        self.root_index: int = 0
        self.array: np.ndarray = np.full(size, np.nan)

    @property
    def root(self) -> int | None:
        return self.array[self.root_index]
    
    def insert(self, value: int) -> bool:
        if np.isnan(self.root):
            self.array[self.root_index] = value
            return True
        
        index: int = self.root_index
        try:
            while True:
                if self.array[index] == value:
                    return False
                
                if value < self.array[index]:
                    index = index * 2 + 1
                    if np.isnan(self.array[index]):
                        self.array[index] = value
                        return True
                else:
                    index = index * 2 + 2
                    if np.isnan(self.array[index]):
                        self.array[index] = value
                        return True
        except IndexError:
            new_array: np.ndarray = np.full(self.array.size * 3, np.nan)
            new_array[: self.array.size] = self.array
            self.array = new_array
            self.array[index] = value

        return False
    
    def contains(self, value: int) -> bool:
        index: int = self.root_index
        has_value: bool = False
        try:
            while not np.isnan(self.array[index]):
                if value < self.array[index]:
                    index = index * 2 + 1
                elif value > self.array[index]:
                    index = index * 2 + 2
                else:
                    has_value = True
                    break
        except IndexError:
            has_value = False
        finally:
            return has_value
