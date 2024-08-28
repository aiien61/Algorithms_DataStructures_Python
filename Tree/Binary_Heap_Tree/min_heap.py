import numpy as np

class MinHeap:
    def __init__(self, size: int=1):
        self.root_index: int = 0
        self._tail_index: int = -1
        self.heap: np.ndarray = np.full(size, np.nan)

    def _swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return None

    def insert(self, value: int) -> bool:
        self._tail_index += 1
        try:
            if np.isnan(self.heap[self._tail_index]):
                self.heap[self._tail_index] = value
        except IndexError:
            new_heap: np.ndarray = np.full(self._tail_index * 3, np.nan)
            new_heap[: self._tail_index] = self.heap
            self.heap = new_heap
            self.heap[self._tail_index] = value
        
        index: int = self._tail_index
        while index > 0:
            parent_index: int = index // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                return True

    def pop(self) -> int | None:
        if np.isnan(self.heap[self.root_index]):
            return None
        
        if self.root_index == self._tail_index:
            min_value: int = self.heap[self._tail_index]
            self._tail_index -= 1
            return int(min_value)
        
        self._swap(self.root_index, self._tail_index)
        min_value: int = int(self.heap[self._tail_index])
        self._tail_index -= 1
        
        index: int = self.root_index
        while True:
            min_index: int = index

            left_child_index: int = index * 2 + 1
            if left_child_index <= self._tail_index:
                if self.heap[left_child_index] < self.heap[min_index]:
                    min_index = left_child_index
            
            right_child_index: int = index * 2 + 2
            if right_child_index <= self._tail_index:
                if self.heap[right_child_index] < self.heap[min_index]:
                    min_index = right_child_index
            
            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                return min_value
