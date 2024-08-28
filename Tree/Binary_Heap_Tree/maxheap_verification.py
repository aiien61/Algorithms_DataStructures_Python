import unittest
from typing import List
from max_heap import MaxHeap

class Test(unittest.TestCase):
    def test_insert_when_single_element(self):
        heap = MaxHeap()
        heap.insert(10)
        expected: int = 10
        actual: int = heap.pop()
        self.assertEqual(expected, actual)

    def test_insert_when_multiple_elements(self):
        heap = MaxHeap()
        heap.insert(5)
        heap.insert(10)
        heap.insert(3)
        expected: int = 10
        actual: int = heap.pop()
        self.assertEqual(expected, actual)

    def test_pop_max_element(self):
        heap = MaxHeap()
        heap.insert(5)
        heap.insert(20)
        heap.insert(15)
        heap.insert(10)
        self.assertEqual(heap.pop(), 20)
        self.assertEqual(heap.pop(), 15)

    def test_pop_from_empty_heap(self):
        heap = MaxHeap()
        expected = None
        actual = heap.pop()
        self.assertEqual(expected, actual)

    def test_insert_and_pop_all(self):
        heap = MaxHeap()
        elements = [2, 3, 1, 7, 6]
        for element in elements:
            heap.insert(element)
        
        expected: List[int] = sorted(elements, reverse=True)
        actual: List[int] = [heap.pop() for _ in range(len(elements))]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
