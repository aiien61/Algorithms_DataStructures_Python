import numpy as np
from typing import List


class Queue:
    
    def __init__(self, array: List[int]=None):
        self.i_head = -1
        self.i_tail = -1
        self.queue = self._init_queue(array)            
    

    def _init_queue(self, array: List[int]) -> np.ndarray:
        if array:
            new_array = np.empty(len(array))
            new_array[:] = array
            self.i_head = 0
            self.i_tail = len(array) - 1
            return new_array
        else:
            return np.full(0, np.nan)


    def put(self, value: int) -> None:
        if self.is_full():
            self.queue = self.expand_queue()

        if self.queue.size == 0:
            self.queue = self._init_queue([value])
        elif self.i_tail < 0:
            self.i_head += 1
            self.i_tail += 1
            self.queue[self.i_tail] = value
        else:
            self.i_tail += 1
            self.i_tail = self.i_tail % self.queue.size
            self.queue[self.i_tail] = value

        if self.is_full():
            self.queue = self.expand_queue()

        return None


    def is_full(self):
        if self.size == 0:
            return False

        i_tail = self.i_tail + 1
        i_tail = i_tail % self.queue.size
        return i_tail == self.i_head
    

    def expand_queue(self):
        new_queue = np.full(self.size*2, np.nan)
        i = 0
        while True:
            if self.size == 0:
                break
            value = self.poll()
            new_queue[i] = value
            i += 1

        self.i_head = 0
        self.i_tail = i - 1
        return new_queue


    def poll(self) -> (int, None):
        if self.size == 0:
            return None

        value = self.queue[self.i_head]
        self.queue[self.i_head] = np.nan
        
        self.i_head += 1
        self.i_head = self.i_head % self.queue.size
        if np.isnan(self.queue[self.i_head]):
            self.i_head = self.i_tail = -1
        return value


    @property
    def size(self):
        if (self.i_head < 0) and (self.i_tail < 0):
            return 0
        elif self.i_head <= self.i_tail:
            return self.i_tail - self.i_head + 1
        else:
            return self.queue.size - self.i_head + (self.i_tail + 1)


    def __repr__(self):
        queue = []
        queue_string = "Queue({queue})"
        
        if self.size == 0:
            return queue_string.format(queue=queue)
        
        i = self.i_head
        while True:
            if np.isnan(self.queue[i]):
                break

            queue.append(self.queue[i])

            if i == self.i_tail:
                break

            i += 1
            i = i % self.queue.size
        
        return queue_string.format(queue=queue)


if __name__ == "__main__":
    values = list(range(1, 6))
    queue = Queue(values)
    print(queue) # 1,2,3,4,5
    
    queue.put(6)
    print(queue) # 1,2,3,4,5,6

    for _ in range(queue.size):
        queue.poll()
    print(queue) # []

    value = queue.poll()
    print(value) # None
    print(queue) # []

    for value in range(11, 16):
        queue.put(value)
    print(queue) # 11,12,13,14,15

    for _ in range(4):
        queue.poll()
    print(queue) # 15
    print(queue.queue) # [_ _ _ _ 15 _ _ _ _ _] 
    
    for value in range(6):
        queue.put(value)
    print(queue) # 15,0,1,2,3,4,5
    print(queue.queue) # [5 _ _ _ 15 0 1 2 3 4]

    for value in range(0, 80):
        queue.put(value+30)
    print(queue)
    print(queue.queue)
