import unittest
from typing import List
from stack_by_list import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        numbers = list(range(1, 6))
        mystack = Stack()
        for n in numbers:
            mystack.push(n)

        expected: List[int] = [1, 2, 3, 4, 5]
        actual: List[int] = mystack.stack_list
        self.assertEqual(expected, actual)

        expected: int = 5
        actual: int = mystack.height
        self.assertEqual(expected, actual)

    def test_pop(self):
        numbers = list(range(1, 7))
        mystack = Stack()
        for n in numbers:
            mystack.push(n)

        for _ in range(5):
            mystack.pop()

        expected: int = 1
        actual: int = mystack.pop()
        self.assertEqual(expected, actual)

        expected: int = 0
        actual: int = mystack.height
        self.assertEqual(expected, actual)

    def test_peek(self):
        numbers = list(range(1, 6))
        mystack = Stack()
        for n in numbers:
            mystack.push(n)

        expected: int = 5
        actual: int = mystack.peek()
        self.assertEqual(expected, actual)

    def test_is_empty_when_stack_is_empty(self):
        mystack = Stack()
        expected: bool = True
        actual: bool = mystack.is_empty()
        self.assertEqual(expected, actual)

    def test_is_empty_when_stack_is_not_empty(self):
        numbers = list(range(1, 6))
        mystack = Stack()
        for n in numbers:
            mystack.push(n)

        expected: bool = False
        actual: bool = mystack.is_empty()
        self.assertEqual(expected, actual)

    def test_pop_from_empty_stack(self):
        mystack = Stack()
        expected: None = None
        actual: int | None = mystack.pop()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()