import unittest
from typing import List
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: 'Node' = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, value: int) -> bool:
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next
        return True
    
    def dequeue(self) -> int | None:
        if self.is_empty():
            return None
        
        temp: Node = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value


@dataclass
class Entry:
    value: int
    priority: int


class PriorityQueue:
    def __init__(self, size: int):
        self.size: int = size
        self.heap: List[Node] = [None] * size
        self.N: int = -1
    
    def less(self, index1: int, index2: int) -> bool:
        return self.heap[index1].priority < self.heap[index2].priority
    
    def swap(self, index1: int, index2: int) -> bool:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return True
    
    def is_empty(self) -> bool:
        return self.N < 0
    
    def is_full(self) -> bool:
        return self.N == self.size
    
    def enqueue(self, value: int, priority: int) -> bool: 
        if self.is_full():
            raise RuntimeError("The priority queue is full.")

        self.N += 1
        self.heap[self.N] = Entry(value, priority)
        self.swim(self.N)
        return True

    def dequeue(self) -> int | None:
        if self.is_empty():
            return None
        
        max_entry: int = self.heap[0]
        self.swap(0, self.N)
        self.heap[self.N] = None
        self.N -= 1
        self.sink(0)
        return max_entry.value

    def swim(self, index: int) -> bool:
        while index > 0 and self.less(index // 2, index):
            self.swap(index // 2, index)
            index = index // 2
        return True
    
    def sink(self, index: int) -> bool:
        while (index + 1) * 2 <= self.size:
            max_index: int = index
            if self.heap[index * 2 + 1] is not None:
                if self.less(max_index, index * 2 + 1):
                    max_index = index * 2 + 1
            
            if self.heap[index * 2 + 2] is not None:
                if self.less(max_index, index * 2 + 2):
                    max_index = index * 2 + 2
            
            if max_index == index:
                break

            self.swap(index, max_index)
            index = max_index
        return True
    
def iterator(priority_queue: PriorityQueue):
    return [entry.value for entry in priority_queue.heap]


class Test(unittest.TestCase):
    def test_enqueue_when_single_element(self):
        pq = PriorityQueue(1)
        pq.enqueue(5, 1)   # Element 5 with priority 1
        expected: int = 5
        actual: int = pq.dequeue()
        self.assertEqual(expected, actual)

    def test_enqueue_when_multiple_elements(self):
        pq = PriorityQueue(3)
        pq.enqueue(5, 2)   # Element 5 with priority 1
        pq.enqueue(10, 1)
        pq.enqueue(1, 0)
        expected: int = 5
        actual: int = pq.dequeue()
        self.assertEqual(expected, actual)

    def test_dequeue_when_single_element(self):
        pq = PriorityQueue(1)
        pq.enqueue(5, 1)   # Element 5 with priority 1
        pq.dequeue()
        expected: bool = True
        actual: bool = pq.is_empty()
        self.assertEqual(expected, actual)

    def test_dequeue_when_multiple_elements(self):
        pq = PriorityQueue(3)
        pq.enqueue(5, 2)   # Element 5 with priority 1
        pq.enqueue(10, 1)
        pq.enqueue(1, 0)
        expected: List[int] = [5, 10, 1]
        actual: List[int] = [pq.dequeue() for _ in range(pq.size)]
        self.assertEqual(expected, actual)

    def test_dequeue_when_empty_queue(self):
        pq = PriorityQueue(1)
        expected: None = None
        actual: None = pq.dequeue()
        self.assertEqual(expected, actual)

    def test_enqueue_when_multiple_same_priority_elements(self):
        pq = PriorityQueue(3)
        pq.enqueue(5, 1)   # Element 5 with priority 1
        pq.enqueue(10, 1)
        pq.enqueue(1, 1)
        expected: List[int] = [5, 10, 1]
        actual: List[int] = [pq.heap[i].value for i in range(pq.size)]
        self.assertEqual(expected, actual)

    def test_enqueue_when_multiple_same_priority_string_elements(self):
        pq = PriorityQueue(3)
        pq.enqueue('a', 1)   # Element 5 with priority 1
        pq.enqueue('c', 1)
        pq.enqueue('b', 1)
        expected: List[int] = ['a', 'c', 'b']
        actual: List[int] = [pq.heap[i].value for i in range(pq.size)]
        self.assertEqual(expected, actual)

    

if __name__ == '__main__':
    # unittest.main()

    pq = PriorityQueue(3)
    pq.enqueue(5, 0)
    pq.enqueue(10, 2)
    pq.enqueue(1, 1)
    print(iterator(pq))
