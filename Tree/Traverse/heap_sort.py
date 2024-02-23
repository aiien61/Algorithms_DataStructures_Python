import numpy as np
from typing import Iterable


def is_valid_heaptree(heaptree: Iterable) -> bool:
    is_valid = True
    prev_is_null = 1 if heaptree[0] is None else 0
    current_is_null = 0
    # only 00, 01, 11 allowed
    for value in heaptree[1:]:
        if value is None:
            current_is_null = 1
        else:
            current_is_null = 0

        if current_is_null < prev_is_null:
            is_valid = False
            break
        prev_is_null = current_is_null
    return is_valid


class MaxHeap:
    def __init__(self, array: Iterable):
        self.array = array
        self.i_end = len(array) - 1
        self._build_maxheap()
    
    def _build_maxheap(self) -> None:
        i = self.i_end
        while True:
            if i < 0:
                break
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
        i_root = 0
        self.array[i_root], self.array[self.i_end] = self.array[self.i_end], self.array[i_root]
        self.i_end -= 1
        self._shift_down(i_root)
        return None



class MinHeap:
    def __init__(self, array: Iterable):
        self.array = array
        self.i_end = len(array) - 1
        self._build_minheap()

    def _build_minheap(self) -> None:
        i = self.i_end
        while True:
            if i < 0:
                break
            self._shift_down(i)
            i -= 1
        return None

    def _shift_down(self, i: int) -> None:
        if i > self.i_end:
            return None

        i_left = (i + 1) * 2 - 1
        i_right = (i + 1) * 2 - 1 + 1
        i_smaller = self._get_smaller_value(i_left, i_right)
        if i_smaller < 0:
            return None

        if self.array[i_smaller] < self.array[i]:
            self.array[i], self.array[i_smaller] = self.array[i_smaller], self.array[i]
            self._shift_down(i_smaller)

        return None

    def _get_smaller_value(self, i_left: int, i_right: int) -> int:
        if i_left > self.i_end:
            return -1
        elif i_right > self.i_end:
            return i_left
        else:
            return i_left if self.array[i_left] < self.array[i_right] else i_right

    def remove_from_top(self) -> None:
        i_root = 0
        self.array[i_root], self.array[self.i_end] = self.array[self.i_end], self.array[i_root]
        self.i_end -= 1
        self._shift_down(i_root)
        return None


class HeapSort:
    @staticmethod
    def sort_ascending(array: Iterable) -> Iterable:
        maxheap = MaxHeap(array)
        i_bound = maxheap.i_end + 1
        i = maxheap.i_end
        while True:
            if i < 0:
                break
            maxheap.remove_from_top()
            i -= 1
        return maxheap.array[: i_bound]
    
    @staticmethod
    def sort_descending(array: Iterable) -> Iterable:
        minheap = MinHeap(array)
        i_bound = minheap.i_end + 1
        i = minheap.i_end
        while True:
            if i < 0:
                break
            minheap.remove_from_top()
            i -= 1
        return minheap.array[: i_bound]

if __name__ == "__main__":
    unsorted_array = [66, 78, 27, 35, 6, 2, 50, 58, 29, 76]
    
    ascending_array = HeapSort.sort_ascending(unsorted_array)
    print(ascending_array)

    descending_array = HeapSort.sort_descending(unsorted_array)
    print(descending_array)
