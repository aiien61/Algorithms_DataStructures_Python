"""Implement a circular queue with O(1) performance on enqueue() and dequeue() methods
"""
import unittest
from typing import List

class Queue:
    def __init__(self, size: int):
        self.size: int = size
        self.storage: List[int] = [None] * size
        self.front: int = 0
        self.back: int = 0
        self.length: int = 0

    def is_empty(self) -> bool:
        return self.length == 0
    
    def is_full(self) -> bool:
        return self.length == self.size
    
    def enqueue(self, item: int) -> bool:
        if self.is_full():
            return False
        
        self.storage[self.back] = item
        self.back = (self.back + 1) % self.size
        self.length += 1
        return True
    
    def dequeue(self) -> int | None:
        if self.is_empty():
            return None

        temp = self.storage[self.front]
        self.front = (self.front + 1) % self.size
        self.length -= 1
        return temp


class Test(unittest.TestCase):
    def test_enqueue_dequeue(self):
        # Test enqueuing and dequeuing a single element
        q = Queue(1)
        q.enqueue(10)
        expected: int = 10
        actual: int = q.dequeue()
        self.assertEqual(expected, actual)

    def test_enqueue_when_full_queue(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        expected: bool = False
        actual: bool = q.enqueue(100)
        self.assertEqual(expected, actual)

    def test_wrap_around_enqueue(self):
        # Test enqueue operation when the queue wraps around
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        q.dequeue()  # This should remove the first element (1)
        # This should wrap around and insert at the beginning
        q.enqueue(6)
        # Now, 2 should be the front element
        expected: int = 2
        actual: int = q.storage[q.front]
        self.assertEqual(expected, actual)
    
    def test_dequeue_when_empty_queue(self):
        q = Queue(1)
        expected: None = None
        actual: None = q.dequeue()
        self.assertEqual(expected, actual)
    

if __name__ == '__main__':
    unittest.main()
