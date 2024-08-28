import unittest
from typing import List
from min_heap import MinHeap


class Test(unittest.TestCase):
    def test_insert_when_single_element(self):
        heap = MinHeap()
        heap.insert(10)
        expected: int = 10
        actual: int = heap.pop()
        self.assertEqual(expected, actual)

    def test_insert_when_multiple_elements(self):
        heap = MinHeap()
        heap.insert(5)
        heap.insert(10)
        heap.insert(3)
        
        expected: int = 3
        actual: int = heap.pop()
        self.assertEqual(expected, actual)

    def test_pop_min_element(self):
        heap = MinHeap()
        heap.insert(5)
        heap.insert(20)
        heap.insert(15)
        heap.insert(10)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 10)

    def test_pop_from_empty_heap(self):
        heap = MinHeap()

        expected = None
        actual = heap.pop()
        self.assertEqual(expected, actual)

    def test_insert_and_pop_all(self):
        heap = MinHeap()
        elements: List[int] = [7, 3, 2, 6, 1]
        for element in elements:
            heap.insert(element)
        
        expected: List[int] = sorted(elements)
        actual: List[int] = [heap.pop() for _ in range(len(elements))]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
