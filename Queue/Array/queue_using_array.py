import unittest
import numpy as np
from typing import List, Any

class QueueCircularArray:
    def __init__(self, value: Any=None):
        self.i_front: int = -1
        self.i_rear: int = -1
        self.array: np.ndarray = np.full(1, np.nan)
        if value is not None:
            self.enqueue(value)

    @property
    def length(self) -> int:
        if self.i_front < 0 and self.i_rear < 0:
            return 0
        elif self.i_front <= self.i_rear:
            return self.i_rear - self.i_front + 1
        else:
            return (self.array.size - self.i_front) + (self.i_rear + 1)

    @property
    def front(self) -> Any:
        return None if self.length == 0 else self.array[self.i_front]

    @property
    def rear(self) -> Any:
        return None if self.length == 0 else self.array[self.i_rear]

    @staticmethod
    def expand_array(array: np.ndarray, i_front: int, i_rear: int, length: int) -> np.ndarray:
        new_array = np.full(length * 2, np.nan)
        if i_front <= i_rear:
            new_array[i_front: (i_rear+1)] = array
        else:
            new_array[:(length - i_front)] = array[i_front:]
            new_array[(length - i_front): (length - i_front + i_rear + 1)] = array[:(i_rear + 1)]
        return new_array
    
    @staticmethod
    def is_empty(array: np.ndarray) -> bool:
        return np.isnan(array).all()

    def return_queue(self) -> List[Any]:
        i = self.i_front
        queue = []
        while True:
            if i == self.i_rear:
                break
            queue.append(self.array[i])
            i = (i + 1) % self.array.size

        if not np.isnan(self.array[self.i_rear]):
            queue.append(self.array[self.i_rear])
        
        return queue


    def enqueue(self, value: Any) -> bool:
        if self.length == 0:
            self.array[0] = value
            self.i_front += 1
            self.i_rear += 1
            return True
        
        try:
            new_i_rear = (self.i_rear + 1) % self.array.size
            assert np.isnan(self.array[new_i_rear])
        except AssertionError:
            new_array = self.expand_array(self.array, self.i_front, self.i_rear, self.length)
            self.array = new_array
            self.i_front = 0
            self.i_rear = np.sum(~np.isnan(self.array))  # do not use self.length to represent i_rear
            self.array[self.i_rear] = value
        else:
            self.array[new_i_rear] = value
            self.i_rear = new_i_rear
        finally:
            return True, self.array, self.i_front, self.i_rear, self.length

        
    def dequeue(self) -> Any:
        if self.length == 0:
            return None

        temp = self.array[self.i_front]
        self.array[self.i_front] = np.nan
        self.i_front += 1
        self.i_front %= self.array.size

        if self.is_empty(self.array):
            self.i_front = -1
            self.i_rear = -1

        return temp


class Test(unittest.TestCase):
    def test_enqueue(self):
        q = QueueCircularArray()
        for i in range(1, 6):
            q.enqueue(i)
        self.assertEqual(q.return_queue(), [1, 2, 3, 4, 5])

    def test_dequeue(self):
        q = QueueCircularArray()
        for i in range(1, 6):
            q.enqueue(i)
        
        expected = 1
        actual = q.dequeue()
        self.assertEqual(expected, actual)

        expected = [2, 3, 4, 5]
        actual = q.return_queue()
        self.assertEqual(expected, actual)

        for _ in range(4):
            q.dequeue()

        expected = None
        actual = q.dequeue()
        self.assertEqual(expected, actual)

        expected = []
        actual = q.return_queue()
        self.assertEqual(expected, actual) 

    def test_circular_array(self):
        q = QueueCircularArray()
        for i in range(1, 6):
            q.enqueue(i)
        for _ in range(4):
            q.dequeue()
        
        for i in range(15, 20):
            q.enqueue(i)

        expected = [5, 15, 16, 17, 18, 19]
        actual = q.return_queue()
        self.assertEqual(expected, actual)

        for i in range(30, 40):
            q.enqueue(i)
        expected = [5, 15, 16, 17, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        actual = q.return_queue()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()