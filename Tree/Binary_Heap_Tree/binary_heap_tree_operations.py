import os, sys
sys.path.append(os.pardir)
from utils.treeviewer import plot_tree_graph

import numpy as np


class MaxHeap:
    
    def __init__(self, array: np.ndarray):
        self.array = array
        self.i_end = len(array) - 1
        self._build_maxheap()

    
    @staticmethod
    def validate(heaptree: np.ndarray) -> bool:
        is_valid = True
        prev_null = 1 if np.isnan(heaptree[0]) else 0
        current_null = 0

        # allow 00, 11, 01, and avoid 10
        for value in heaptree[1:]:
            if np.isnan(value):
                current_null = 1
            else:
                current_null = 0

            if current_null < prev_null:
                is_valid = False
                break
            prev_null = current_null

        return is_valid
    
    
    def _build_maxheap(self) -> None:
        i = self.i_end

        while np.isnan(self.array[i]):
            i -= 1

        self.i_end = i

        while i >= 0:
            self._shift_down(i)
            i -= 1

        return None
    

    def _shift_down(self, i: int) -> None:
        if i > self.i_end:
            return None

        i_left = (i + 1) * 2 - 1
        i_right = (i + 1) * 2 - 1 + 1
        
        i_bigger = self._get_bigger_value(i_left, i_right)
        if i_bigger < 0:
            return None
        
        if self.array[i] < self.array[i_bigger]:
            self.array[i], self.array[i_bigger] = self.array[i_bigger], self.array[i]
            self._shift_down(i_bigger)

        return None
    

    def _get_bigger_value(self, i_left: int, i_right: int) -> int:
        if i_left > self.i_end:
            return -1
        elif i_right > self.i_end:
            return i_left
        else:
            return i_right if self.array[i_left] < self.array[i_right] else i_left
        
    
    def remove_from_top(self) -> None:
        """Remove the root"""
        i_root = 0
        self.array[i_root], self.array[self.i_end] = self.array[self.i_end], self.array[i_root]
        self.i_end -= 1
        self._shift_down(i_root)
        return None
    

    def append(self, value: int) -> None:
        if (self.i_end + 1) > (self.array.size - 1):
            self.array = self.expand_array(self.array, self.i_end)
        
        self.i_end += 1
        self.array[self.i_end] = value
        self._shift_up(self.i_end)
        return None
    

    def _shift_up(self, i: int) -> None:
        if i <= 0:
            return None

        i_parent = i // 2
        if self.array[i_parent] < self.array[i]:
            self.array[i_parent], self.array[i] = self.array[i], self.array[i_parent]
            self._shift_up(i_parent)
        return None
        

    @staticmethod
    def expand_array(array: np.ndarray, end_index: int) -> np.ndarray:
        new_array = np.full(array.size * 2, np.nan)
        new_array[: (end_index + 1)] = array[: (end_index + 1)]
        return new_array


if __name__ == "__main__":
    values = np.array([66, 78, 27, 35, 6, 2, 50, 58, 29, 76])
    bht = MaxHeap(values)
    print(bht.array)
    bht.array = MaxHeap.expand_array(bht.array, bht.i_end)
    print(bht.array)

    bht.remove_from_top()
    print(bht.array)

    bht.remove_from_top()
    print(bht.array)

    bht.append(1)
    bht.append(2)
    print(bht.array)

    tree_args = {"tree_root_index": 0, "tree_array": bht.array}
    plot_tree_graph(tree_structure="array", to_file="maxheap.png", **tree_args)

    # values = np.array([66, 78, 27, 35, 6, 2, np.nan, 50, 58, 29, 76])
    # is_valid = MaxHeap.validate(values)
    # print(is_valid)

    # values = np.full(20, np.nan)
    # values[: 10] = [66, 78, 27, 35, 6, 2, 50, 58, 29, 76]
    # bht = MaxHeap(values)
    # print(bht.array)
    # print(bht.i_end)
